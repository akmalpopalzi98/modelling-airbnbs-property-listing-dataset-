# Modelling AirBnB property listing

> Property dataset from AirBnB is collected from an AWS S3 bucket and stored for preparation. The dataset contains property details and images which will need to be processed before feeding into machine learning models.

## Milestone 1

- Data is loaded onto local machines after extraction from S3 bucket in the cloud. Tools such as Boto3 and AWS CLI were used to interact with AWS services using python.

- Once extracted, both image and tabular data underwent preprocessing steps. Image data was formated so that all images have the same aspect ratio. Packages such as cv2 and PIL were used to deal with image formatting.


