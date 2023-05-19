import sqlalchemy as db

engine = db.create_engine('sqlite:///database.db')       # pick lang:///file.name

connection = engine.connect()

metadata = db.MetaData()        # something like a dictionary

#   -   Create table in engine (path)

teleinfo = db.Table('teleinfo', metadata,
                    db.Column('chat_id', db.Integer, primary_key=True),
                    db.Column('msg_from_id', db.Integer),
                    db.Column('msg_to_id', db.Integer)
                    )

metadata.create_all(engine)