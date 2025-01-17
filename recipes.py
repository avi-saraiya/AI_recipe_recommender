from index_mapper import name_ingredient

test_dataset = [{"dish_name": "Fruit salad", "test_ingredients": ["apple", "orange"], "cuisine": "international"}]

def check_dataset():
    ingredient = name_ingredient()
    for dish in test_dataset:
        if ingredient in dish["test_ingredients"]:
            print("dish found!")
        else:
            print ("dish not found")

if __name__ == "__main__":
    check_dataset()

