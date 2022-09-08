#Task5.
#Ваша задача - переписать решение, которое вы нашли на практической, с помощью функций. Результат практической у каждой группы разный, поэтому ориентируйтесь не на готовый код, а на задачу.
#То есть, вы писали фильтр, который создает список предложений из списка словарей без функций - а теперь пишите с ними. 
#Какие аргументы использовать и какой ретертн, сделать одну функцию или много маленьких - решение за вами. Важно самому искать максимально эффективный путь.

#Вот тут можете взять результаты практической от Группы 1, если у кого нет:
#https://discord.com/channels/943636503190462574/966856654907912236/982644264947314699

user = {"username" : "Sarah_Conor",
		"level" : 1} 

message = {"user": user,
		   "text": "take"}

sentences = [
	{"text": "When my time comes \nForget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \nOh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
			]

def sentence_search(user, message, sentence):
    relevant_sentence = []
    check_level = False

    user_level = user.get("level")
    user_message = message.get("text")

    for txt in sentence:
        if txt.get("level") == user_level:
            check_level = True
            if user_message in txt.get("text"):
                relevant_sentence.append(txt.get("text"))
    result = [relevant_sentence, check_level]
    return result

def result(result):
    if result[1] == False:
        print("There are no sentence for your level")
    elif len(result[0]) == 0:
        print("There are no sentence of your level and with your word")
    if len(result[0]) == 1:
        print((result[0])[0])
    if len(result[0]) > 1:
        for txt in result[0]:
            print(txt)
                
#check def sentence_search
print(sentence_search(user, message, sentences)) # Вывод соответствующего предложения для уровня пользователя (будет список) и проверка на "True", строка 37.

print("----------")
print("----------")
result(sentence_search(user, message, sentences))
