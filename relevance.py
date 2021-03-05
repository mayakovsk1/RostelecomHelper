from keywords import key_words
from dictionary import dictionary_key_words


#  {релевантность: заголовок}
relevance_check = {}
string = '''Извините, не можем ответить на ваш вопрос.
Пожалуйста, обратитесь в службу поддержки по номеру: 8-800-1000-800'''


#  Сравнивает введенные слова с добытыми с сайта
#  question - введённые слова
def entry_relevance(question):


    try:
        #  проверка на соответствие слов
        for i in dictionary_key_words:
            relevance_check[len(set(question.split()) & dictionary_key_words[i])] = i
        relevance_check_value = relevance_check[max(relevance_check)]


        if max(relevance_check) < 1:
            relevance_check.clear()
            return string
        else:
            relevance_check.clear()
            return relevance_check_value


    except Exception:
        return string


if __name__ == '__main__':
    while True:
        message = input('>>>')
        if message == '0':
            break
        print(entry_relevance(message))
        print()