#Task4.
#Ваша задача - доработать механизм выборки нужного предложения. Сейчас у нас следующая система:
#- перебираем предложения в списке
#- как только одно из них подоходит под уровень и содержит нужное слово - печатаем.

#Это не то, что нужно для бота. Для него нам, как минимум, нужно сохранять результат подброки куда-то, чтоб, в будущем, отправить в Телеграме, как ответ, а не печатать в командной строке.
#То есть, результат нужно вложить в переменную.

#При этом result = "some sentence" тут не подойдет. Ведь у нас есть три варианта результата.
#- ни одно предложение не совпало
#- одно совпадение
#- несколько совпадений.

#Значит, наш результат это СПИСОК, в который можно класть совпавшие варианты или же предусмотреть доработку, когда список пуст.


data_user = {"Language": "English", 
				"user_name": "Sarah",
				"user_id": "123654",
				"password": "qweasd123",
				"first_name": "Sarah",
				"second_name": "Connor",
				"user_level": "B1"}



user_message = {"user": data_user, 
				"text_message": "year"}


sentences = [
			{"text": "Merry Christmas and happy new year.",
				"user_level": "A1"},
			{"text": "Will you be around this time next year?", 
				"user_level": "A2"},
			{"text": "Thousands of tourists descend on the lake every year.", 
				"user_level": "B1"},
			{"text": "He has a mental illness and every year he is tested.", 
				"user_level": "B2"},
			{"text": "All our family gathered at the big round table to celebrate the New Year.", 
				"user_level": "C1"}]


result_list = []

for sentence in sentences:
	if user_message.get("user").get("user_level") == sentence.get("user_level"):
		if user_message.get("text_message") in sentence.get("text"):
			result_list.append(sentence.get("text"))

print(result_list)

