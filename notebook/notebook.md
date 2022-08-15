#  8/14/22 Working through Flask Tutorial

Starting with [this tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/) from the Flask documentation; this is in the `tutorial` folder. This also includes making a python venv as described [here](https://flask.palletsprojects.com/en/2.2.x/installation/). 


## Modifying SQL database 

Pretty straightforward. Now trying to modify this to fit the fridge application. First -- modifying the SQLite database. I think the first goal will be to just manually add stuff (so the website prompts the user to type a UPC code) and display the current fridge contents at the home page. And also use the authorization to allow certain people to add contents to the fridge.

Generally planning to use [this UPC lookup API](https://www.ean-search.org/ean-database-api.html). 


Thoughts on structure -- there will be a table that collects all of the UPC codes that have been scanned, and then the "fridge" page displays a result of a query that gets every item that is currently *present*. So when an item is scanned, it is first compared to the global-items table to determine if we locally know what it is, before using the UPC lookup api to find it online. 

Also on the home page: sort by location (fridge, bathroom, laundry, kitchen, pantry) and things like food type (dairy, veg, nonperishables).



- Added iof-pages with html templates for iof pages
- Added iof.py to create blueprints for the iof pages


Adapting the boilerplate blog post code (below) to use the python API to look up UPC codes and add them to the database.

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

