import os, json


def load_dataset() -> list[dict[str, str | bool | list[dict[str, str]]]]:

	data = []

	for filename in os.listdir('./data'):
		with open('./data/' + filename, 'r', encoding='utf-8') as file:
			for line in file:
				data.append(json.loads(line))

	return data


def merge_dataset(path: str = './dataset.jsonl') -> None:

	with open(path, 'w', encoding='utf-8') as file:
		for filename in os.listdir('./data'):
			with open('./data/' + filename, 'r', encoding='utf-8') as f:
				for line in f:
					file.write(line)
