# chatbot-telegram

# Docker
docker run -p5555:5000 rasa/rasa_nlu:0.10.4-spacy python -m rasa_nlu.train configs/spacy_config.json

# Python bot
pipenv shell
export FLASK_APP=[your file path]
flask run

# ngrok
./ngrok http 5000

# webhook.py
Edit webhook.py with https address created by ngrok
