# -*- coding: utf-8 -*-
"""Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QUaW8xSQGBhRV0OT-BhzMAg4KamJo20I
"""

!pip install openai

"""Import the required libraries and set up the OpenAI API key:"""

import openai

# Set your OpenAI GPT-3 API key here
api_key = "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"
openai.api_key = api_key

"""Task: Accept Job Description and Multiple CVs
Assuming the user provides the job description and uploads CVs, store them in variables for further processing.
"""

# Example job description and CVs
job_description = "Job description content..."
cvs = ['cv1.pdf', 'cv2.docx', 'cv3.txt']  # List of CV file names

"""Task: Job Description Evaluation
Use ChatGPT to score the job description based on the job title and provide recommendations for enhancements.
"""

# Function to evaluate job description using ChatGPT
def evaluate_job_description(description):
    prompt = f"Evaluate the job description: {description}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=api_key
    )
    evaluation = response['choices'][0]['text'].strip()
    return evaluation

"""Task: User Interaction for Job Description
Ask the user if they would like to continue with the original version or incorporate the suggested changes to the job description.
"""

# Function for user interaction regarding job description
def job_description_interaction(description):
    print("Job Description Evaluation:")
    print(evaluate_job_description(description))
    print("\nDo you want to incorporate the suggested changes?")
    user_response = input("Type 'yes' or 'no': ")
    return user_response.lower() == 'yes'

"""Task: CV Ranking and Shortlisting
Use ChatGPT to rank the CVs according to their alignment with the job requirements and shortlist candidates based on the rankings.
"""

# Function to rank and shortlist CVs using ChatGPT
def rank_and_shortlist_cvs(job_description, cvs):
    ranked_cvs = []

    for cv in cvs:
        prompt = f"Rank the CV based on its alignment with the job requirements: CV: {cv}, Job Description: {job_description}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=api_key
        )
        cv_score = float(response['choices'][0]['text'].strip())
        ranked_cvs.append((cv, cv_score))

    # Sort the CVs based on their scores (higher score indicates better alignment)
    ranked_cvs.sort(key=lambda x: x[1], reverse=True)

    # Shortlist candidates (top 5 CVs in this example)
    shortlisted_candidates = [cv_info[0] for cv_info in ranked_cvs[:5]]

    return shortlisted_candidates

"""Task: Additional Information on Shortlisted Candidates
Use ChatGPT to provide additional information or insights about the shortlisted candidates.
"""

# Function to get additional information on shortlisted candidates using ChatGPT
def additional_info_on_candidates(shortlisted_candidates):
    candidate_info = {}
    for candidate in shortlisted_candidates:
        prompt = f"Provide additional information about candidate: {candidate}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=api_key
        )
        candidate_info[candidate] = response['choices'][0]['text'].strip()
    return candidate_info

"""Task: Email Notifications
Use ChatGPT to generate personalized email notifications for the shortlisted candidates.
"""

# Function to generate email notifications using ChatGPT
def generate_email_notifications(shortlisted_candidates):
    email_content = {}
    for candidate in shortlisted_candidates:
        prompt = f"Generate email notification for shortlisted candidate: {candidate}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=api_key
        )
        email_content[candidate] = response['choices'][0]['text'].strip()
    return email_content

"""Task: Screening Questions
Use ChatGPT to develop screening questions for each candidate, considering different levels of importance assigned to the job description and the candidate's CV.
"""

# Function to develop screening questions for candidates using ChatGPT
def develop_screening_questions(job_description, cv, importance_level):
    prompt = f"Develop screening questions for candidate CV: {cv} for job description: {job_description}, considering importance level: {importance_level}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=api_key
    )
    screening_questions = response['choices'][0]['text'].strip().split('\n')
    return screening_questions

"""Task: First-Round Interview
Use ChatGPT to conduct the first-round interview, record the candidate's responses to the screening questions, and evaluate their performance for consideration in the next in-person round.
"""

# Function to conduct the first-round interview using ChatGPT
def first_round_interview(candidate_name, screening_questions):
    print(f"Conducting the first-round interview for candidate: {candidate_name}")
    responses = {}
    for question in screening_questions:
        response = input(f"{question} ")
        responses[question] = response
    return responses

"""Task: Communication with HR Team
Use ChatGPT to maintain continuous communication with the HR team, providing updates on the hiring process and relevant information.
"""

# Function for communication with HR team using ChatGPT
def communicate_with_hr_team(update_message):
    prompt = f"Update message for HR team: {update_message}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        api_key=api_key
    )
    communication_response = response['choices'][0]['text'].strip()
    return communication_response

"""Putting it all together:"""

def main():
    # Task: Accept Job Description and Multiple CVs
    # job_description and cvs variables already provided in the outline above

    # Task: Job Description Evaluation
    continue_with_original = job_description_interaction(job_description)

    # Task: CV Ranking and Shortlisting
    shortlisted_candidates = rank_and_shortlist_cvs(job_description, cvs)

    # Task: Additional Information on Shortlisted Candidates
    candidate_info = additional_info_on_candidates(shortlisted_candidates)

    # Task: Email Notifications
    email_content = generate_email_notifications(shortlisted_candidates)

    # Task: Screening Questions
    for candidate in shortlisted_candidates:
        importance_level = 5  # Importance level for this candidate (example)
        screening_questions = develop_screening_questions(job_description, candidate, importance_level)
        candidate_responses = first_round_interview(candidate, screening_questions)
        print(f"{candidate}'s Responses: {candidate_responses}")

    # Task: Communication with HR Team
    hr_update = "First-round interviews completed. Proceeding to the next round."
    communication_response = communicate_with_hr_team(hr_update)
    print("HR Team Response:", communication_response)

if __name__ == "__main__":
    main()