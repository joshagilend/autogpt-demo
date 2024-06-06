import openai
import json

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def call_openai_api(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-4o",  # Use the appropriate engine for your needs
            prompt=prompt,
            max_tokens=150  # Adjust the max tokens as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def save_response_to_file(response, filename):
    try:
        with open(filename, 'w') as file:
            file.write(response)
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    user_prompt = "Write a short story about a time traveler who falls in love with a person from the past."
    api_response = call_openai_api(user_prompt)
    output_filename = "output.txt"
    
    save_response_to_file(api_response, output_filename)
    print(f"Response saved to {output_filename}")
