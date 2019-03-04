# TextClassifier
Simple text classifier with python

This module will read training file from "data.txt"
training file will look like this:
```
greetings
how are you
what do you do
what you doin
hello
hi
hai
good morning
good evening
good afternoon
good night#
```
The first row will be read as class name where the other rows are the sentence that define the class until '#' symbol.

It will make a dictionary that consist of class name with their sentences.

every word will have their own value. That value will be used for counting score for classifying text.


refences:

https://towardsdatascience.com/multinomial-naive-bayes-classifier-for-text-analysis-python-8dd6825ece67
https://gist.github.com/ugik
