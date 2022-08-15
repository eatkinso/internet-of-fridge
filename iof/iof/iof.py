from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from iof.auth import login_required
from iof.db import get_db

bp = Blueprint('iof', __name__)


## Adding a link to Fridgeview
@bp.route('/fridgeview')
def fridgeview():
    return render_template('iof-pages/fridgeview.html')

@bp.route('/add_item')
def add_item():
    return render_template('iof-pages/add-item.html')