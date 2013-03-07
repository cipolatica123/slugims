# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

def user_bar():
    if auth.user and not auth.user.staff :
        logout=A('Logout', _href=URL('default', 'user/logout'))
        profile=A('Profile', _href=URL('default', 'profile'))
        team_search=A('Search for Teams', _href=URL('default', 'team_search'))
    	team_signup=A('Team Signup', _href=URL('default', 'team_signup'))
    	my_teams=A('My Teams', _href=URL('default', 'my_teams'))
        bar = UL(LI(auth.user.email), LI(profile), LI(my_teams), LI(team_signup), LI(team_search), LI(logout), _class='auth_navbar')
    elif auth.user and auth.user.staff:
        logout=A('Logout', _href=URL('default', 'user/logout'))
        bar = UL(LI(auth.user.email), LI(logout), _class='auth_navbar')
    else:
        login=A('Login', _href=URL('default', 'user/login'))
        register=A('Register',_href=URL('default', 'user/register'))
        staff=A(T("Staff Signup"),  _href=URL('default', 'staff_signup'))
        bar = UL(LI(login), LI(register), LI(staff), _class='auth_navbar')
    return bar
    
response.user_bar = user_bar()

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Bardia Keyouamrsi, Alberto Plata, Vincent Lantaca'
response.meta.description = 'UCSC Intramurals Website'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('Basketball'), False, URL('sports','basketball'), []),
    (T('Dodgeball'), False, URL('sports','dodgeball'), []),
    (T('Flag Football'), False, URL('sports','flag_football'), []),
    (T('Indoor Soccer'), False, URL('sports','indoor_soccer'), []),
    (T('Soccer'), False, URL('sports','soccer'), []),
    (T('Softball'), False, URL('sports','softball'), []),
    (T('VOlleyball'), False, URL('sports','volleyball'), []),
    (T('Ultimate Frisbee'), False, URL('sports','ultimate_frisbee'), []),
    (T('Water Polo'), False, URL('sports','water_polo'), []),    
    ]
