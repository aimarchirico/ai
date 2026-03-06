import keras


def load_mnist():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Normalize the input data - MNIST data is pixel arrays, so divide by max pixel value 255
    x_train = x_train/255.0
    x_test = x_test/255.0

    # Output is categorical - map from digit target to vector (e.g. 2 -> [0,0,1,0,0,0,0,0,0,0])
    y_train = keras.utils.to_categorical(y_train, num_classes=10)
    y_test = keras.utils.to_categorical(y_test, num_classes=10)

    return x_train, y_train, x_test, y_test


def build_model(cnn=True):

    model = keras.Sequential()

    # Input is 28x28 image, single channel (grayscale)
    model.add(keras.Input(shape=(28, 28, 1)))

    if not cnn:

        ###  Fully connected neural network ###

        # Input is multidimensional, flattened to single dimension
        model.add(keras.layers.Flatten())
        # Hidden layers with dropout to reduce overfitting
        model.add(keras.layers.Dense(units=256, activation="relu"))
        model.add(keras.layers.Dropout(0.3))
        model.add(keras.layers.Dense(units=128, activation="relu"))
        model.add(keras.layers.Dropout(0.3))

    else:

        ###  Convolutional neural network  ###

        # First convolutional block
        model.add(keras.layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same"))
        # Add pooling layer to downscale (MaxPooling downscales by returning the maximum value in each input window)
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))
        # Second convolutional block with more filters to capture higher-level spatial features
        model.add(keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        # Flatten internal dimensions before output
        model.add(keras.layers.Flatten())
        # Dense layer to combine extracted features before classification
        model.add(keras.layers.Dense(units=128, activation="relu"))
        model.add(keras.layers.Dropout(0.5))

    # Final model layer - the same for all model architectures
    # Activation is softmax
    model.add(keras.layers.Dense(units=10, activation="softmax"))

    return model



if __name__ == "__main__":

    keras.utils.set_random_seed(3)

    x_train, y_train, x_test, y_test = load_mnist()

    print("Fully Connected Network (MLP)")
    mlp_model = build_model(cnn=False)
    mlp_optimizer = keras.optimizers.Adam(learning_rate=0.001)
    mlp_model.compile(optimizer=mlp_optimizer, loss="categorical_crossentropy", metrics=['accuracy'])
    mlp_model.summary()
    mlp_model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=1, validation_split=0.1)
    mlp_loss, mlp_acc = mlp_model.evaluate(x_test, y_test, verbose=1)
    print(f"MLP  - Test loss: {mlp_loss:.4f}  |  Test accuracy: {mlp_acc:.4f}")

    print("\nConvolutional Neural Network (CNN)")
    cnn_model = build_model(cnn=True)
    cnn_optimizer = keras.optimizers.Adam(learning_rate=0.001)
    cnn_model.compile(optimizer=cnn_optimizer, loss="categorical_crossentropy", metrics=['accuracy'])
    cnn_model.summary()
    cnn_model.fit(x_train, y_train, epochs=10, batch_size=128, verbose=1, validation_split=0.1)
    cnn_loss, cnn_acc = cnn_model.evaluate(x_test, y_test, verbose=1)
    print(f"CNN  - Test loss: {cnn_loss:.4f}  |  Test accuracy: {cnn_acc:.4f}")
