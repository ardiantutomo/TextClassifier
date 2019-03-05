import os,pickle


class Trainer:
    training_data = []  

    def load_default_data(self,inpath,outpath):    
        classes = ""
        with open(inpath, encoding='utf-8-sig') as file: # text file
            for line in file:
                file_data = line.rstrip()
                if classes == "":
                    classes = file_data
                else:
                    if file_data[len(file_data)-1] == "#":
                        file_data = file_data[:-1]
                        self.training_data.append({"class":classes, "sentence":file_data})
                        classes = ""
                    else:
                        self.training_data.append({"class":classes, "sentence":file_data})
        with open(outpath,"wb") as output_file:
            pickle.dump(self.training_data, output_file)


    def training(self, classes, sentence,path):
        self.training_data.append({"class":classes, "sentence":sentence})
        with open(path,"wb") as output_file:
            pickle.dump(self.training_data, output_file)

    def print_training_data(self):
        result = {}
        classes = list(set([a['class'] for a in self.training_data])) # get name of class   
        for c in classes:
            result[c] = [] # make list for each class

        for data in self.training_data:
            result[data['class']].extend([data['sentence']])
        print (result)

if __name__ == '__main__':
    while True:
        z = Trainer()
        classes = input("Class: ")
        sentence = input("Sentence: ")
        path = "trained.trn"
        path2 = "data.txt"
        z.load_default_data(path2,path)
        z.training(classes,sentence,path)
        z.print_training_data()