import numpy as np
import pandas as pd


path_to_movelist = r"C:\Users\jasak\PycharmProjects\pythonProject\movelist.txt"
movelist = np.squeeze(pd.read_csv(path_to_movelist, delimiter='\n', header=None).values)
