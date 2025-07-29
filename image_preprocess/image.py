def show_image(image):
    import numpy as np
    if image.dtype == np.float32:
        image = np.uint8(image * 255)

    if image.shape[0] == 3:
        image = np.transpose(image, (1, 2, 0))

    import matplotlib.pyplot as plt
    plt.figure(figsize=(20, 20))
    plt.axis('off')
    plt.imshow(image)
    plt.show()

def save_image(image, path):
    import numpy as np
    if image.dtype == np.float32:
        image = np.uint8(image * 255)

    if image.shape[0] == 3:
        image = np.transpose(image, (1, 2, 0))

    import PIL.Image as Image
    Image.fromarray(image).save(path)