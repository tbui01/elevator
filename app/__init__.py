from flask import Flask
from app.elevator import Elevator

app = Flask(__name__)
currentfloor = 1
minfloor = -2
maxfloor = 5
elevator = Elevator(currentfloor, minfloor, maxfloor)

from . import inside_elevator, outside_elevator
