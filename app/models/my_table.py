from app import db


class MyTable(db.Model):
    """Model for My Table."""

    __tablename__ = 'my_table'

    id = db.Column(db.BigInteger,
                   primary_key=True)
    ts_created = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=False)
    r_value = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)

    def __repr__(self):
        return '<MyTable %r>' % self.r_value
