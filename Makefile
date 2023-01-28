install:
	python -m venv github_actions_demo
	source github_actions_demo/bin/activate
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-gcp:
	pip install --upgrade pip &&\
		pip install -r requirements-gcp.txt

install-azure:
	pip install --upgrade pip &&\
		pip install -r requirements-azure.txt
		
install-aws:
	pip install --upgrade pip &&\
		pip install -r requirements-aws.txt

test:
	python -m pytest -vv --cov=hello test_hello.py

lint:
	pylint --disable=R,C hello.py
	
format:
	black *.py
	


