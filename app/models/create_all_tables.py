#!/usr/bin/python
import argparse

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from data_config import DATABASE_URI

#### DEFINE Master() for initial CREATE
# creating from scratch, do not require args
metadata = MetaData()
engine = create_engine(DATABASE_URI, echo=True)

master = Table("master", metadata,
    Column('id', Integer, primary_key=True),
    Column('player_id', String(), unique=True, nullable=False),
    Column('birth_year', Integer),
    Column('birth_month', Integer),
    Column('birth_day', Integer),
    Column('birth_country', String()),
    Column('birth_state', String()),
    Column('birth_city', String()),
    Column('death_year', Integer),
    Column('death_month', Integer),
    Column('death_day', Integer),
    Column('death_country', String()),
    Column('death_state', String()),
    Column('death_city', String()),
    Column('name_first', String()),
    Column('name_last', String()),
    Column('name_given', String()),
    Column('weight', Integer),
    Column('height', Integer),
    Column('bats', String()),
    Column('throws', String()),
    Column('debut', String()),
    Column('final_game', String()),
    Column('retro_id', String()),
    Column('bbref_id', String())
    )


if __name__ == "__main__":
    '''
    from ../app 
        $ python -m models.create_all_tables --create_tables Y
        $ python -m models.create_all_tables --drop_tables Y
    '''

    table_list = []

    ### append all tables to be added here
    table_list.append(master)

    ###
    parser = argparse.ArgumentParser()

    parser.add_argument("--create_tables", type=str, 
                help="Set to Y if you want to create the table")
    parser.add_argument("--drop_tables", type=str, 
                help="Set to Y if you want to create the table")

    args = parser.parse_args()

    if args.create_tables == "Y":
        for table in table_list:
            table.create(engine)

    if args.drop_tables == "Y":
        for table in table_list:
            table.drop(engine)
