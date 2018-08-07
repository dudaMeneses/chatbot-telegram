FROM rasa/rasa_nlu
ADD ./configs /app/configs
ADD ./data/examples/rasa /app/data
WORKDIR /app
CMD ["run","python","-m","rasa_nlu.train","-c","configs/config_spacy.yml","-d","data/training-data.json","--path","projects"]
CMD ["start","--path","projects"]