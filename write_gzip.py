
import gzip
import os

from compare_data import LETICIA_DIR, LETICIA_ID_INDEX, LETICIA_SCORE_INDEX, LETICIA_DELIMITER, ALP_DELIMITER, process_file

OUT_FILE = '9606.protein.links.detailed_FAKE.v10.txt.gz'
PROT_PREFIX = '9606.'

def run():
	edges = dict()
	files = [f for f in os.listdir(LETICIA_DIR)]
	for f in files:
		file_name = LETICIA_DIR + '/' + f
		in_file = open(file_name, 'r')
		print 'Processing file ' + f + '...'
		process_file(edges, in_file, LETICIA_ID_INDEX, LETICIA_SCORE_INDEX, LETICIA_DELIMITER, True)
	out_file = gzip.open(OUT_FILE, 'wb')
	to_write = ['Ignore this line']
	for key in edges:
		prot1 = PROT_PREFIX + key[0]
		prot2 = PROT_PREFIX + key[1]
		to_write.append(ALP_DELIMITER.join([key[0], key[1], '0', '0', '0', '0', '0', '0', '0', str(edges[key])]))
	out_file.write('\n'.join(to_write))
	out_file.close()

run()