import fasttext
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .cosine_similarity import cosine_one_many

class FastTextVectorizer:
    def __init__(self, model_path):
        self.model = fasttext.load_model(model_path)

    def vectorize_sentence(self, sentence):
        sentence_vector = self.model.get_sentence_vector(sentence)
        return sentence_vector

    def vectorize_sentences(self, sentences):
        vectorized_sentences = [self.vectorize_sentence(sentence) for sentence in sentences]
        return vectorized_sentences


class TFIDFVectorizer:

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.vectorizer = TfidfVectorizer(stop_words="english", 
                                          tokenizer=self.tokenizer)

    def calculate_tfidf(self, search_terms, sentences):
        vectors = self.vectorizer.fit_transform([search_terms] + sentences)
        #print(vectors)
        cosine_similarities = linear_kernel(vectors[0:1], vectors).flatten()
        #print(cosine_similarities)
        
        sentences_scores = [item.item() for item in cosine_similarities[1:]]
        max_score = float(max(sentences_scores))
        max_score_idx = sentences_scores.index(max_score)
        output=dict(most_similar_sentence=sentences[max_score_idx], score=max_score)
        #print(output)
        return output
            