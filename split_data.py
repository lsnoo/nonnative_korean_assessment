import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

raw_data = pd.read_csv('./pronun.csv', names=['path', 'score'])
print(raw_data)

def count_l1(data_frame):
	eng = 0
	eu = 0
	asia = 0
	sjr = 0
	for i in range(len(data_frame)):
		if 'eng' in data_frame.iloc[i]['path']: eng += 1
		elif 'eu' in data_frame.iloc[i]['path']: eu += 1
		elif 'asia' in data_frame.iloc[i]['path']: asia += 1
		elif 'sjr' in data_frame.iloc[i]['path']: sjr += 1
	print(eng+eu+asia+sjr)
	eng = round(eng * 100 / len(data_frame), 2)
	eu = round(eu * 100 / len(data_frame), 2)
	asia = round(asia * 100 / len(data_frame), 2)
	sjr = round(sjr * 100 / len(data_frame), 2)
	print('eng = {0}%, eu = {1}%, asia = {2}%, sjr = {3}%'.format(eng, eu, asia, sjr))

#print('entire_data')
#count_l1(raw_data)

## L1 열 추가
L1 = []
for row in raw_data['path']:
	if 'eng' in row: L1.append('eng')
	elif 'eu' in row: L1.append('eu')
	elif 'asia' in row: L1.append('asia')
	else: L1.append('sjr')
raw_data['L1'] = L1

print(raw_data)

def split_data(raw_data, test_frac):
	split = StratifiedShuffleSplit(n_splits=1, test_size=test_frac, random_state=1313)

	for train_index, test_index in split.split(raw_data, raw_data['L1']):
		str_train_set = raw_data.iloc[train_index]
		str_test_set = raw_data.iloc[test_index]

	return str_train_set, str_test_set

train_set, test_sets = split_data(raw_data, 0.2)
test_set, valid_set = split_data(test_sets, 0.5)

for d in (train_set, test_set, valid_set):
	d.drop('L1', axis=1, inplace=True)
print(train_set)
print(test_set)
print(valid_set)
#print('train_set')
#count_l1(train_set)
#print('test_set')
#count_l1(valid_set)
#print('valid_set')
#count_l1(test_set)

train_set.to_csv('./pronunciation/train.csv', index=None, header=None)
valid_set.to_csv('./pronunciation/valid.csv', index=None, header=None)
test_set.to_csv('./pronunciation/test.csv', index=None, header=None)
