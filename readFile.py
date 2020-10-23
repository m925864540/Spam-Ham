
def read_File_LabelList(filepath):
    labelList=[]
    f=open(filepath, "r")
    
    for line in f:
        labelList.append(line.split(' ', 1)[0])  #put ham and spam into labelList
    toNum(labelList)       #turn label into 0 or 1.
    print(labelList)
    f.close()

def read_File_SampleList(filepath):
    sampleList=[]
    f=open(filepath, "r")
    for lines in f:
        lines=lines.rstrip("\n")
        sampleList.append(lines.split(' ', 1)[1]) #put rest of the sample into sampleList
    print(sampleList)
    f.close()

def toNum(labelList):
    for idx in range(len(labelList)):
        if(labelList[idx]=='spam'):
            labelList[idx]='1'
        else:
            labelList[idx]='0'

read_File_LabelList("textFile.txt")
read_File_SampleList("textFile.txt")