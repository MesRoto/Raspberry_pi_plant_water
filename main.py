import numpy as np
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
from waterer import Watererer

if __name__ == "__main__":
    water = Watererer
    water.start()
