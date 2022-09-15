import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__= 'user'
    id= Column(Integer, primary_key=True)
    email=Column(String(250))
    username=Column(String(250), nullable=False)
    password=Column(String(250), nullable=False)


class favourite(Base):
    __tablename__= 'favourite'
    id= Column(Integer, primary_key=True)
    user_id= (Integer, ForeignKey('user.id'))
    character_id= (Integer, ForeignKey('character.id'))
    planet_id= (Integer, ForeignKey('planet.id'))
    vehicle_id= (Integer, ForeignKey('vehicle.id'))


class character(Base):
    __tablename__= 'character'
    id= Column(Integer, primary_key=True)
    name= Column(String(250))
    height= Column(Integer)
    mass= Column(Integer)
    hair_color= Column(String(250))
    skin_color= Column(String(250))
    eye_color= Column(String(250))
    gender= Column(String(250))
    birth_year= Column(String(250))
    homeworld= Column(Integer, ForeignKey('planet.planet_id'))


class planet(Base):
    __tablename__= 'planet'
    id= Column(Integer, primary_key=True)
    name= Column(String(250))
    diameter= Column(Integer)
    rotation_period= Column(Integer)
    orbital_period= Column(Integer)
    gravity= Column(String(250))
    population= Column(Integer)
    climate= Column(String(250))
    terrain= Column(String(250))
    surface_water= Column(Integer)


class vehicle(Base):
    __tablename__= 'vehicle'
    id= Column(Integer, primary_key=True)
    name= Column(String(250))
    model=Column(String(250))
    vehicle_class= Column(String(250))
    manufacturer= Column(String(250))
    cost_in_credits= Column(Integer)
    length= Column(Integer)
    crew= Column(Integer)
    passengers= Column(Integer)
    max_atmosphering_speed= Column(Integer)
    cargo_capacity= Column(Integer)
    consumables= Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')