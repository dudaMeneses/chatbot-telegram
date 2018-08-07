# chatbot-telegram

# docker
docker run -p5555:5000 caneleiros-fc run python -m rasa_nlu.train -c /app/configs/config_spacy.yml -d /app/data/training-data.json

# python bot
pipenv shell
export FLASK_APP=[your file path]
flask run

# ngrok
./ngrok http 5000

# webhook.py
Edit webhook.py with https address created by ngrok
