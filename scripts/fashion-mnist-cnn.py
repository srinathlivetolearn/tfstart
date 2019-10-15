import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

image_shape = (28, 28, 1)

train_images = train_images / 255.0
test_images = test_images / 255.0

train_images_reshape = train_images.reshape(train_images.shape[0], *image_shape)
test_images_reshape = test_images.reshape(test_images.shape[0], *image_shape)

model = keras.Sequential([
    keras.layers.Conv2D(32, kernel_size=3, activation='relu', input_shape=image_shape, kernel_initializer='he_normal',
                        name='Conv2D-1'),
    keras.layers.MaxPooling2D(pool_size=2, name='MaxPool'),
    keras.layers.Dropout(0.25, name='Dropout-1'),
    keras.layers.Conv2D(64, kernel_size=3, activation='relu', name='Conv2D-2'),
    keras.layers.Dropout(0.25, name='Dropout-2'),
    keras.layers.Conv2D(128, kernel_size=3, activation='relu', name='Conv2D-3'),
    keras.layers.Dropout(0.4, name='Dropout-3'),
    keras.layers.Flatten(name='flatten'),
    keras.layers.Dense(1024, activation='relu', name='Dense'),
    keras.layers.Dropout(0.4, name='Dropout'),
    keras.layers.Dense(10, activation='softmax', name='Output')
])

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_images_reshape, train_labels, batch_size=512, epochs=50)

test_loss, test_accuracy = model.evaluate(test_images_reshape, test_labels)
print('\nTest accuracy: ', test_accuracy)
print('\nTest loss: ', test_loss)

predictions = model.predict(test_images_reshape)


def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel(" {} {:2.0f}% ({})".format(class_names[predicted_label],
                                          100 * np.max(predictions_array),
                                          class_names[true_label]), color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color='#777777')
    plt.ylim(0, 1)
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 10
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
    plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()
