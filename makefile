mm:
	@python manage.py makemigrations

m:
	@python manage.py migrate

rs: 
	@python manage.py runserver