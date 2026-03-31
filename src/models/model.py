import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(tabular_input_shape):
    
    # 🔵 Image branch (CNN)
    image_input = layers.Input(shape=(128, 128, 3))

    x = layers.Conv2D(32, (3,3), activation='relu')(image_input)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Flatten()(x)

    # 🟢 Tabular branch
    tabular_input = layers.Input(shape=(tabular_input_shape,))
    y = layers.Dense(64, activation='relu')(tabular_input)
    y = layers.Dense(32, activation='relu')(y)

    # 🔶 Combine
    combined = layers.concatenate([x, y])

    z = layers.Dense(64, activation='relu')(combined)
    z = layers.Dense(1)(z)  # output (price)

    model = models.Model(inputs=[image_input, tabular_input], outputs=z)

    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )

    return model