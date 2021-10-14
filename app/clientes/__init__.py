from flask import Blueprint

main = Blueprint("main",__name__)

from . import router
from . import config