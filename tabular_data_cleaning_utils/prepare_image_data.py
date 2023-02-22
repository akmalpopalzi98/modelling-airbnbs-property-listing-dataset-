import boto3
import os
import cv2
import PIL
from PIL import Image


class ImageProcessing:
    def __init__(self):
        self.resource = boto3.resource('s3')
        self.my_bucket = self.resource.Bucket('airbnbimage')
        self.folder_names = []
        self.file_names = []
        self.height = []
        self.width = []
        


    def get_folder_names(self):
        for file in self.my_bucket.objects.filter(Prefix = 'images/'):
            if file.key.split('/')[1] not in self.folder_names:
                self.folder_names.append(file.key.split('/')[1])

    def get_file_names(self):
        for file in self.my_bucket.objects.filter(Prefix = 'images/'):
            self.file_names.append(file.key)

    def download_images(self):
        working_dir = '/Users/akmalpopalzi/Documents/S3images/'
        for folder in self.folder_names:
            path = os.path.join(working_dir,folder)
            os.mkdir(path)

        for image in self.file_names:
            lst = image.split('/')
            self.my_bucket.download_file(Key = image, Filename= f'/Users/akmalpopalzi/Documents/S3images/{lst[1]}/{lst[2]}')

    def get_image_details(self):
        for image2 in self.file_names:
            lst2 = image2.split('/')
            img = Image.open(f'/Users/akmalpopalzi/Documents/S3images/{lst2[1]}/{lst2[2]}')
            self.width.append(img.width)
            self.height.append(img.height)

    def min_height(self):
        return min(self.height)
    

    def resize_images(self):
        fixed_height = self.min_height()
        working_dir = '/Users/akmalpopalzi/Documents/airbnb_processed_images/'
        for folder in self.folder_names:
            path = os.path.join(working_dir,folder)
            os.mkdir(path)

        for file in self.file_names:
            lst3 = file.split('/')
            path = f'/Users/akmalpopalzi/Documents/S3images/{lst3[1]}/{lst3[2]}'
            img2 = cv2.imread(path)
            original_height = img2.shape[0]
            original_width = img2.shape[1]
            scale_percent = fixed_height/original_height
            resized_width = int(original_width*scale_percent)
            resized_img = cv2.resize(img2,(resized_width,fixed_height),interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'/Users/akmalpopalzi/Documents/airbnb_processed_images/{lst3[1]}/{lst3[2]}',resized_img)


    


    


