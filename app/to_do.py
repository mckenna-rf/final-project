from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from app.auth import login_required # the decorator to ensure login
from app.db import get_db

# group together related parts of the app
bp = Blueprint("to-do", __name__)