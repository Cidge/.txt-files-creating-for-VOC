import os
path = './Annotations'		#annotations dir
curDir = sys.path[0]		#current dir
preDir = "./ImageSets/Main/"	#a pre-dir for Main, if it doesn't exits create it
filelist = os.listdir(path)	#Get all file of Annotations
count = 0;			#Rate control for test and trainval
count2 = 0;			#Rate Control for train and val

try:				
	os.stat(preDir)
except:
	os.mkdir(preDir)

test = open('./ImageSets/Main/test.txt','w')
train = open('./ImageSets/Main/train.txt','w')
trainval = open('./ImageSets/Main/trainval.txt','w')
val = open('./ImageSets/Main/val.txt','w')

for files in filelist:
	lastdir = os.path.join(path,files)
	if os.path.isdir(lastdir):
		continue;
	filename = os.path.splitext(files)[0]
	if count%2 == 0:
		trainval.writelines(filename+'\n');
		if count2%2 == 0:
			train.writelines(filename+'\n')
		else:
			val.writelines(filename+'\n')
		count2=count2+1
	else:
		test.writelines(filename+'\n');
	print filename
	count=count+1

test.close()
train.close()
trainval.close()
val.close()
