##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import argparse
from time import time

from fnc.extractFeature import extractFeature
from fnc.matching import matching


#------------------------------------------------------------------------------
#	Argument parsing
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str,
                    help="../CASIA1/")

parser.add_argument("--temp_dir", type=str, default="./templates/CASIA1/",
					help="./templates/CASIA1/")

parser.add_argument("--thres", type=float, default=0.38,
					help="Threshold for matching.")

args = parser.parse_args()


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
# Extract feature
start = time()
print('>>> Start verifying {}\n'.format(args.file))
template, mask, file = extractFeature(args.file)


# Matching
result = matching(template, mask, args.temp_dir, args.thres)

if result == -1:
	print('>>> No registered sample.')

elif result == 0:
	print('>>> No sample matched.')

else:
	print('>>> {} samples matched (descending reliability):'.format(len(result)))
	for res in result:
		print("\t", res)


# Time measure
end = time()
print('\n>>> Verification time: {} [s]\n'.format(end - start))