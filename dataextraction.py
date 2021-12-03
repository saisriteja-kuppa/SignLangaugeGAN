path = 'D:\\projects\\sign langauge\\datasets\\sastra dataset\\ISL_CSLRT_Corpus\\Frames_Sentence_Level'

import glob

import os

print(path + '\\*\\3\\*')

files = glob.glob(path + '\\*\\3\\*')


print(files)




from shutil import copyfile


count = 0



for i in files:
    filename = i.split('\\')[-1]
    dst = os.path.join('D:\\projects\\sign langauge\\codes\\images\\train' , filename )

    if count > 2775 - 400:
            dst = os.path.join('D:\\projects\\sign langauge\\codes\\images\\test' , filename )


    count = count + 1


    copyfile(i, dst)
print(len(files))


