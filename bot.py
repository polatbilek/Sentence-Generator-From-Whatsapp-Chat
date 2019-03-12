from nltk import trigrams
from collections import defaultdict
import nltk
import numpy
import copy
import argparse

def read_messages(path, target, mode):
	sentences = []

	with open(path, "r", encoding="utf8") as f:
		for line in f:
			if mode == "one":
				splitted = line.strip().split(target + ":")
				if len(splitted) > 1 and "görüntü dahil edilmedi" not in line and "<Media omitted>" not in line:
					sentences.append(splitted[1])
			else:
				splitted = line.strip().split(target + ": ")
				if len(splitted) > 1 and "görüntü dahil edilmedi" not in line and "<Media omitted>" not in line:
					sentences.append(splitted[1])

	return sentences

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', type=int,
						help='Length of the sentence you want to generate')
	parser.add_argument('-p', type=str,
						help='absolute path to the chat file')
	parser.add_argument('-name', type=str,
						help='name of the person from chat (e.g. "-name Ozan") if you want to include all person from chat type all (e.g. "-name all")')

	args = parser.parse_args()

	length = args.l
	chat_file_path = args.p
	name_of_target_person = args.name

	if name_of_target_person == "all":
		sentences = read_messages(chat_file_path, "", mode="all")
	else:
		sentences = read_messages(chat_file_path, name_of_target_person, mode="one")

	model = defaultdict(lambda: defaultdict(lambda: 0))

	for sentence in sentences:
		token = nltk.word_tokenize(sentence)
		for w1, w2, w3 in trigrams(token, pad_right=True, pad_left=True):
			model[(w1, w2)][w3] += 1

	for w1_w2 in model:
		total_count = float(sum(model[w1_w2].values()))
		for w3 in model[w1_w2]:
			model[w1_w2][w3] /= total_count

	text = [None, None]
	sentence_finished = False

	while not sentence_finished:
		temp_model = copy.deepcopy(model)

		a = numpy.random.choice(a=len(list(temp_model[tuple(text[-2:])].values())), size=1, replace=False, p=list(temp_model[tuple(text[-2:])].values()))

		text.append(list(temp_model[tuple(text[-2:])].keys()).pop(a[0]))

		if len([t for t in text if t]) >= length:
			sentence_finished = True

	print(' '.join([t for t in text if t]))
