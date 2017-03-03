# Test-txt-files-for-Pascal-Vol
This is a simple python program for the four .txt file in ImageSets/Main document creating, which is used to build your train sets for Faster R-CNN.\n
The proportion of each part of sets should be：\n

test: 50% of all \n
trainval: 50% of all \n
train: 50% of trainval \n
val: 50% of trainval \n

This program is fully automatic which means it will read the content of Annotations of current dir and create needed dir or file and fill the .txt file.\n

这是一个帮助创建faster R-CNN 自用训练集的程序。\n
他会帮助你建立好在ImageSets/Main下的四个txt文件： test,trainval,train,val，并且按照规定的比例分配。
