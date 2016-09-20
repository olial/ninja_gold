"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        if 'gold' not in session:
            session['gold'] = 0
        if 'log' not in session:
            session['log'] = ''
        session['farm'] = random.randrange(10, 21)
        session['cave'] = random.randrange(5, 11)
        session['house'] = random.randrange(2, 6)
        session['casino'] = random.randrange(-50, 51)
        return self.load_view('index.html')
    def process(self):
        session['title'] = ""
        if request.form['building'] == 'farm':
            session['gold'] += session['farm']
            message = "<div> You clicked farm and you got " + " " + str(session['farm']) + "</div><br>"
        elif request.form['building'] == 'cave':
            session['gold'] += session['cave']
            message = "You clicked cave and you got" + " " +  str(session['cave'])
        elif request.form['building'] == 'house':
            session['gold'] += session['house']
            message = "You clicked house and you got" + " " + str(session['house'])
        elif request.form['building'] == 'casino':
            session['gold'] += session['casino']
            message = "You clicked casino and you got" + " " +  str(session['casino'])

        session['log'] += message
        return redirect('/')
    def reset(self):
        session['gold'] = 0
        session['log'] = ''
        return redirect('/')
