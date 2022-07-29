from app import app, elevator, minfloor, maxfloor
from flask import render_template, request, redirect, url_for, make_response
from time import sleep
import os

@app.route("/", methods=['GET', 'POST'])
def outside():
    if request.cookies.get('userID') is None:
        userId = os.urandom(12).hex()
        resp = make_response(render_template("outside.html", elevator=elevator, min=minfloor, max=maxfloor, userId=userId))
        resp.set_cookie('userID', userId)
    else:
        resp = make_response(render_template("outside.html", elevator=elevator, min=minfloor, max=maxfloor, userId=request.cookies.get('userID')))
    return resp

@app.route("/gettheelevator", methods=['GET', 'POST'])
def gettheelevator():
    if request.args['clientfloor'] != "choose":
        target_floor = int(request.args['clientfloor'])
    else:
        return redirect(url_for("outside"))
    depart = (request.cookies.get('userID'), target_floor)
    if depart not in elevator.departs:
        elevator.departs.append(depart)
    if target_floor != elevator.currentfloor:
        if depart[0] == elevator.departs[0][0]:
            sleep(2)
            if target_floor > elevator.currentfloor:
                elevator.goUp()
            else:
                elevator.goDown()
        return render_template("outside.html", elevator=elevator, min=minfloor, max=maxfloor, clientfloor=target_floor,
                               userId=request.cookies.get('userID')), {
                   "Refresh": "1; url=" + url_for('gettheelevator') + "?userId=" + elevator.departs[0][
                       0] + "&clientfloor=" + str(target_floor)}
    else:
        return redirect(url_for('inside'))
