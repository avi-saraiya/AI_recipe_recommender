import json
import requests
from load_model import predict_class

# Acts as a cache
class_idx = None

def load_class_labels():
    global class_idx
    if class_idx is None:
        url = 'https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json' #url that contains the human readable equivalent of the class indices
        response = requests.get(url)
        class_idx = json.loads(response.text)
    return class_idx

def map_class_to_label(class_index):
    # Loads class labels (from the cache)
    class_idx = load_class_labels()
    predicted_class_label = class_idx[str(class_index)][1]
    return predicted_class_label

#Usage
def name_ingredient():
    user_input = ""
    ingredient = ""
    image_path = "orange.png"
    try:
        image_path = input("Please enter the path of the image you want to identify\n")
        class_index = predict_class(image_path)
        class_label = map_class_to_label(class_index)
        print(f"Predicted class index: {class_index}")
        print(f"Predicted class label: {class_label}")
        ingredient = class_label
    except FileNotFoundError:
        print("File was not found")
    if ingredient == "":
        print("This is the ingredient : " + ingredient)
        return "No ingredient found"
    else:
        print("The ingredient is : " + ingredient)
        return ingredient

if __name__ == "__main__":
    name_ingredient()

