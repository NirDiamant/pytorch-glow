import os
from PIL import Image
from matplotlib import pyplot as plt

def create_ano_file(images_folder):
    num_images = len(os.listdir(images_folder))
    attributes = 0
    file = open('list_attr_celeba.txt', 'w')
    file.write(str(num_images) + "\n")
    file.write(str(attributes) + "\n")
    for filename in os.listdir(images_folder):
        file.write(os.path.join(images_folder, filename) + ' ' + str(attributes) + "\n")

    file.close()
images_folder = "/home/nird/glow_pytorch/dataset/Data/CelebA"
create_ano_file(images_folder)
# path = "C:\studies\BSc\semester_11\GANS\datasets\celebahq"
#
# def check_num_channel_of_image(image_folder):
#     all_images = os.listdir(image_folder)
#     for image in all_images:
#         img = plt.imread(os.path.join(image_folder,image))
#         if img.shape[2] < 3:
#             print(img.shape)
#
# check_num_channel_of_image(path)
