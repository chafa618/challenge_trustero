import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS as sw

class SpacyTokenizer:
    def __init__(self, model_name):
        self.model = spacy.load(model_name)
        self.punctuations = string.punctuation
        self.stop_words = sw

    def lemma_tokenizer(self, sent):
        tokens = self.model(sent)
        tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
        tokens = [word for word in tokens if word not in self.stop_words and word not in self.punctuations]
        return tokens
    
    def wsp_tokenizer(self, sent):
        tokens = self.model(sent)
        tokens = [word.lower_ for word in tokens]
        tokens = [word for word in tokens if word not in self.punctuations]
        return tokens

    def lemmatizer(self, sent):
        tokens = self.model(sent)
        lemmas = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
        return lemmas