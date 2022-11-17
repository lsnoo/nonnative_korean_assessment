import glob
import re
import json

flist = glob.glob('/data/lsnoo/topik_ProEval/*/lab/*.json')
wav_list = glob.glob('/data/lsnoo/topik_ProEval/*/sound/*.wav')
pronun_lines = []
fluency_lines = []
compreh_lines = []

for f in flist:
	with open(f, 'r', encoding='utf-8') as f1: json_data = json.load(f1)
	#print(f)
	wav_path = '/'.join(f.split('/')[:5]) + '/sound/' + f.split('/')[-1][:-4] + 'wav'
	#wav_path = ('.')[0] + '.wav'
	#print(wav_path)
	if wav_path not in wav_list: print('===============', wav_path)

	pronun = str(json_data["EvaluationMetadata"]["PronunProfEval"])
	fluency = str(json_data["EvaluationMetadata"]["FluencyEval"])
	compreh = str(json_data["EvaluationMetadata"]["ComprehendEval"])

	#print('Pronounciation: {0}, Fluency: {1}, Comprehension: {2}'.format(pronun, fluency, compreh))

	pronun_line = wav_path + ',' + pronun + '\n'
	fluency_line = wav_path + ',' + fluency + '\n'
	compreh_line = wav_path + ',' + compreh + '\n'

	pronun_lines.append(pronun_line)
	fluency_lines.append(fluency_line)
	compreh_lines.append(compreh_line)

with open('./pronun.csv', 'w') as f: f.writelines(pronun_lines)
with open('./fluency.csv', 'w') as f: f.writelines(fluency_lines)
with open('./compreh.csv', 'w') as f: f.writelines(compreh_lines)

