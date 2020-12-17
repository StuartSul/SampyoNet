import os
import sys
import csv
import pandas as pd
from PIL import Image
from PIL import ImageStat

# modify root_dir according to your repo
root_dir = '/home/stuartsul/J6-Sampyo_SediNet'

gravel_dir_temp = root_dir+'/temp_images/gravel'
sand_dir_temp = root_dir+'/temp_images/sand'
image_dir = root_dir+'/images'

#brightness threshold
thr = 20
#brightness function
def brightness (im_file):
    try:
        im = im_file.convert('L')
        stat = ImageStat.Stat(im)
        return stat.mean[0]
    except IOError:
        print(im_file + "IOError")
        return 0

# show status data
total_num = 0
processed_num = 0
deleted_num = 0

if(sys.argv[1] == "gravel") or (sys.argv[1] == "both"):
    gravel_image_list = os.listdir(gravel_dir_temp)

    gravel_rawdata = pd.read_csv(root_dir+"/data/gravel-dist-rawdata.csv", encoding='utf-8')
    fg_csv = open(root_dir+'/data/gravel.csv','a')
    g_csv = csv.writer(fg_csv)

    for image in gravel_image_list:
        print("image: " + image)
        total_num = total_num + 1

        # rename image : "RAW-OS-GXXX-XX.jpg" -> "BIG-OS-GXXX-XX.jpg"
        NEW = image.split('-')[0]
        if(NEW != "RAW"):
            continue
        LOC = image.split('-')[1]
        NAME = image.split('-')[2]
        NUM = image.split('-')[3]
        new_name = '/BIG-'+LOC+'-'+NAME+'-'+NUM

        # delete tilted image
        NUMBER = NUM.split('.')[0]
        if(NUMBER.isdigit()):
            if(int(NUMBER)%8>=5 or int(NUMBER)%8==0):
                deleted_num = deleted_num + 1
                print(str(deleted_num) + " : deleted due to tilted : " + image)
                os.remove(gravel_dir_temp+'/'+image)
                continue

        # write csv files for images
        temp_line = gravel_rawdata.loc[gravel_rawdata['fac'].str.contains(LOC, na=False)]
        data_line = temp_line.loc[temp_line['no'].str.contains(NAME, na=False)]

        # if no data is in gravel-dist-rawdata.csv
        if (data_line.empty):
            deleted_num = deleted_num + 1
            print(str(deleted_num) + " : deleted due to no data : " + image)
            os.remove(gravel_dir_temp+'/'+image)
            continue

        # open image and check its size
        # crop image and save it in image directory
        # delete RAW image
        try:
            img = Image.open(gravel_dir_temp+'/'+image)
            img_size = img.size
            if(img_size[0] <3500 or img_size[1] < 2350):
                deleted_num = deleted_num +1
                print(str(deleted_num) + " : deleted due to size : " + image)
                os.remove(gravel_dir_temp+'/'+image)
                continue

            # crop image
            area = (500, 650, 3500, 2350) # cropped area
            if(img_size[0] < img_size[1]):
                img_rotate = img.rotate(90,expand=True)
                crop_image = img_rotate.crop(area)
            else:
                crop_image = img.crop(area)
            
            # delete dark image
            br = brightness(crop_image)
            if(br <= thr):
                deleted_num = deleted_num + 1
                print(str(deleted_num) + " : deleted due to brightness : " + image)
            else:
                processed_num = processed_num + 1
                crop_image.save(image_dir+new_name)
                g_csv.writerow(['images'+new_name,data_line.iat[0,2],data_line.iat[0,3],data_line.iat[0,4],data_line.iat[0,5],data_line.iat[0,6],data_line.iat[0,7],data_line.iat[0,8],data_line.iat[0,9],data_line.iat[0,10],data_line.iat[0,11],data_line.iat[0,12]])
            
            # delete original RAW image in temp_images directory
            os.remove(gravel_dir_temp+'/'+image)
        except IOError:
            deleted_num = deleted_num + 1
            print(str(deleted_num) + " : deleted due to IOError : " + image)
            os.remove(gravel_dir_temp+'/'+image)
            continue

        if(total_num%100==0):
            print("total : " + str(total_num))
            print("processed : " +str(processed_num))
            print("deleted : " + str(deleted_num))



    fg_csv.close()
