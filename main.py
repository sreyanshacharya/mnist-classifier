import tensorflow as tf
from tensorflow import keras
from keras.losses import SparseCategoricalCrossentropy 

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train/255.0, x_test/255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape = (28,28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

model.evaluate(x_test, y_test, verbose=2)

#model.save('mnist_breadv1.keras')
#commented the above line so it doesnt save the model every time the script is run.
#feel free to de-comment if any tweaks have been made to the model to save it as your own.



