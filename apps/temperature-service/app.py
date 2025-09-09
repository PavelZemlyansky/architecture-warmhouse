#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, abort
import random
app = Flask(__name__)
 
@app.route('/temperature')
def getTemperature():
    location=request.args.get('location')
    if location != None:
        return "{\"device_id\": \"53302a65-b54a-4058-89df-d56dc522aa86\", \"value\":" + str(random.randint(15, 35)) + "}"
    else:
        abort(404)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8081)