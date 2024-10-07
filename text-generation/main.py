import random
import numpy as np
from tensorflow.keras.models import sequential
import tensorflow as tf

# sequential  = tf.keras.models.Sequential()

filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

text = open(filepath,'rb').read().decode(encoding='utf-8')

text =text[300000:800000]

characters = sorted((set(text)))

char_to_index = dict((c,i) for i,c in enumerate(characters))
index_to_char = dict((i,c) for i,c in enumerate(characters))

sentence = []
next_character = []


