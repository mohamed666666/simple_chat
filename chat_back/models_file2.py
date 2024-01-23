import whisper
import numpy as np
import torch
from googletrans import Translator, LANGUAGES
from flair.data import Sentence
from flair.models import SequenceTagger
from transformers import BertTokenizerFast, BertForTokenClassification, pipeline
from transformers import AutoModelForTokenClassification, AutoTokenizer

def transcribe_wav_file(wav_file_path, langauge):
    # Initialize the device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model('base', device=device)
    
    try:
        result = model.transcribe(wav_file_path, language=langauge)
        return result['text']
    except Exception as e:
        return str(e)

def translate_text(text, source_lang, target_lang):
    # Create a Translator object
    translator = Translator()

    # Detect the source language if not specified
    if source_lang == "auto":
        source_lang = translator.detect(text).lang

    # Translate the text
    translation = translator.translate(text, src=source_lang, dest=target_lang)

    return translation.text

def ner_en(text):
    # load tagger
    tagger = SequenceTagger.load("flair/ner-english")

    # make example sentence
    sentence = Sentence(text)

    # predict NER tags
    pred = tagger.predict(sentence)
    
    # iterate over entities and print
    entities, labels = [], []
    for entity in sentence.get_spans('ner'):
        entities.append(entity.text)
        labels.append(entity.labels[0].value)
    return entities, labels

def ner_es(text):
    # load tagger
    tagger = SequenceTagger.load("flair/ner-spanish-large")

    # make example sentence
    sentence = Sentence(text)

    # predict NER tags
    pred = tagger.predict(sentence)
    
    # iterate over entities and print
    entities, labels = [], []
    for entity in sentence.get_spans('ner'):
        entities.append(entity.text)
        labels.append(entity.labels[0].value)
    return entities, labels

def ner_it(text):

    tokenizer = BertTokenizerFast.from_pretrained("osiria/bert-italian-cased-ner")
    model = BertForTokenClassification.from_pretrained("osiria/bert-italian-cased-ner")

    ner = pipeline("ner", model = model, tokenizer = tokenizer, aggregation_strategy="first")
    nlp = ner(text)
    
    # iterate over entities
    entities, labels = [], []
    for entity in nlp:
        entities.append(entity['word'])
        labels.append(entity['entity_group'])
    return entities, labels

def ner_ar(text):

    ner_model = AutoModelForTokenClassification.from_pretrained("ychenNLP/arabic-ner-ace")
    ner_tokenizer = AutoTokenizer.from_pretrained("ychenNLP/arabic-ner-ace")

    ner = pipeline("ner", model=ner_model, tokenizer=ner_tokenizer, grouped_entities=True)
    nlp = ner(text)
    
    # iterate over entities
    entities, labels = [], []
    for entity in nlp:
        entities.append(entity['word'])
        labels.append(entity['entity_group'])
    return entities, labels
