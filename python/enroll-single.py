##-----------------------------------------------------------------------------
##  Import
##-----------------------------------------------------------------------------
import argparse, os
from time import time
from scipy.io import savemat

from fnc.extractFeature import extractFeature


#------------------------------------------------------------------------------
#	Argument parsing
#------------------------------------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--file", type=str,
                    help="/home/aju/Iris-Recognition/CASIA1/")

parser.add_argument("--temp_dir", type=str, default="./templates/temp/",
					help="Path to the directory containing templates.")

args = parser.parse_args()


##-----------------------------------------------------------------------------
##  Execution
##-----------------------------------------------------------------------------
start = time()
#args.file = "../CASIA1/001_1_1.jpg"

# Check the existence of temp_dir
if not os.path.exists(args.temp_dir):
	print("makedirs", args.temp_dir)
	os.makedirs(args.temp_dir)

# Extract feature
print('>>> Enroll for the file ', args.file)
template, mask, file = extractFeature(args.file)

# Save extracted feature
basename = os.path.basename(file)
out_file = os.path.join(args.temp_dir, "%s.mat" % (basename))
savemat(out_file, mdict={'template':template, 'mask':mask})
print('>>> Template is saved in %s' % (out_file))

end = time()
print('>>> Enrollment time: {} [s]\n'.format(end-start))