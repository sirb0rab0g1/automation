install:
	pipenv --three
	touch sample.py
	make fix

fix: # this command after installing certain 3rd party
	pip3 install pipenv
	pipenv run pip install pip==18.0
	pipenv install

run:
	pipenv run python automate-post.py

hp-run:
	pipenv run python hpautomation.py

clean:
	pipenv clean
	pipenv --rm
