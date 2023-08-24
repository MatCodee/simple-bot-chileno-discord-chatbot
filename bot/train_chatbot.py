# Aqui vamos a implementar la estructura de entrenamiento del chatbot
import nltk
import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random


# Entrenamiento de la red neuronal 
