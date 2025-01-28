import json
import requests
from load_model import predict_class
from camera import capture_image

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

    # To generalize specific foods
    generalize = {"Granny_Smith": "apple"} # Add to this as seen fit
    user_input = ""
    ingredients = []
    ingredient = ""
    image = ""

    # Will continuously receive ingredients from user until the user prompts otherwise
    while user_input != "end" and user_input != "no":
        try:
            image = capture_image()
            class_index = predict_class(image)
            class_label = map_class_to_label(class_index)
            print(f"Predicted class index: {class_index}")
            print(f"Predicted class label: {class_label}")

            if class_label in generalize:
                class_label = generalize[class_label]

            ingredient = class_label
            ingredients.append(ingredient)

        except FileNotFoundError:
            print("File was not found")

        user_input = input("Would you like to continue adding ingredients?\n")

    if len(ingredients) == 0:
        return "No ingredient found"
    else:
        print("The ingredients are : ")
        for element in ingredients:
            print(element)
    return ingredients


if __name__ == "__main__":
    name_ingredient()

