#Task 3.
#Домашнее задание. 

#Собсна, теперь мы уже можем подготовить данные для нашего бота.
#Итак, у нас будет три сущности, которые нужно описать.

#Пользователь.
#Предложение
#Сообщение от пользователя.

#Они нам нужны для организации процесса: Пользователь отправляет Сообщение, которое содержит слово на английском.
#Из списка предложений, выбирается то, у котрого уровень пользователя совпадает с уровнем сложности предложения, а слово, которое было в сообщении Пользователя, входит в состав предложения.

#Соответвенно, используя то, что мы прошли, опишите следующие структуры (часть уже была в предыдущих ДЗ)
#- Пользователь
#- Предложение
#- Список предложений.

#Какие именно структуры использовать, решайте сами, отталкиваясь от задачи.
#Например, у нас укзано, что из списка предложений нужно выбрать то, которое соответвует Пользователью по уровню, и которое содержит нужное слово.
#Значит, мы можем сделать сущность Sentence с двумя полями Text и Level.

data_user = {"Language": "English", 
				"user_name": "Ivan",
				"user_id": "123654",
				"password": "qweasd123",
				"first_name": "Ivan",
				"second_name": "Makhomet",
				"user_level": "B1"}



user_message = {"user": "data_user", 
				"text_message": "year"}


sentence1 = {"text": "Merry Christmas and happy new year.",
				"user_level": "A1"}

sentence2 = {"text": "Will you be around this time next year?", 
				"user_level": "A2"}

sentence3 = {"text": "Thousands of tourists descend on the lake every year.", 
				"user_level": "B1"}

sentence4 = {"text": "He has a mental illness and every year he is tested.", 
				"user_level": "B2"}

sentence5 = {"text": "All our family gathered at the big round table to celebrate the New Year.", 
				"user_level": "C1"}

sentences_list = [sentence1, sentence2, sentence3, sentence4, sentence5]

print(data_user["user_name"], data_user["user_level"], user_message["text_message"])
print(sentences_list)
