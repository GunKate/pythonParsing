from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_eanglish_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id ="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return{
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print ("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_eanglish_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get ("word_definition")

        translator = Translator()
        word_definition_ru = translator.translate(word_definition, dest="ru")
        word_ru = translator.translate(word, dest="ru")

        print(f"значение слова - {word_definition_ru.text}")
        user = input ("Что это за слово? ")
        if user == word_ru.text:
            print ("Все верно!")
        else:
            print(f"ответ неверный было загадано это слово - {word_ru.text}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру")
            break

word_game()