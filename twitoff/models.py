"""
SQLAlchemy models and utility functions for TwitOff
"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users corresponding to Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet text and data."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allows for text + links
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '-Tweet {}-'.format(self.text)


def example_users():
    """Example data to play with."""
    austen = User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    kermit = User(id=3, name='kermit')
    frank = User(id=4, name ='frankenstein')
    DB.session.add(austen)
    DB.session.add(elon)
    DB.session.add(kermit)
    DB.session.add(tesla)
    DB.session.commit()

def example_tweet():
    """Example data to play with."""
    tweet1 = Tweet(id=1, text='Lambda School', user_id=1)
    tweet2 = Tweet(id=2, text='Space X', user_id=1)
    tweet3 = Tweet(id=3, text='it aint easy being green', user_id=1)
    tweet4 = Tweet(id=4, text='Groan', user_id=1)
    tweet5 = Tweet(id=2, text='Satellites', user_id=1)
    tweet6 = Tweet(id=3, text='Miss Piggy', user_id=1)
    DB.session.add(tweet1)
    DB.session.add(tweet2)
    DB.session.add(tweet3)
    DB.session.add(tweet4)
    DB.session.add(tweet5)
    DB.session.add(tweet6)
    DB.session.commit()

    # DB.session.add(tweet) 
    # and DB.session.commit() 
    # after appending to a user.tweet.