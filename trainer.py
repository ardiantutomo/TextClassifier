import os,pickle
import sys


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
                    if file_data== "#":
                        classes = ""
                    else:
                        self.training_data.append({"class":classes, "sentence":file_data})
        with open(outpath,"wb") as output_file:
            pickle.dump(self.training_data, output_file)

    def check_data(self,path): 
        if os.path.exists(path) == False:
            return False
        else:
            return True

    def load_trained_data(self, inpath):
        with open(inpath,"rb") as file:
            self.training_data = pickle.load(file)


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

        key = ""
        for k,v in result.items():
            if key != k: 
                print(k)  
                key = k
            for z in v:
                print("- " + z) 
    
    def  export_to_txt(self, outpath):
        result = {}
        classes = list(set([a['class'] for a in self.training_data])) # get name of class   
        for c in classes:
            result[c] = [] # make list for each class
        
        for data in self.training_data:
            result[data['class']].extend([data['sentence']])

        key = ""
        with open(outpath,"w+") as file:
            for k,v in result.items():
                if key != k: 
                    file.write(k + "\n") 
                    key = k
                for z in v:
                    file.write(z + "\n") 
                file.write("#\n")
        file.close
        


if __name__ == '__main__':
    arguments = sys.argv[1:]
    z = Trainer()
    path = "trained.trn"
    path2 = "data.txt"

    if "-load-default" in arguments:
        #-load-default inFilePath outFilePath
        id = arguments.index("-load-default")
        if not z.check_data(arguments[id+1]) or not z.check_data(arguments[id+2]):
            print("File not found")
            exit
        z.load_default_data(arguments[id+1] ,arguments[id+2])


    if "-list" in arguments:
        z.print_training_data() 

    if "-export" in arguments:
        id = arguments.index("-export")
        z.export_to_txt(arguments[id+1])

    if "-train" in arguments:
        #-train inFilePath outFilePath
        if "-load" in arguments:
            id = arguments.index("-load")
            z.load_trained_data(arguments[id+1]) if z.check_data(arguments[id+1]) else print("File not found")
        else:
            id = arguments.index("-train")
            z.load_default_data(arguments[id+1] ,arguments[id+2])
            z.load_default_data(arguments[id+1] ,arguments[id+2])
        while True:
            z.print_training_data()
            classes = input("Class: ")
            sentence = input("Sentence: ")
            z.training(classes,sentence,path)