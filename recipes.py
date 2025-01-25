import openai
from index_mapper import name_ingredient

# Replace with YOUR OpenAI API key
openai.api_key = "Enter your API key"


def recommend_dish(ingredient):
    try:
        messages = [ # This is to establish the context of the conversation for the AI model
            {"role": "system", "content": "You are a helpful chef who suggests dishes based on ingredients."},
            {"role": "user", "content": f"I have the ingredient '{ingredient}'. Can you suggest some dishes I can make with it?"}
        ]

        # Calls the AI model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7 # This is a scale out of 1.0 where 1 is the maximum degree of creativity, and 0 is the maximum preciseness
        )

        # Extract and print the response
        suggestions = response['choices'][0]['message']['content'].strip()
        print("\nRecommended dishes:")
        print(suggestions)
        return suggestions

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    ingredient = name_ingredient()
    if ingredient and ingredient != "No ingredient found":
        recommend_dish(ingredient)
if __name__ == "__main__":
    main()
