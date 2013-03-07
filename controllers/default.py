# -*- coding: utf-8 -*-
#########################################################################
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

from array import *
import os

def index():
    basketball_schedules = db(db.basketball.winner == None).select(db.basketball.ALL, orderby=db.basketball.date)  
    dodgeball_schedules = db(db.dodgeball.winner == None).select(db.dodgeball.ALL, orderby=db.dodgeball.date)  
    flag_football_schedules = db(db.flag_football.winner == None).select(db.flag_football.ALL, orderby=db.flag_football.date)  
    indoor_soccer_schedules = db(db.indoor_soccer.winner == None).select(db.indoor_soccer.ALL, orderby=db.indoor_soccer.date)  
    soccer_schedules = db(db.soccer.winner == None).select(db.soccer.ALL, orderby=db.soccer.date)  
    softball_schedules = db(db.softball.winner == None).select(db.softball.ALL, orderby=db.softball.date)  
    ultimate_frisbee_schedules = db(db.ultimate_frisbee.winner == None).select(db.ultimate_frisbee.ALL, orderby=db.ultimate_frisbee.date)  
    volleyball_schedules = db(db.volleyball.winner == None).select(db.volleyball.ALL, orderby=db.volleyball.date)  
    water_polo_schedules = db(db.water_polo.winner == None).select(db.water_polo.ALL, orderby=db.water_polo.date)
      
    return dict(basketball_schedules=basketball_schedules, dodgeball_schedules=dodgeball_schedules,
                flag_football_schedules=flag_football_schedules, indoor_soccer_schedules=indoor_soccer_schedules,
                soccer_schedules=soccer_schedules,
                softball_schedules=softball_schedules, ultimate_frisbee_schedules=ultimate_frisbee_schedules,
                volleyball_schedules=volleyball_schedules, water_polo_schedules=water_polo_schedules)

#######################        Player Profiles    ############################

@auth.requires_login()
def profile():
    flag = False
    team_id = None
    if request.args(0):
        player = db.auth_user(request.args[0]) or redirect(URL('index'))
        if request.args(1):
            team_id = request.args(1) or redirect(URL('index'))
            flag = True
    else:
        player = db(db.auth_user.id == auth.user_id).select().first()
        team_id = None
        flag = False
    leader_invites = db((db.team_leader_invites.receiver == player.id)).select()
    team_invites = db(db.team_inviting_players.receiver == player.id).select()
    return dict(player=player, leader_invites=leader_invites, team_invites=team_invites, flag=flag, team_id=team_id)

def invite_player():
    player = db.auth_user(request.args(0)) or redirect('index')
    team_id = request.args(1) or redirect('index')
    temp = db(db.team_inviting_players.sender==team_id and db.team_inviting_players.receiver==player.id).select()
    count = 0
    for row in temp:
        count = count + 1
    if (count==0):
        db.team_inviting_players.insert(sender=team_id , receiver=player.id)
        db.commit()
    session.flash='Invite Successful'
    redirect(URL('search_for_players', args=[team_id]))
    
#######################   Functions related to invites  ######################

@auth.requires_login()
def accept():
    table_abbr = request.args[0] or redirect('index')    
    destination = request.args[1] or redirect('index')
    
    # update the invites table then do the neccessary action to submit the accept
    if table_abbr == 'tli':
        invite = db.team_leader_invites(request.args[2]) or redirect('index')        
        invite.update_record(pending = False)
        if invite.team.team_leader_2 == None:
            invite.team.update_record(team_leader_2 = auth.user_id)
            db(db.team_leader_invites.id == invite.id).delete()
            db.commit()
            session.flash = 'You have been assigned the team leader'
            redirect(URL(destination))
        elif invite.team.team_leader_3 == None:
            invite.team.update_record(team_leader_3 = auth.user_id)
            db(db.team_leader_invites.id == invite.id).delete()
            db.commit()
            session.flash = 'You have been assigned the team leader'
            redirect(URL(destination))
        else:
            session.falsh = 'The team already has three leaders. Please contact your Originial team leader'
            redirect(URL(destination))
  
    elif table_abbr == 'pat':
        invite = db.player_asking_teams(request.args[2]) or redirect('index')
        invite.update_record(pending = False)
        team_id = invite.receiver.id
        db.team_players.insert(team = invite.receiver.id, player = invite.sender.id)
        invite.receiver.update_record(number_of_players = invite.receiver.number_of_players + 1)
        db(db.player_asking_teams.id == invite.id).delete()
        db.commit()
        #session.flash = invite.sender.name + 'is now part of your team'
        redirect(URL(destination, args=[team_id]))
        
    elif table_abbr == 'tip':
        invite = db.team_inviting_players(request.args[2]) or redirect('index')
        invite.update_record(pending = False)
        db.team_players.insert(team = invite.sender.id, player = auth.user_id)
        invite.sender.update_record(number_of_players = invite.sender.number_of_players + 1)
        db(db.team_inviting_players.id == invite.id).delete()
        db.commit()
        #session.flash = 'You are now a member of the ' + invite.sender.name
        redirect(URL(destination))
        
    else:
        session.flash = 'wrong arguments passed, try again'
        redirect(URL(destination))
        
@auth.requires_login()
def decline():
    table_abbr = request.args[0] or redirect('index')    
    destination = request.args[1] or redirect('index')
    
    # update the invites table then do the neccessary action to submit the decline
    if table_abbr == 'tli':
        db(db.team_leader_invites.id == request.args(2)).delete()
        db.commit()
        redirect(URL(destination))
  
    elif table_abbr == 'pat':
        db(db.player_asking_teams.id == request.args[2]).delete()
        db.commit()
        redirect(URL(destination))
        
    elif table_abbr == 'tip':
        invite = db(db.team_inviting_players.id == request.args[2]).delete()
        db.commit()
        redirect(URL(destination))
        
    else:
        session.flash = 'wrong arguments passed, try again'
        redirect(URL(destination))


def drop_player():
    team_player = db.team_players(request.args[0]) or redirect(URL('my_teams'))
    team_id = team_player.team.id
    form = SQLFORM.factory(Field('confirm_deletion', 'boolean', default=False))
    if form.process().accepted:
        if form.vars.confirm_deletion == True:
            if team_player.player.id == team_player.team.team_leader_2:
                team_player.team.update_record(team_leader_2 = None)
            if team_player.player.id == team_player.team.team_leader_3:
                team_player.team.update_record(team_leader_3 = None)
            db(db.team_players.id == request.args[0]).delete()
            db.commit()
            redirect(URL('team', args=team_id))
        else:
            redirect(URL('team', args=team_id))
    return dict(form=form, player=team_player.player)


#######################   Teams related functions ############################

@auth.requires_login()
def team_signup():
    # Players can be part of one team only so here in the sports drop down
    # the categories that they already have a team in wont be displayed 
    players_teams = db(db.team_players.player == auth.user_id).select()
    sports=[]
    for team in players_teams:
        sports.append(team.team.sport)
        
    sport=['Basketball', 'Dodgeball', 'Flag Football',
           'Indoor Soccer', 'Soccer', 'Softball', 'Volleyball',
           'Ultimate Frisbee', 'Water Polo']
           
    for s in sports:
        sport.remove(s)
        
    form = SQLFORM.factory(
                           Field('image', 'upload', uploadfolder=os.path.join(request.folder,'uploads/')),
                           Field('name', 'string', requires=IS_NOT_EMPTY()),
                           Field('sport', requires=IS_IN_SET(sport)),
                           table_name='teams'
                          )
    if form.process().accepted:
        db.teams.insert(image = form.vars.image, name = form.vars.name,
                        sport = form.vars.sport, number_of_players = 1)
        db.commit()
        team = db(db.teams.name == form.vars.name).select().first()
        db.team_players.insert(team = team, player = auth.user_id)
        db.commit()        
        redirect(URL('my_teams'))
    elif form.errors:
        response.flash = 'Fix the errors please'
    return dict(form=form)

@auth.requires_login()
def my_teams():
	# grab all the teams that are associated with the user
    teams = db(db.team_players.player == auth.user_id).select()
    return dict(teams=teams)

def add_leader_validation(form):
    leader2 = form.vars.leader_2
    leader3 = form.vars.leader_3
    if leader2 == leader3:
        form.errors.leader_3 = 'cannot be the same as leader 2'
		
				
@auth.requires_login()
def add_leader():
    team = db.teams(request.args[0]) or redirect('index')
    team_players = db(db.team_players.team == team.id).select()
    players=[]
    for player in team_players:
        if (player.player.id != team.team_leader_1.id):
            players.append(player.player.email)

    # Creating the forms based on how many team leaders are already there    
    if team.team_leader_2==None and team.team_leader_3==None:
        form = SQLFORM.factory(Field('leader_2', requires=IS_EMPTY_OR(IS_IN_SET(players))),
                               Field('leader_3', requires=IS_EMPTY_OR(IS_IN_SET(players))))        
    elif team.team_leader_2==None:
        form = SQLFORM.factory(Field('leader_2', requires=IS_EMPTY_OR(IS_IN_SET(players))))        
    else:
        form = SQLFORM.factory(Field('leader_3', requires=IS_EMPTY_OR(IS_IN_SET(players))))
        
    # If form processed then add the invitation to the invites table        
    if form.process(onvalidation=add_leader_validation).accepted:
        message = 'Your invite was sent.'
        flag_for_leader_2 = False
        flag_for_leader_3 = False
        
        # Fetch all the invites that this team leader has already sent
        # to check for any duplicate invites
        sent_invites = db(db.team_leader_invites.sender == auth.user_id).select()
        
        if form.vars.leader_2 != None:
            leader2 = db(db.auth_user.email == form.vars.leader_2).select().first()
            # check for any duplicate invite
            for invite in sent_invites:
                if invite.receiver.id == leader2.id and invite.team.id == team.id:
                    flag_for_leader_2 = True
                    message = 'You have already sent a request to this person.' 
                    break
            if flag_for_leader_2 == False:
                db.team_leader_invites.insert(sender=auth.user_id, receiver=leader2.id, team=team.id)
                db.commit()
            #team.update_record(team_leader_2 = leader2.id)            
        if form.vars.leader_3 != None:
            leader3 = db(db.auth_user.email == form.vars.leader_3).select().first()
            # check for any duplicate invite
            for invite in sent_invites:
                if invite.receiver.id == leader3.id and invite.team.id == team.id:
                    flag_for_leader_3 = True
                    message = 'You have already sent a request to this person.'
                    break
            if flag_for_leader_3 == False:
                db.team_leader_invites.insert(sender=auth.user_id, receiver=leader3.id, team=team.id)
                db.commit()
        session.flash = message
        redirect(URL('my_teams'))       
    elif form.errors:
        response.flash = 'form has errors'            
    
    if team.team_leader_1 == auth.user_id:        
        return dict(team=team, form=form)
    else:
        response.flash = 'You do not have the right permissions'
        redirect(URL('my_teams'))
    
@auth.requires_login()    
def delete_leader():
    team = db.teams(request.args[0]) or redirect('index')
    leader = request.args[1] or redirect('index')
    
    if ((team.team_leader_1.id == auth.user_id) or
       (team.team_leader_2.id == auth.user_id) or
       (team.team_leader_3.id == auth.user_id)):
        if leader == 'aWaX22xzzA2':
            team.update_record(team_leader_2 = None)
            redirect(URL('team', args=[team.id]))
        elif leader == 'aWaX33xzzA3':
            team.update_record(team_leader_3 = None)
            redirect(URL('team', args=[team.id]))
        else:
            response.flash = 'Bad argument passed, try again!'
            redirect(URL('my_teams'))
    else:
        response.flash = 'You do not have the right permissions'
        redirect(URL('my_teams'))
    
        
###############################   Staff sign up options ################################

def staff_signup():
    form = SQLFORM.factory(
        Field('first_name', 'string', length=64, requires=IS_NOT_EMPTY()),
        Field('last_name', 'string', length=64, requires=IS_NOT_EMPTY()),
        Field('email', requires = [IS_EMAIL(forced='^.*\ucsc.edu(|\..*)$', error_message='Please enter your @ucsc.edu email.'),
                                    IS_NOT_IN_DB(db, db.auth_user.email, error_message='Error: email already in database.') ]),
        Field('password','password', requires=IS_NOT_EMPTY()),
        Field('password_again', 'password',
              requires=IS_EQUAL_TO(request.vars.password)),
        )
    if form.process().accepted:
        response.flash = 'form accepted'
        session.first_name = form.vars.first_name
        session.last_name = form.vars.last_name
        session.email = form.vars.email
        session.password = form.vars.password
        redirect(URL('staff_output'))
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

def staff_output(): 
    db.auth_user.insert(first_name = session.first_name,
        last_name=session.last_name, email=session.email, password = db.auth_user.password.validate(session.password)[0], staff=True)
    response.flash = 'new staff complete!'
    redirect(URL('index'))
    return dict(session=session)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())


#################### Search For Players ####################
def search_for_players():
    this_team = db.teams(request.args[0]) or redirect(URL('my_teams'))
    players = db().select(db.team_players.ALL)
    athletes = db(db.auth_user.sport == this_team.sport).select()
    player_ids=[]
    for athlete in athletes:
        player_ids.append(int(athlete.id))
        
    for player in players:
        if player.player.id in player_ids:
            player_ids.remove(player.player.id)
    
    return dict(player_ids=player_ids, team_id=this_team.id, sport=this_team.sport)

#################### Team View Controller ####################
@auth.requires_login()
def team():
    message = 'request sent'
    flag = False
    invites = None
    test='kos'
    team = db.teams(request.args[0]) or redirect(URL('index'))
    team_players = db(db.team_players.team == team).select()
    for player in team_players:
        if auth.user_id == player.player.id:
            flag = True
            break    
    form=FORM(INPUT(_type='submit', _value='request to join'))
    temp = None
    if form.process().accepted:
        temp = db(db.player_asking_teams.sender==auth.user_id and db.player_asking_teams.receiver ==team.id).select()
        count = 0;
        for row in temp:
            count = count + 1
        if (count==0):
            db.player_asking_teams.insert(
                sender = auth.user_id,
                receiver = team.id
            )
        session.flash = message
        
    
    if ((auth.user_id == team.team_leader_1) or 
        (auth.user_id == team.team_leader_2) or
        (auth.user_id == team.team_leader_3)):
       invites = db((db.player_asking_teams.receiver == team.id) &
                    (db.player_asking_teams.pending == True)).select(db.player_asking_teams.ALL)
    
    return dict(team=team, form=form, invites=invites, team_players=team_players, flag=flag, test=test, temp=temp)

#################### Team Search ####################
@auth.requires_login()
def team_search():
    players_teams = db(db.team_players.player == auth.user_id).select()
    sports=[]
    for team in players_teams:
        sports.append(team.team.sport)
        
    sport=['Basketball', 'Dodgeball', 'Flag Football',
           'Indoor Soccer', 'Soccer', 'Softball', 'Volleyball',
           'Ultimate Frisbee', 'Water Polo']
           
    for s in sports:
        sport.remove(s)
        
    form=FORM(LABEL('Please Select a Sport'), BR(),
        SELECT(sport, _name='sport'), BR(),
        INPUT(_type='submit')
        )
    if form.process().accepted:
        session.search_sport = request.vars.sport
        redirect(URL('team_search_result'))
    return dict(form=form)

#################### Team Search Result ####################
@auth.requires_login()
def team_search_result():
    teams = db(db.teams.number_of_players < 5 and db.teams.sport == session.search_sport).select(db.teams.ALL)
    users_teams = db(db.team_players.player == auth.user_id).select()
    
    a=[]
    for team1 in teams:
        for team2 in users_teams:
            if team1.id == team2.team.id:
                a.append(int(team1.id))
    return dict(teams=teams, sport=session.search_sport, users_teams=users_teams, a=a)

#################### Delete Team ####################
def delete_team():
    team = db.teams(request.args[0]) or redirect(URL('my_teams'))
    form = SQLFORM.factory(Field('confirm_deletion', 'boolean', default=False))
    if form.process().accepted:
        if form.vars.confirm_deletion == True:
            db(db.teams.id == request.args[0]).delete()
            db.commit()
            redirect(URL('my_teams'))
        else:
            redirect(URL('my_teams'))
    return dict(form=form, team=team)



#################### Debug User Info ####################
def user_debug_information():
    user = None
    if (auth.is_logged_in()):
        user = auth.user
    return dict(user=user)
    
@auth.requires_login()
def delete_profile():
    deleteform = SQLFORM.factory(Field('confirm_deletion', 'boolean', default=False))
    if deleteform.process().accepted:
        if deleteform.vars.confirm_deletion == True:
            db(db.auth_user.id == auth.user_id).delete()
            db.commit()
            auth.logout()
        else:
            redirect(URL('index'))
    return dict(user=auth.user, deleteform=deleteform)
