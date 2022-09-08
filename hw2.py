#Мы с вами готовимся к тому, чтобы сделать бота, прокачивающего знания английского. Юзер вводит слово и в соответствии с его уровнем, ему выдается несколько предложений на английском, из которых понятен контекст.

#Подумайте, как можно, с помощью словаря, описать нашего пользователя и предложение. Имено предложение, как собирать их в списки мы рассмотрим дальше.

#Скажем, у предложения должно быть, как минимум, 2 поля:
#Текст предложения
#Уровень (для начинающих что-то простое, для более продвинутых - хитрое.)

#Опишите это с помощью словаря, и то же самое проверните с юзером.

#Типы данных выбирайте сами, исходя из логики.

#Task 2.1
data_user = {"Language": "English", 
				"user_name": "Ivan",
				"user_id": "123654",
				"password": "qweasd123",
				"first_name": "Ivan",
				"second_name": "Makhomet",
				"user_level": "B1"}

sentence = {"text": "Merry christmas and Happy new year.",
				"word": "year", 
				"user_level": "B1"}

#check 2.1
print(data_user)
print(data_user["user_name"])
print(data_user["second_name"])
print(sentence)


#Используйте то, что мы прошли на лекции, чтобы, с помощью словаря описать героя и снаряжение в ролевой игре, например Готике или Дьябло. Что-то подобное у вас легко может выпасть, если будете заниматься разработкой, скажем, какой браузерки.

#Типы данных выбирайте сами. Понять из абстрктного описания, какие именно данные должны быть в коде, это очень нужный навык. Умение правильно описать данные - суперважная вещь.

#Броня: -Защита в ближнем бою; -Защита в далнем бою; -Вес;

#Оружие: -Магическое или нет?; -Урон; -Урон магией(если не магичесое, то урон, соответвенно, никакой); -Вес;

#Персонаж:-Уровнь; -Здоровье; -Мана.

#Task 2.2 
armor = {"close_battle": 5, 
		"distance_battle": 15,
		"weight": "20 кг.",
		"origin": "silver"}

weapon = {"magic": "True",
		"damage": 5,
		"magic_damage": 10,
		"weight": "5 кг."}

personage = {"person_name": "Sara", 
			"person_level": "80", 
			"age": 25,
			"gender": "female",
			"health": 75,
			"mana": 50}

#check 2.2
print(armor["origin"])
print(weapon["magic"])
print(personage["person_level"])

#Task 2.3
#Развить задачу 2 - добавить герою поля "Оружие" и "Броня", куда вставить словари с, собственно, оружием и броней. То есть, должны получиться словари в словаре.

personage = {"person_name": "Sara", 
			"person_level": "80", 
			"age": 25,
			"gender": "female",
			"health": 75,
			"mana": 50,
				"armor" : {"close_battle": 5, 
							"distance_battle": 15,
							"weight": "20 кг.",
							"origin": "silver"},

				"weapon" : {"magic": "True",
							"damage": 5,
							"magic_damage": 10,
							"weight": "5 кг."}}

person_name = personage.get("person_name")
armor_weight = personage.get("armor").get("weight")
weapon_magic_damage = personage.get("weapon").get("magic_damage")

print(person_name)
print(armor_weight)
print(weapon_magic_damage)