from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/')
def start_here():
	return render_template("pirate_greet.html")

@app.route('/play')
def game():
	return render_template("pirate_game.html")

@app.route('/translate')
def translate():
	# takes input from pirate_game.html page (inputted on /play)
	input_sentence = request.args.get("input_sentence")
	print input_sentence

	pirate_dict = {"sir": "matey", "hotel" : "fleabag inn", "student" : "swabbie", "boy" : "matey", "madam" : "proud beauty", "professor": "foul blaggart", "restaurant" : "galley", "your" : "yer", "excuse" : "arr", "students" : "swabbies", "are" : "be", "lawyer" : "foul blaggart", "the" : "th'", "restroom" : "head", "my" : "me", "hello": "avast", "is" : "be", "man" : "matey"}

	# pirate_dict = {"sir": "matey", "hotel": "fleabag inn"}

	split_sentence = input_sentence.split()
	print split_sentence

	result_list = []
	for word in split_sentence:
		if word in pirate_dict:
			value = pirate_dict[word]
			result_list.append(value)
		else:
			result_list.append(word)
	
	result_sentence = string.join(result_list)

	return render_template("pirate_translate.html", input_sentence=input_sentence, result_sentence= result_sentence)


if __name__ == "__main__":
	app.run()