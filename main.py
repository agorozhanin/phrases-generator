import random

from datasets import *

COUNT_ITERATION = 500

output_list = []
for i in range(COUNT_ITERATION):
    words_list = [
        random.choices(basic_words, weights=basic_words_weights)[0],
        random.choices(mood, weights=mood_weights)[0],
        random.choices(energy, weights=energy_weights)[0],
        random.choices(emotions, weights=emotions_weights)[0],
        random.choices(variation_1, weights=variation_1_weights)[0],
        random.choices(variation_2, weights=variation_2_weights)[0],
        random.choices(variation_3, weights=variation_3_weights)[0], ]

    words_list_for_concatenate = []
    for word in words_list:
        if word != '':
            words_list_for_concatenate.append(word)

    output_list.append(', '.join(words_list_for_concatenate))

print(*output_list, sep='\n')
