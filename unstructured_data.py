import csv
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with unstructured data, and your task is to parse it into CSV format."
    },
    {
      "role": "user",
      "content": "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1
)

# Get the response content
response_text = response.choices[0].message.content

# Example structure from the assistant's response
# This will depend on how the model formats the output, so adjust this part accordingly.
# Here we're assuming the response will be something like:
# "neoskizzles, purple, candy; loheckles, grayish blue, tart; ..."

# Split the response into fruit data
fruit_data = response_text.split(';')

# Create a list to store rows for the CSV file
rows = [["Fruit Name", "Color", "Taste"]]

# Process each piece of fruit data into a row
for fruit in fruit_data:
    fruit_info = fruit.split(',')
    if len(fruit_info) == 3:  # Ensure it has name, color, and taste
        rows.append([fruit_info[0].strip(), fruit_info[1].strip(), fruit_info[2].strip()])

# Write the rows to a CSV file
with open('fruits.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file has been written successfully!")