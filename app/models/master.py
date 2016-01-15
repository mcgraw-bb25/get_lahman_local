#!/usr/bin/python
'''
from ../app 
    $ python -m models.master --load_csv Master.csv
'''
import argparse
import csv
import os
fileprefix = os.getcwd()[:os.getcwd().find("app")] + "lahman_data/"

# from sqlalchemy import *
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from data_config import DATABASE_URI

#### DEFINE Master() for initial CREATE
# creating from scratch, do not require args
metadata = MetaData()

#### AUTOLOAD Master() for use ####
# for autoloading Master, requires active engine
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base(engine)


class Master(Base):
    __tablename__ = "master"
    __table_args__ = {'autoload': True}

    def __repr__(self):
        return "<Player(Name: %s %s ID: %s Year Born: %s)>" % (
                        self.name_first, 
                        self.name_last, 
                        self.player_id, 
                        self.birth_year)


# for loading Master data with autoload, engine and Base declared
def load_session_for_usage():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--load_csv", type=str, 
                help="Type filename to read")

    args = parser.parse_args()

    if args.load_csv:
        session = load_session_for_usage()
        try:
            csv_file_name = fileprefix + args.load_csv
            with open(csv_file_name, newline='') as csv_file:
                datareader = csv.reader(csv_file, delimiter=',', quotechar='"')
                line = 0
                for row in datareader:
                    # Add new object to record
                    if line != 0:
                        record = Master(
                            player_id = row[0],
                            birth_year = row[1],
                            birth_month = row[2],
                            birth_day = row[3],
                            birth_country = row[4],
                            birth_state = row[5],
                            birth_city = row[6],
                            death_year = row[7],
                            death_month = row[8],
                            death_day = row[9],
                            death_country = row[10],
                            death_state = row[11],
                            death_city = row[12],
                            name_first = row[13],
                            name_last = row[14],
                            name_given = row[15],
                            weight = row[16],
                            height = row[17],
                            bats = row[18],
                            throws = row[19],
                            debut = row[20],
                            final_game = row[21],
                            retro_id = row[22],
                            bbref_id = row[23],
                            )
                        session.add(record)
                    line = line + 1
                session.commit()
        except FileNotFoundError:
            print ("That file doesn't exist! Please check input.")
