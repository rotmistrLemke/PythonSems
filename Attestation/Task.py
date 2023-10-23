import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data[['robot_indicator', 'human_indicator']] = data['whoAmI'].apply(lambda x: pd.Series(dict(robot = int(x == 'robot'), human = int(x == 'human'))))
print(data)

