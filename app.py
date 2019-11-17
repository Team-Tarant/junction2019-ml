import os
import json

from flask import Flask, send_from_directory, request

import model

app = Flask(__name__)
ml = model.Ml('model/nuuksio_paths.sav')


@app.route('/predict')
def predict():
    ts = int(request.args.get('timestamp'))
    counter_id = request.args.get('counterId', None)
    result = ml.predict(ts, counter_id)

    body = {'data': {'visitors': result}}

    result = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        'body': json.dumps(body),
    }

    return result
