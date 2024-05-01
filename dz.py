# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()

import pandas as pd
from random import shuffle
lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI'] == 'robot','robot'] = '1'
data.loc[data['whoAmI'] == 'robot', 'human'] = '0'
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
print(data.head())