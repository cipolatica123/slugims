# coding: utf8

from datetime import datetime

db.define_table('team_inviting_players',                
                Field('sender', 'reference teams'),
                Field('receiver', 'reference auth_user'),                
                Field('date_sent', 'datetime', default=datetime.utcnow()),
                Field('pending', 'boolean', default=True),
               )

db.define_table('player_asking_teams',                
                Field('sender', 'reference auth_user'),
                Field('receiver', 'reference teams'),                
                Field('date_sent', 'datetime', default=datetime.utcnow()),
                Field('pending', 'boolean', default=True),
               )


db.define_table('team_leader_invites',                
                Field('sender', 'reference auth_user'),
                Field('receiver', 'reference auth_user'),
                Field('team', 'reference teams'),            
                Field('date_sent', 'datetime', default=datetime.utcnow()),
                Field('pending', 'boolean', default=True),
               )
