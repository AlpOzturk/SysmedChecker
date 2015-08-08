
import os
import gzip

LETICIA_DIR = 'String_Siblings_updated'
LETICIA_ID_INDEX = 4
LETICIA_SCORE_INDEX = -1
LETICIA_DELIMITER = '\t'

ALP_FILE = '9606.protein.links.detailed.v10.txt.gz'
ALP_ID_INDEX = 0
ALP_SCORE_INDEX = -1
ALP_DELIMITER = ' '

def run():
	leticia_data = get_leticia_data(LETICIA_ID_INDEX, LETICIA_SCORE_INDEX, LETICIA_DELIMITER)
	alp_data = get_alp_data(ALP_ID_INDEX, ALP_SCORE_INDEX, ALP_DELIMITER)
	match = 0
	missing = 0
	different = 0
	#print str(leticia_data.keys())
	#print alp_data.keys()
	for key in leticia_data:
		if key in alp_data:
			if alp_data[key] == leticia_data[key]:
				match += 1
			else:
				different += 1
		else:
			missing += 1
	print 'Matches: ' + str(match)
	print 'Missing: ' + str(missing)
	print 'Different: ' + str(different)

def get_leticia_data(id_index, score_index, delimiter):
	edges = dict()
	files = [f for f in os.listdir(LETICIA_DIR)]
	for f in files:
		file_name = LETICIA_DIR + '/' + f
		in_file = open(file_name, 'r')
		print 'Processing file ' + f + '...'
		process_file(edges, in_file, id_index, score_index, delimiter, True)
	return edges

def get_alp_data(id_index, score_index, delimiter):
	edges = dict()
	in_file = gzip.open(ALP_FILE, 'rb')
	process_file(edges, in_file, id_index, score_index, delimiter, False)
	return edges


def process_file(edge_map, in_file, id_index, score_index, delimiter, score_correction):
	first_line = True
	inconsistency = False
	for line in in_file:
		if first_line:
			first_line = False
		else:
			data = line.strip().split()
			id1 = data[id_index].split('.')[-1]
			id2 = data[id_index + 1].split('.')[-1]
			score = int(float(data[score_index]) * 1000) if score_correction else int(data[score_index])
			key = (id1, id2) if id1 < id2 else (id2, id1)
			if key in edge_map and edge_map[key] != score:
				print 'INCONSITENCY DETECTED for key ' + str(key) + '. Scores ' + str(score) + ' & ' + str(edge_map[key])
				inconsistency = True
			else:
				edge_map[key] = score
	in_file.close()
	if not inconsistency:
		print 'No inconsistency detected.'

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   run()
