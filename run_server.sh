#! /bin/bash

HOST=0.0.0.0
PORT=8000

export FLASK_APP=app
rm -rf app.egg-info
pip install -e .

flask run -h ${HOST} -p ${PORT} --with-threads --reload --debugger