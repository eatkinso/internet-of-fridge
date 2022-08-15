from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from iof.auth import login_required
from iof.db import get_db

bp = Blueprint('iof', __name__)


@bp.route('/add_item')
def add_item():
    return render_template('iof_pages/add-item.html')


@bp.route('/view_inv')
def view_inventories():
    return render_template('iof_pages/view_inv.html')

@bp.route('/iofhome')
def iof_home():
    return render_template('iof_pages/index.html')

@bp.route('/newitem')
def new_item():
    if request.method == 'POST':
        title = request.form['Name']
        body = request.form['upc']
        error = None
    if not title:
            error = 'Title is required.'
    if error is not None:
            flash(error)

    else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))        
    return render_template('iof_pages/add_item.html')