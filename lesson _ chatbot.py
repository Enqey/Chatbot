# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:51:07 2022

@author: Enqey De-Ben Rockson
"""
#1 - import libraries
import re
import long_responses as long
import random 

#3
#create get_response function which takes a user input as the keyword
def get_response(user_input):
#create a fxn that splits the messages in an array and analyze each word separately by removing all these symbols from the message   
#these symbols are very common symbols found in general statements, user input is the input statement  
#nte: the string in the fxn must be defined in the dictionary under the fxn
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#2
#create an infinite while true loop so you can always get long responses 
#Testing the response system

while True:
    print('Bot: ' + get_response(input('You: ')))
    
    
#4
#function that calculates the probability that the input is appropraite
#user_message = user input
#recognised_word = keyword
#single_response = tells if the answer should be a single answer or a long response
#required words = empty list
def message_probability (user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1 
#this means is the recognized word in the sentence by the user is recognized, then the sentence is a more accurate sentence hence.... 

#calculate the percentage of recognised words in the user message
    Percentage = float(message_certainty) / float(len(recognised_words))

#5
#to check the required words are included in the user message
    for word in recognised_words:
        if word not in user_message:
            has_required_words = False
#this means if the recognized word is not in the sentence given by the user , then the sentence is not an accurate sentence hence.... 
            break

#6
#this code reads the required words, if true the percentage is converted into an integer and multiplied by 100, else 0 is returned 
    if has_required_words or single_response:
        return int(Percentage*100)
    else:
        return 0

#7
#CREATE A FXN TO CHECK ALL MESSAGE
def check_all_messages(message):
#create an empty dictionary
    highest_prob_list = {}

#8
#create a helper function to simplify the response creation
    def response(bot_response, list_of_words, single_response = False, required_words =[]):

#refer to highest_prob_list as a nonlocal so it can be used in this function 
        nonlocal highest_prob_list

#create a key at the index of bot_response and add items to bot response
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

#9
#RESPONSES----------------------------------------------------------------------------
#The key (hello) is the response, next group of words are the keywords in the users input
#set response to true if the response is a single response - this also shows theres no required qord but a boolean sentence 
#setting required words mean, the key (response) only pops up if the required words pop up in the the user input
    response('Hello!', ['hello','hi','sup','hey','heyo'], single_response= True)
    response('I\'m doing fine, and you?', ['how','are','you','doing'], required_words= ['how'])
    response('Thank you!', ['i','love','code','palace'], required_words= ['code', 'palace'])
    
#test function
#best match looks through all response list and returns the response with the highest probability of keywords in its list of word
#max value returns value with the highest probability list
#return the key of the highest value from the highest prob.list
#when you enter keywords which requires two differents responses, the bot replies with answers to keywords which have the highest probobility 
    best_match = max(highest_prob_list, key =highest_prob_list.get)
    print(highest_prob_list)
    return best_match
    
#10
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

#11
#responses can be written hear to avoind cluster on a code page

#create a function to reply to unclear random messages
def unknown():
    response = ['coul you rephrase the ?',
                "....",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
 
