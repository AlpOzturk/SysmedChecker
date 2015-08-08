
import os

LETICIA_DIR = 'String_Siblings_updated'
LETICIA_ID_INDEX = 4
LETICIA_SCORE_INDEX = -1
LETICIA_DELIMITER = '\t'

def run():
	leticia_data = get_leticia_data(LETICIA_ID_INDEX, LETICIA_SCORE_INDEX, LETICIA_DELIMITER)

def get_leticia_data(id_index, score_index, delimiter):
	edges = dict()
	files = [f for f in os.listdir(LETICIA_DIR)]
	for f in files:
		file_name = LETICIA_DIR + '/' + f
		in_file = open(file_name, 'r')
		print 'Processing file ' + f + '...'
		process_file(edges, in_file, id_index, score_index, delimiter)


def process_file(edge_map, in_file, id_index, score_index, delimiter):
	first_line = True
	inconsistency = False
	for line in in_file:
		if first_line:
			first_line = False
		else:
			data = line.strip().split()
			id1 = data[id_index]
			id2 = data[id_index - 1]
			score = int(float(data[score_index]) * 1000)
			key = (id1, id2) if id1 < id2 else (id2, id1)
			if key in edge_map and edge_map[key] != score:
				print 'INCONSITENCY DETECTED for key ' + key + '. Scores ' + str(score) + ' & ' + edge_map[key]
				inconsistency = True
			else:
				edge_map[key] = score
	in_file.close()
	if not inconsistency:
		print 'No inconsistency detected.'

run()
