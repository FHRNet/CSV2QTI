import argparse
from CSVImporter import CSVImporter
import xmlGenerator
import os
import shutil

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
description=
"""Create zip with xml which are ready to be imported in TAO
Only one category per file supported!
CSV Format: ID;Otazka;Kategorie;Spravne;Spatne1;Spatne2;Spatne3;Spatne4;Obrazek;
""")
parser.add_argument('csv', metavar='csv', help='csv file to be converted')
parser.add_argument('output', metavar='output', help='Export filename')

args = parser.parse_args()
questions = CSVImporter(";").getQuestions(args.csv)

prefix = ""

if not os.path.exists(args.output):
	os.makedirs(args.output)
if not os.path.exists(args.output + '/' + args.output):
	os.makedirs(args.output + '/' + args.output)

for i in range(0, len(questions)):
	item_id = '%02d' % i
	if prefix == "":
		prefix = questions[i].category
	else:
		if prefix != questions[i].category:
			print("ERROR! Multiple categories in the input detected.")
			print("Please split the input file so it contains only one category.")
			exit(1)
	questions[i].title = prefix + "_" + questions[i].id
	questions[i].title_id = questions[i].title.lower()
	questions[i].question = questions[i].question + ' [' + questions[i].title + ']'
	xmlGenerator.saveXML(questions[i], args.output + '/' + args.output + '/' + questions[i].title + '.xml')

xmlGenerator.generateManifest(args.output, prefix + "_pack")
print "%d items generated!" % len(questions)
shutil.make_archive(args.output, 'zip', args.output)
shutil.rmtree(args.output, ignore_errors=True)
