# chatbot-telegram

## docker
~~docker run -p5555:5000 caneleiros-fc~~

## rasa.nlu
```
python -m rasa_nlu.train -c configs/config_spacy.yml -d data/examples/rasa/training-data.json
```
```
python -m rasa_nlu.server -P 5050 --path projects
```

## python bot
```
pipenv shell
```
```
export FLASK_APP=[your file path]
```
```
flask run
```

## ngrok
```
./ngrok http 5000
```

## webhook.py
Edit webhook.py with https address created by ngrok
