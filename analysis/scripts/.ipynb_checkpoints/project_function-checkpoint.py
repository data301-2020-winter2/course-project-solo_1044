import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def cleaning(data):
    data=(data
              #.dropna()
              .rename(columns={'charges': 'cost'})
              .reset_index()
              .drop(columns=['index'])
              .sort_values(by=['age'])
              )