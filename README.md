# Test-txt-files-for-Pascal-Vol
This is a simple python programe for the name collection of the test data prepation of Faster R-CNN.

In ImageSets/Main document.

The proportion of each part of sets should be：

test: 50% of all
trainval: 50% of all
train: 50% of trainval
val: 50% of trainval

It will read the content of annotations and create the dir automatically in current dir.

这是一个帮助创建faster R-CNN 自用训练集的程序。他会帮助你建立好在ImageSets/Main下的四个txt文件： test,trainval,train,val，并且按照规定的比例分配。
