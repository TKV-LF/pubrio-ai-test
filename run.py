import openai
import json
import re

# Set your OpenAI API key
openai.api_key = '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'

def extract_companies_from_text(text):
	prompt = (
		"Extract relevant companies from the given text:\n\n"
		f"Text: '{text}'\n\n"
		"Relevant companies: Bloomberg, Reuters, Fortune\n\n"
		"Extract relevant companies from the text:\n"
		"result need to return json with the following structure:\n"
		"'related_companies':  [{'company_name':'X', 'company_domain':'x.com' }, {'company_name':'Bloomberg', 'company_domain':'bloomberg.com' }], 'topic':'X is launching two new subscription tiers, including a 'Premium+' ad-free plan'"
	)
	

	response = openai.Completion.create(
	model="gpt-3.5-turbo-instruct",
	prompt=prompt,
	max_tokens=200,
)
	
	extracted_text = response.choices[0].text.strip()
	return extracted_text

# Read the content from the file
with open('input.txt', 'r') as file:
	text = file.read()

clean_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
clean_text = clean_text.strip()  # Remove leading/trailing spaces

# Extract relevant companies using the function
relevant_companies = extract_companies_from_text(clean_text)