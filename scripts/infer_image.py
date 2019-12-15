from keras_preprocessing.image import load_img, img_to_array
from tensorflow import keras
import sys

imagepath = sys.argv[1];

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

image_shape = (28, 28, 1)

train_images = train_images / 255.0
test_images = test_images / 255.0

train_images_reshape = train_images.reshape(train_images.shape[0], *image_shape)
test_images_reshape = test_images.reshape(test_images.shape[0], *image_shape)

model = keras.models.load_model('../models/fashion_mnist_50_epochs.h5')


# load and prepare the image
def load_image(filename):
    image = load_img(filename, color_mode="grayscale", target_size=(28, 28))
    image = img_to_array(image)
    image = image.reshape(1, 28, 28, 1)
    image = image.astype('float32')
    image = image / 255.0
    return image


# predict test input
img = load_image(imagepath)
res = model.predict_classes(img)
print('{"class":"%s"}' % class_names[res[0]])
