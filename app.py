import os
import json
import math

from flask import Flask, send_from_directory, request

import model

app = Flask(__name__)
ml = model.Ml('model/nuuksio_paths.sav')


@app.route('/predict')
def predict():
    ts = int(request.args.get('timestamp'))
    counter_id = request.args.get('counterId', None)
    result = ml.predict(ts, counter_id)

    crowdedness = math.floor(max(min(6000, result), 600) / 600)

    result = {'visitors': math.floor(result), 'crowdedness': crowdedness}

    return result
