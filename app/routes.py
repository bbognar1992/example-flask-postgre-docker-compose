from datetime import datetime as dt

from flask import current_app as app, make_response
from flask_table import Table, Col

from app.models.my_table import MyTable
from . import db


# Declare my table
class ItemTable(Table):
    id = Col('id')
    r_value = Col('r_value')
    ts_created = Col('ts_created')


@app.route('/generate/', methods=['GET'])
def generate():
    # generate random integer values
    from random import seed
    from random import randint
    # seed random number generator
    seed(1)

    """Generate records"""
    for i in range(0, 300):
        # generate integer
        random_integer = randint(1000, 9999)
        # create new record
        rew_row = MyTable(r_value=random_integer, ts_created=dt.now())
        # add new record to database
        db.session.add(rew_row)

    # Commits all changes
    db.session.commit()

    return make_response(f"successfully created!")


@app.route('/show_records/', methods=['GET'])
def show():
    """get records with r_value above 9000"""
    items = MyTable.query.filter(MyTable.r_value > 9000).all()

    # Populate the table
    table = ItemTable(items)

    return make_response(f"{table.__html__()}")
