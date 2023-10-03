PYTHON3 = python3

init: .venv
	. .venv/bin/activate && pip install -r requirements.txt

.venv:
	$(PYTHON3) -m venv .venv

clean:
	rm -rf .venv

start: .venv
	. .venv/bin/activate && python manage.py runserver

up:
	docker compose up --build

# usage: `make && make start` or `sudo make up`
