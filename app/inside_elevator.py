from app import app, elevator
from flask import render_template, request, redirect, url_for
from time import sleep

@app.route("/inside", methods=['GET', 'POST'])
def inside():
    return render_template("inside.html", elevator=elevator, userId=request.cookies.get('userID'))

@app.route("/movetheelevator", methods=['GET', 'POST'])
def movetheelevator():
    target_floor = int(request.args['target_floor'])
    destination = (request.cookies.get('userID'), target_floor)
    if destination not in elevator.destinations:
        elevator.destinations.append(destination)
    if target_floor != elevator.currentfloor:
        if request.cookies.get('userID') == elevator.destinations[0][0]:
            sleep(2)
            if target_floor > elevator.currentfloor:
                elevator.goUp()
            else:
                elevator.goDown()
        return render_template("inside.html", elevator=elevator, userId=request.cookies.get('userID')), {
            "Refresh": "1; url=" + url_for('movetheelevator') + "?userId="+request.cookies.get('userID') + "&target_floor=" + str(target_floor)}
    else:
        elevator.departs = [tup for tup in elevator.departs if tup[0] != destination[0]]
        elevator.destinations.remove(destination)
        return redirect(url_for('outside'))
