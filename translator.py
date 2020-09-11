from translate import Translator
#translate module gives us the translation of the required language
fromlanguage=input("Enter your input language:")
tolanguage=input("Enter the required language:")
#getting input from the user and storing in a variable
translator= Translator(from_lang=fromlanguage,to_lang=tolanguage)
sentence=input("Enter the words you want to translate:")
translation = translator.translate(sentence)
print(translation)
