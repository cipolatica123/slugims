# coding: utf8

from datetime import datetime

####################   Teams related databases ##########################

db.define_table('teams',
                Field('image', 'upload'),
                Field('name', 'string', required=True, length=100),
                Field('team_leader_1', db.auth_user, default=auth.user_id, readable=False, writable=False),
                Field('team_leader_2', db.auth_user, readable=False, writable=False, required=False),
                Field('team_leader_3', db.auth_user, readable=False, writable=False, required=False),
                Field('sport', requires=IS_IN_SET(['Basketball', 'Dodgeball', 'Flag Football',
                      'Indoor Soccer', 'Soccer', 'Softball', 'Volleyball', 'Ultimate Frisbee', 'Water Polo'])),
                Field('championship', readable=False, writable=False),
                Field('date_created', 'datetime', default=datetime.utcnow()), 
                Field('number_of_players', 'integer', default=0, requires=IS_INT_IN_RANGE(0, 20), readable = False, writable=False),
                format='%(name)s'
                )

db.teams.date_created.writable = db.teams.date_created.readable = False
db.teams.name.requires = IS_NOT_IN_DB(db, 'teams.name')

db.define_table('team_players',
                Field('team', 'reference teams'),
                Field('player', 'reference auth_user'),
               )
               
"""db.define_table('basketball_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('dodgeball_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
  
db.define_table('flag_football_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('indoor_soccer_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('soccer_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('softball_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('volleyball_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('ultimate_frisbee_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )
               
db.define_table('water_polo_sport',
                Field('team', 'reference teams'),
                Field('team_name', 'string'),
               )"""
