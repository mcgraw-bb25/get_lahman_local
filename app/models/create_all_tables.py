#!/usr/bin/python
'''
from ../app 
    $ python -m models.create_all_tables --create_tables Y
    $ python -m models.create_all_tables --drop_tables Y
'''
import argparse

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

from data_config import DATABASE_URI

#### DEFINE Master() for initial CREATE
# creating from scratch, do not require args
metadata = MetaData()
engine = create_engine(DATABASE_URI, echo=True)

master = Table("master", metadata,
    Column('id', Integer, primary_key=True),
    Column('player_id', String(), unique=True,
                                  nullable=False),
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


batting = Table("batting", metadata,
    Column('id', Integer, primary_key=True),
    Column('player_id', String(), ForeignKey("master.player_id"),
                                 nullable=False),
    Column('year_id', Integer),
    Column('stint', Integer),
    Column('team_id', String()),
    Column('lg_id', String()),
    Column('_G', Integer),
    Column('_AB', Integer),
    Column('_R', Integer),
    Column('_H', Integer),
    Column('_2B', Integer),
    Column('_3B', Integer),
    Column('_HR', Integer),
    Column('_RBI', Integer),
    Column('_SB', Integer),
    Column('_CS', Integer),
    Column('_BB', Integer),
    Column('_SO', Integer),
    Column('_IBB', Integer),
    Column('_HBP', Integer),
    Column('_SH', Integer),
    Column('_SF', Integer),
    Column('_GIDP', Integer)
    )

if __name__ == "__main__":

    ### append all tables to be added here
    table_list = [
        master,
        batting,
    ]

    ###
    parser = argparse.ArgumentParser()

    parser.add_argument("--create_tables", type=str, 
                help="Set to Y if you want to create the table")
    parser.add_argument("--drop_tables", type=str, 
                help="Set to Y if you want to create the table")

    args = parser.parse_args()

    if args.create_tables == "Y":
        for table in table_list:
            table.create(engine, checkfirst=True)

    if args.drop_tables == "Y":
        for table in table_list:
            table.drop(engine)
