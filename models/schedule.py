# coding: utf8

from datetime import datetime

db.define_table('basketball',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
db.define_table('dodgeball',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('flag_football',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('indoor_soccer',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('soccer',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('softball',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('volleyball',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('ultimate_frisbee',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
                
db.define_table('water_polo',
                Field('date', 'datetime', widget=SQLFORM.widgets.datetime.widget, required=True),      
                Field('team_1', 'reference teams', required=True),
                Field('team_2', 'reference teams', required=True),
                Field('winner', 'reference teams'),
                Field('score', required=False),
                )
