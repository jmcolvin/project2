#!/usr/bin/python3

import os
import bottle
from app import app


if __name__ == "__main__":
    bottle.run(reloader=True, debug=True, port=5002)
