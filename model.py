"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)


db = SQLAlchemy()


class User(db.Model):
    """User of ratings website."""

    __tablename__ = "Users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    fname = db.Column(db.String(15), nullable=False)

    # @classmethod
    # def get_by_email(cls, email):
    #     """Query for a specific melon in the database by the primary key"""
    #      = db.session.query.filter(cls.email==email).first()




    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<user_id= %s email= %s fname = %s>" % (self.user_id, self.email, self.fname)


class Measurement_Chart(db.Model):
    """Measurement Charts for specific users."""
    
    __tablename__ = "Measurement_Charts"

    chart_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nickname = db.Column(db.Integer, nullable=False)
    pattern_url = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), db.ForeignKey('Users.user_id'))
    bust = db.Column(db.Integer, nullable=False)
    waist = db.Column(db.Integer, nullable=False)

    full_length = db.Column(db.Integer, nullable=False) 
    center_front = db.Column(db.Integer, nullable=False)
    front_shoulder_slope = db.Column(db.Integer, nullable=False)
    strap = db.Column(db.Integer, nullable=False)
    front_across_shoulder = db.Column(db.Integer, nullable=False)
    across_chest = db.Column(db.Integer, nullable=False)
    bust_depth = db.Column(db.Integer, nullable=False)
    shoulder_length = db.Column(db.Integer, nullable=False)
    bust_arc = db.Column(db.Integer, nullable=False)
    bust_span = db.Column(db.Integer, nullable=False)
    waist_arc = db.Column(db.Integer, nullable=False)
    dart_placement = db.Column(db.Integer, nullable=False)
    side_length = db.Column(db.Integer, nullable=False)

    full_length_back = db.Column(db.Integer, nullable=False)
    center_back = db.Column(db.Integer, nullable=False)
    back_shoulder_slope = db.Column(db.Integer, nullable=False)
    across_back = db.Column(db.Integer, nullable=False)
    back_shoulder_length = db.Column(db.Integer, nullable=False)
    back_arc = db.Column(db.Integer, nullable=False)
    waist_arc_back = db.Column(db.Integer, nullable=False)
    back_neck = db.Column(db.Integer, nullable=False)
    back_across_shoulder = db.Column(db.Integer, nullable=False)
    back_dart_intake = db.Column(db.Integer, nullable=False)


    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("Measurement_Charts"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Chart Id= %s User Id= %s>" % (self.chart_id, self.user_id)


    # TODO EXPAND THIS FUNCTION TO ADD MORE MEASUREMENTS
    @classmethod
    def add_chart_to_db(cls, nickname, user_id, bust, waist, cflength):
        chart_to_add = cls(nickname, user_id, bust, waist, cflength)
        db.session.add(chart_to_add)




# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drafter.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."