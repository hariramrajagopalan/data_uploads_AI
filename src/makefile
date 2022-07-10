deps:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install --editable .
	( \
       . .flasktest/bin/activate; \
    )

dev-env:
	python3 -m venv .flasktest

run:
	data_uploads start-server