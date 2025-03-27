install:
	pip install --upgrade pip
	pip install -r requirements.txt

connect:
	sudo openvpn --config jorgeb1.ovpn

create:
	python3 -m venv .venv

activate:
	source .venv/bin/activate

