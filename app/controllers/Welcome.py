"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

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
        print "im am index"

        all_friends = self.models['WelcomeModel'].get_all_friends()

        return self.load_view('index.html', all_friends=all_friends)

    def add(self):
        print "hi i'm add method"

        return self.load_view('add.html')

    def add_submit(self):
        print "hi i'm add_submit method"

        new_friend_details = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        self.models['WelcomeModel'].add_friend(new_friend_details)
        return redirect('/')

    def delete(self, id):
        print "hi i'm delete_ method"

        user = self.models['WelcomeModel'].get_user(id)
        return self.load_view('delete.html', id = id, user=user)

    def delete_submit(self, id):
        print "hi i'm delete_submit method"
        self.models['WelcomeModel'].delete_submit(id)
        flash ('deleted')
        return redirect('/')
        pass

    def show_edit(self, id):
        print "hi i'm show_edit method"
        user = self.models['WelcomeModel'].get_user(id)
        print user
        return self.load_view('show_user.html', user=user)

    def edit_submit(self, id):
        print "hi i'm edit_submit method"
        edit_friend = {
                'name': request.form['name'],
                'email': request.form['email'],
                'id': id
            }
        print edit_friend
        self.models['WelcomeModel'].edit_submit(edit_friend)

        return redirect('/')




