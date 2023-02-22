import boto3
import os


class ImageProcessing:
    def __init__(self):
        self.resource = boto3.resource('s3')
        self.my_bucket = self.resource.Bucket('airbnbimage')
        self.folder_names = []
        self.file_names = []


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


    


