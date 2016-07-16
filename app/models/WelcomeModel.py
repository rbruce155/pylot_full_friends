"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
	def __init__(self):
		super(WelcomeModel, self).__init__()

	def get_all_friends(self):
		get_all_friends_query = "SELECT * from friends"
		return self.db.query_db(get_all_friends_query)

	def add_friend(self, new_friend_details):
		print "hi i am add_freind model"
		add_query = "INSERT INTO friends (name, email, created_at, updated_at) VALUES (:name, :email, NOW(), NOW())"
		add_data = { 'name': new_friend_details['name'], 'email': new_friend_details['email'] }
		return self.db.query_db(add_query, add_data)

	def get_user(self, id):
		print "I'm get_user model"
		id_query = "SELECT * FROM friends WHERE id = :id"
		id_data = {'id': id}
		return self.db.query_db(id_query, id_data)

	def delete_submit(self, id):
		delete_user_query = 'DELETE FROM friends WHERE id = :id'
		delete_id_data = {'id': id}
		print id,'deleted'
		return self.db.query_db(delete_user_query, delete_id_data)

	def edit_submit(self, edit_friend):

		edit_query = 'UPDATE friends SET name= :name, email= :email, updated_at= NOW() WHERE id= :id '
		edit_data = { 'name': edit_friend['name'], 'email': edit_friend['email'], 'id':edit_friend['id']  }
		return self.db.query_db(edit_query, edit_data)



 # Below is an example of a model method that queries the database for all users in a fictitious application

 #    Every model has access to the "self.db.query_db" method which allows you to interact with the database

 #    def get_users(self):
 #        query = "SELECT * from users"
 #        return self.db.query_db(query)

 #    def get_user(self):
 #        query = "SELECT * from users where id = :id"
 #        data = {'id': 1}
 #        return self.db.get_one(query, data)

 #    def add_message(self):
 #        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
 #        data = {'message': 'awesome bro', 'users_id': 1}
 #        self.db.query_db(sql, data)
 #        return True

 #    def grab_messages(self):
 #        query = "SELECT * from messages where users_id = :user_id"
 #        data = {'user_id':1}
 #        return self.db.query_db(query, data)

