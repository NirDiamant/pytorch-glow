import os

def create_ano_file(images_folder):
    num_images = len(os.listdir(images_folder))
    attributes = 0
    file = open('list_attr_celeba.txt', 'w')
    file.write(str(num_images) + "\n")
    file.write(str(attributes) + "\n")
    for filename in os.listdir(images_folder):
        file.write(os.path.join(images_folder, filename) + ' ' + str(attributes) + "\n")

    file.close()


create_ano_file("/home/nird/glow_pytorch/dataset/Data/CelebA")
