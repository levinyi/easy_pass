from django.shortcuts import render

# Create your views here.
class User(object):
	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
		