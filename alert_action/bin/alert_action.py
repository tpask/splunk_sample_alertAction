#sample alert_action script


import json, sys
import shutil
import gzip

work_dir = '/tmp'
unzipped_file = "%s/unzipped_file.csv" %work_dir

def printfile(file):
	with open(file, 'r') as f:
    		print(f.read())

if __name__ == "__main__":
	payload=json.loads(sys.stdin.read())
	zipped_file = payload["results_file"]
	#print zipped_file
	try:
		with gzip.open(zipped_file, 'rb') as zf, open(unzipped_file, 'w') as uzf:
			shutil.copyfileobj(zf, uzf)
		#printfile(unzipped_file)
	except:
		sys.exit(1)

