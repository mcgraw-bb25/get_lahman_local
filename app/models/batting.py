#!/usr/bin/python
'''
from ../app
    $ python -m models.batting --load_csv Batting.csv
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


class Batting(Base):
    __tablename__ = "batting"
    __table_args__ = {'autoload': True}

    def __repr__(self):
        return "Batting(Player ID: %s Year: %s Team: %s AB: %s)>" % (
                        self.player_id, 
                        self.year_id, 
                        self.team_id, 
                        self.AB)


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
                    # Add new object data to record
                    if line != 0:
                        record = Batting(
                            player_id =  row[0],
                            year_id =  row[1],
                            stint =  row[2],
                            team_id =  row[3],
                            lg_id =  row[4],
                            _G =  row[5],
                            _AB =  row[6],
                            _R =  row[7],
                            _H =  row[8],
                            _2B =  row[9],
                            _3B =  row[10],
                            _HR =  row[11],
                            _RBI =  row[12],
                            _SB =  row[13],
                            _CS =  row[14],
                            _BB =  row[15],
                            _SO =  row[16],
                            _IBB =  row[17],
                            _HBP =  row[18],
                            _SH =  row[19],
                            _SF =  row[20],
                            _GIDP =  row[21],
                            )
                        session.add(record)
                    line = line + 1
                session.commit()
        except FileNotFoundError:
            print ("That file doesn't exist! Please check input.")
