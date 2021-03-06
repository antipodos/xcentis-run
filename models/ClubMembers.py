from sqlalchemy import Column, Integer, DateTime, String, Table, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from base import Base
import datetime

club_athletes_association = Table('club_athletes', Base.metadata,
                                  Column('club_id', Integer, ForeignKey('club.id')),
                                  Column('athlete_id', Integer, ForeignKey('athlete.id'))
)


class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    update_timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    athletes = relationship("Athlete", secondary=club_athletes_association)

    def __init__(self, id):
        self.id = id


class Athlete(Base):
    __tablename__ = 'athlete'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    update_timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    clubs = relationship("Club", secondary=club_athletes_association)

    stats = relationship("Stats")

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def set_update_timestamp(self):
        self.update_timestamp = datetime.datetime.utcnow()


class ChartRace(Base):
    __tablename__ = "chartrace"

    athlete_id = Column(Integer, ForeignKey('athlete.id'), primary_key=True)
    year = Column(Integer, primary_key=True)
    week = Column(Integer, primary_key=True)
    distance = Column(Float)

    def __init__(self, athlete_id, year, week, distance):
        self.athlete_id = athlete_id
        self.year = year
        self.week = week
        self.distance = distance

class ChartRaceCharts(Base):
    __tablename__ = "chartracechart"
    club_id = Column(Integer, ForeignKey('club.id'), primary_key=True)
    year = Column(Integer, primary_key=True)
    video_html = Column(Text)

    def __init__(self, club_id, year, video_html):
        self.club_id = club_id
        self.year = year
        self.video_html = video_html


class Stats(Base):
    __tablename__ = "stats"
    athlete_id = Column(Integer, ForeignKey('athlete.id'), primary_key=True)
    year = Column(Integer, primary_key=True)
    running_ytd_distance = Column(Float)

    def __init__(self, athlete_id, year, running_ytd_distance):
        self.athlete_id = athlete_id
        self.year = year
        self.running_ytd_distance = running_ytd_distance