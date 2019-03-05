import nltk,os,pickle
from math import log10
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

class TextClassifier:
    stemmer = WordNetLemmatizer()
    training_data,classes,corpus_words,class_words = [],[],{},{}     

    def check_training_data(self,path): 
        #default training data
        if os.path.exists(path) == False:
            return False
        else:
            return True


    def load_training_data(self, path):
        with open(r"trained.trn","rb") as file:
            self.training_data = pickle.load(file)


    def __init__(self):
        path = "trained.trn"
        if self.check_training_data(path):
            self.load_training_data(path)
            self.classes = list(set([a['class'] for a in self.training_data])) # get name of class        
            print(self.classes)
            print()
            for c in self.classes:
                self.class_words[c] = [] # make list for each class

            for data in self.training_data:
                for word in nltk.word_tokenize(data['sentence']):
                    if word not in ["?", "'s"]:
                        stemmed_word = self.stemmer.lemmatize(word.lower())
                        if stemmed_word not in self.corpus_words:
                            self.corpus_words[stemmed_word] = 1
                        else:
                            self.corpus_words[stemmed_word] += 1
                        self.class_words[data['class']].extend([stemmed_word])
        else:
            print ("Error trained data not found!")
            return

    def get_score(self,sentence, class_name):
        score = 0
        for word in nltk.word_tokenize(sentence):
            if self.stemmer.lemmatize(word.lower()) in self.class_words[class_name]:
                score += 1 + self.corpus_words[self.stemmer.lemmatize(word.lower())]
        try:
            return 1 + log10(score)
        except:
            return 0

    def classify(self,sentence):
        final_class = None
        final_score = 0
        for c in self.class_words.keys():
            score = self.get_score(sentence, c)
            if score > final_score:
                final_class = c
                final_score = score

        return final_class, final_score

    def get_definition(self,sentence):
        # processing sentence to get noun or adjective
        # assumption = NN and JJ is a word that user wants to know about
        words = nltk.word_tokenize(sentence)
        tagged = pos_tag(words)
        word = ""
        before = ""
        for t in tagged:
            if before == "" or before in ["JJ", "NN"]:
                if t[1] in ["JJ", "NN", "NNP", "NNS"]:    
                    word += t[0] + " "
                    before = t[1]
            else:
                return word
        
        return word

if __name__ == '__main__':
    while True:
        z = TextClassifier()
        a = input(">> ")
        print(z.classify(a)[0])