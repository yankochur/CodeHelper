import sqlalchemy as db


#####   CONNECTION


engine = db.create_engine('sqlite:///database.db')       # pick lang:///file.name

connection = engine.connect()

metadata = db.MetaData()        # something like a dictionary


#####   CREATE TABLE


teleinfo = db.Table('teleinfo', metadata,
                    db.Column('chat_id', db.Integer, primary_key=True),
                    db.Column('msg_from_id', db.Integer),
                    db.Column('msg_to_id', db.Integer),
                    db.Column('msg_text', db.Text)
                    )

# metadata.create_all(engine)         # create database


#####   ADD A NEW COLUMN


alter_table = db.text("ALTER TABLE teleinfo ADD COLUMN msg_text TEXT")    # create a new column (without sqlalchemy)
connection.execute(alter_table)



#####   INSERT TO DB


insertion_query = teleinfo.insert().values([
    {"chat_id":228322, "msg_from_id":228, "msg_to_id":322, "msg_text":"Здарова ублюдки"},
    {"chat_id":1337, "msg_from_id":17, "msg_to_id":57, "msg_text":None},
    {"chat_id":2021, "msg_from_id":1, "msg_to_id":0, "msg_text":None}
])

connection.execute(insertion_query)         # insert to database


#####   SELECTION IN DB


select_all_query = db.select(teleinfo)        # selection ALL from teleinfo
select_all_result = connection.execute(select_all_query)

print(select_all_result.fetchall())     # fetchall need for values

select_price_query = db.select(teleinfo).where(teleinfo.columns.chat_id == 2021)        # selection where...
select_price_result = connection.execute(select_price_query)

print(select_price_result.fetchall())


#####   UPDATE ITEMS


update_query = db.update(teleinfo).where(teleinfo.columns.chat_id == 1337).values(chat.id = 1338)       # idk, but red wavy line due to "chat.id = 1338" (==)
connection.execute(update_query)


#####   DELETE FROM DB


delete_query = db.delete(teleinfo)
connection.execute(delete_query)

connection.commit()     # always needed