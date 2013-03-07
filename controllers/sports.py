# coding: utf8

def index():
    redirect(URL('basketball'))
    
#################### Validation for adding a new schedule ####################

def schedule_validation(form):
    team1 = form.vars.team_1
    team2 = form.vars.team_2
    winner = form.vars.winner
    date = form.vars.date
    if team1 == team2:
        form.errors.team_2 = 'teams can not be the same'
    if date == None:
        form.errors.date = 'please select date'
   # if winner!= team1 and winner != team2:
    #    form.errors.winner = 'winner must be team1 or team2'

#################### Get the sidebar Schedules ####################
def get_schedules():
    basketball = dodgeball = flag_football = indoor_soccer = soccer = softball = ultimate_frisbee = None
    volleyball = water_polo = None
    
    bball = db(db.basketball.winner == None).select(orderby=db.basketball.date).first()
    if bball:
        basketball=[bball.team_1.name, bball.team_2.name, bball.date.strftime("%a, %b %d"),
                    bball.date.strftime("%I:%M %p")]
                    
    dball = db(db.dodgeball.winner == None).select(orderby=db.dodgeball.date).first()
    if dball:
        dodgeball=[dball.team_1.name, dball.team_2.name, dball.date.strftime("%a, %b %d"),
                    dball.date.strftime("%I:%M %p")]
                    
    football = db(db.flag_football.winner == None).select(orderby=db.flag_football.date).first()
    if football:
        flag_football=[football.team_1.name, football.team_2.name, football.date.strftime("%a, %b %d"),
                        football.date.strftime("%I:%M %p")]
                    
    i_soccer = db(db.indoor_soccer.winner == None).select(orderby=db.indoor_soccer.date).first()
    if i_soccer:
        indoor_soccer=[i_soccer.team_1.name, i_soccer.team_2.name, i_soccer.date.strftime("%a, %b %d"),
                        i_soccer.date.strftime("%I:%M %p")]
    
    sc = db(db.soccer.winner == None).select(orderby=db.soccer.date).first()  
    if sc:
        soccer=[sc.team_1.name, sc.team_2.name, sc.date.strftime("%a, %b %d"),
                        sc.date.strftime("%I:%M %p")]
                        
    sball = db(db.softball.winner == None).select(orderby=db.softball.date).first()
    if sball:
        softball=[sball.team_1.name, sball.team_2.name, sball.date.strftime("%a, %b %d"),
                    sball.date.strftime("%I:%M %p")]
                    
    uf = db(db.ultimate_frisbee.winner == None).select(orderby=db.ultimate_frisbee.date).first()
    if uf:
        ultimate_frisbee=[uf.team_1.name, uf.team_2.name, uf.date.strftime("%a, %b %d"),
                    uf.date.strftime("%I:%M %p")]
                    
    vball = db(db.volleyball.winner == None).select(orderby=db.volleyball.date).first()
    if vball:
        volleyball=[vball.team_1.name, vball.team_2.name, vball.date.strftime("%a, %b %d"),
                    vball.date.strftime("%I:%M %p")]
                    
    wp = db(db.water_polo.winner == None).select(orderby=db.water_polo.date).first()
    if wp:
        water_polo=[wp.team_1.name, wp.team_2.name, wp.date.strftime("%a, %b %d"),
                    wp.date.strftime("%I:%M %p")]
    
    return dict(basketball=basketball, dodgeball=dodgeball, flag_football=flag_football, indoor_soccer=indoor_soccer, soccer=soccer,
                softball=softball, ultimate_frisbee=ultimate_frisbee, volleyball=volleyball, water_polo=water_polo)

#################### Sports Views ####################

def basketball():
    schedules = db().select(db.basketball.ALL, orderby=db.basketball.date)       
    
    staff_is_logged_in = False
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True
    
    return dict(message=T('Basketball'), staff=staff_is_logged_in, schedules=schedules)


def dodgeball():
    schedules = db().select(db.dodgeball.ALL, orderby=db.dodgeball.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Dodgeball'), staff=staff_is_logged_in, schedules=schedules)


def flag_football():
    schedules = db().select(db.flag_football.ALL, orderby=db.flag_football.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Flag Football'), staff=staff_is_logged_in, schedules=schedules)


def indoor_soccer():
    schedules = db().select(db.indoor_soccer.ALL, orderby=db.indoor_soccer.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Indoor Soccer'), staff=staff_is_logged_in, schedules=schedules)


def soccer():
    schedules = db().select(db.soccer.ALL, orderby=db.soccer.date)
    
   
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Soccer'), staff=staff_is_logged_in, schedules=schedules)


def softball():
    schedules = db().select(db.softball.ALL, orderby=db.softball.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Softball'), staff=staff_is_logged_in, schedules=schedules)


def volleyball():
    schedules = db().select(db.volleyball.ALL, orderby=db.volleyball.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Volleyball'), staff=staff_is_logged_in, schedules=schedules)


def ultimate_frisbee():
    schedules = db().select(db.ultimate_frisbee.ALL, orderby=db.ultimate_frisbee.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Ultimate Frisbee'), staff=staff_is_logged_in, schedules=schedules)


def water_polo():
    schedules = db().select(db.water_polo.ALL, orderby=db.water_polo.date)
    
    staff_is_logged_in = False;
    if auth.user:
        if auth.user.staff:
            staff_is_logged_in = True;
    return dict(message=T('Water Polo'), staff=staff_is_logged_in, schedules=schedules)


###################### Edit Game Pages ######################
def basketball_edit():
    this_schedule = db.basketball(request.args(0, cast=int)) or redirect(URL('basketball'))

    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('basketball'))
    return dict(form=form)

def dodgeball_edit():
    this_schedule = db.dodgeball(request.args(0, cast=int)) or redirect(URL('dodgeball'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('dodgeball'))
    return dict(form=form)
    
def flag_football_edit():
    this_schedule = db.flag_football(request.args(0, cast=int)) or redirect(URL('flag_football'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('flag_football'))
    return dict(form=form)
	
def indoor_soccer_edit():
    this_schedule = db.indoor_soccer(request.args(0, cast=int)) or redirect(URL('indoor_soccer'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('indoor_soccer'))
    return dict(form=form)
    
def soccer_edit():
    this_schedule = db.soccer(request.args(0, cast=int)) or redirect(URL('soccer'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('soccer'))
    return dict(form=form)
    
    
def softball_edit():
    this_schedule = db.softball(request.args(0, cast=int)) or redirect(URL('softball'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('softball'))
    return dict(form=form)
    
    
def volleyball_edit():
    this_schedule = db.volleyball(request.args(0, cast=int)) or redirect(URL('volleyball'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('volleyball'))
    return dict(form=form)
    
    
def ultimate_frisbee_edit():
    this_schedule = db.ultimate_frisbee(request.args(0, cast=int)) or redirect(URL('ultimate_frisbee'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('ultimate_frisbee'))
    return dict(form=form)

def water_polo_edit():
    this_schedule = db.water_polo(request.args(0, cast=int)) or redirect(URL('water_polo'))
    form = SQLFORM.factory(               
                Field('winner', requires=IS_IN_SET([this_schedule.team_1.name, this_schedule.team_2.name])),
                Field('score', required=True),
                )
    if form.process().accepted:
        winner = db(db.teams.name == form.vars.winner).select().first()
        this_schedule.update_record(winner=winner.id, score=form.vars.score)
        db.commit()
        redirect(URL('water_polo'))
    return dict(form=form)

###################### Add Game Pages ######################
def get_team_names(sport):
    teams = []
    teams_from_db = db(db.teams.sport == sport).select(orderby=db.teams.name)
    for team in teams_from_db:
        teams.append(team.name)
        
    return teams



def basketball_addgame():    
    teams = get_team_names('Basketball')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.basketball.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('basketball'))
    return dict(form=form)

def dodgeball_addgame():
    teams = get_team_names('Dodgeball')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.dodgeball.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('dodgeball'))
    return dict(form=form)
	
def flag_football_addgame():
    teams = get_team_names('Flag Football')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.flag_football.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('flag_football'))
    return dict(form=form)
    
def indoor_soccer_addgame():
    teams = get_team_names('Indoor Soccer')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.indoor_soccer.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('indoor_soccer'))
    return dict(form=form)
    
def soccer_addgame():
    teams = get_team_names('Soccer')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.soccer.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('soccer'))
    return dict(form=form)
    
def softball_addgame():
    teams = get_team_names('Softball')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.softball.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('softball'))
    return dict(form=form)

def volleyball_addgame():
    teams = get_team_names('Volleyball')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.volleyball.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('volleyball'))
    return dict(form=form)
                
def ultimate_frisbee_addgame():
    teams = get_team_names('Ultimate Frisbee')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.ultimate_frisbee.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('ultimate_frisbee'))
    return dict(form=form)
                
def water_polo_addgame():
    teams = get_team_names('Water Polo')
    
    form = SQLFORM.factory(
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', requires=IS_IN_SET(teams), required=True),
                Field('team_2', requires=IS_IN_SET(teams), required=True),
                )
    if form.process(onvalidation=schedule_validation).accepted:
        team_1 = db(db.teams.name == form.vars.team_1).select().first()
        team_2 = db(db.teams.name == form.vars.team_2).select().first()
        db.water_polo.insert(date = form.vars.date,
                             team_1 = team_1.id,
                             team_2 = team_2.id,
                             )
        db.commit()
        redirect(URL('water_polo'))
    return dict(form=form)
