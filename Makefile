# local use only
SHELL := /bin/bash # use bash syntax
run:
	uvicorn app:app --host=0.0.0.0 --port=8000 --log-config=config/log-config.yml
install:
	@pip install -r requirements-dev.txt