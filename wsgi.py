#!/bin/env python
"""
This script runs the librario application using a development server.
"""

import os

from librario import app as application
from librario import db
from librario.views import main

application.register_blueprint(main)
db.create_all()
if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "8888"))
    except ValueError:
        PORT = 8888
    application.run(HOST, PORT, threaded=True)
