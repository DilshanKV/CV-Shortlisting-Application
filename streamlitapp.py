import streamlit as st
import pdfplumber
import pandas as pd

from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_information_from_cv(pdf_content):
    with pdfplumber.open(pdf_content) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    return text

def extract_title(text):
    # Extract the title section
    Title_start = text.find("Title:")
    Title_end = text.find("Name:")

    return text[Title_start + len("Title:"):Title_end].strip() if Title_start != -1 and Title_end != -1 else None


def extract_name(text):
    # Extract the name section
    Name_start = text.find("Name:")
    Name_end = text.find("Email:")

    return text[Name_start + len("Name:"):Name_end].strip() if Name_start != -1 and Name_end != -1 else None


def extract_Email(text):
    # Extract the Email section
    Email_start = text.find("Email:")
    Email_end = text.find("Phone:")

    return text[Email_start + len("Email:"):Email_end].strip() if Email_start != -1 and Email_end != -1 else None


def extract_Phone(text):
    # Extract the Phone section
    Phone_start = text.find("Phone:")
    Phone_end = text.find("LinkedIn:")

    return text[Phone_start + len("Phone:"):Phone_end].strip() if Phone_start != -1 and Phone_end != -1 else None


def extract_LinkedIn(text):
    # Extract the LinkedIn section
    LinkedIn_start = text.find("LinkedIn:")
    LinkedIn_end = text.find("GitHub:")

    return text[LinkedIn_start + len("LinkedIn:"):LinkedIn_end].strip() if LinkedIn_start != -1 and LinkedIn_end != -1 else None


def extract_Github(text):
    # Extract the Github section
    Github_start = text.find("GitHub:")
    Github_end = text.find("Summary:")

    return text[Github_start + len("GitHub:"):Github_end].strip() if Github_start != -1 and Github_end != -1 else None


def extract_summary(text):
    summary_start = text.find("Summary:")
    summary_end = text.find("Education:")

    return text[summary_start + len("Summary:"):summary_end].strip() if summary_start != -1 and summary_end != -1 else None


def extract_education(text):
    education_start = text.find("Education:")
    education_end = text.find("Internship:")

    return text[education_start + len("Education:"):education_end].strip() if education_start != -1 and education_end != -1 else None


def extract_Internship(text):
    Internship_start = text.find("Internship:")
    Internship_end = text.find("Professional Experience:")

    return text[Internship_start + len("Internship:"):Internship_end].strip() if Internship_start != -1 and Internship_end != -1 else None

def extract_experience(text):
    exp_start = text.find("Professional Experience:")
    exp_end = text.find("Projects:")

    return text[exp_start + len("Professional Experience:"):exp_end].strip() if exp_start != -1 and exp_end != -1 else None


def extract_projects(text):
    projects_start = text.find("Projects:")
    projects_end = text.find("Awards and Certifications:")

    return text[projects_start + len("Projects:"):projects_end].strip() if projects_start != -1 and projects_end != -1 else None


def extract_certifications(text):
    certifications_start = text.find("Awards and Certifications:")
    certifications_end = text.find("Skills:")

    return text[certifications_start + len("Awards and Certifications:"):certifications_end].strip() if certifications_start != -1 and certifications_end != -1 else None


def extract_skills(text):
    skills_start = text.find("Skills:")
    
    return text[skills_start + len("Skills:"):].strip() if skills_start != -1 else None


def main():
    st.title("CV Shortlisting App")
    job_description = st.text_area('Job description')
    uploaded_files = st.file_uploader("Choose multiple CV files", type="pdf", accept_multiple_files=True)
    options = [i+1 for i in range(len(uploaded_files))]
    no_of_candidates = st.selectbox('No of candidates need:', options)
    if no_of_candidates:
        extract_button = st.button("Extract Data")

    extracted_data = []
    cv_data = []


    if uploaded_files and extract_button:
        for uploaded_file in uploaded_files:
            cv_text = extract_information_from_cv(uploaded_file)

            cv_data.append(cv_text)

            title = extract_title(cv_text)
            name = extract_name(cv_text)
            phone = extract_Phone(cv_text)
            email = extract_Email(cv_text)
            linkedin = extract_LinkedIn(cv_text)
            github = extract_Github(cv_text)
            summary = extract_summary(cv_text)
            education = extract_education(cv_text)
            internship = extract_Internship(cv_text)
            experience = extract_experience(cv_text)
            projects = extract_projects(cv_text)
            certifications = extract_certifications(cv_text)
            skills = extract_skills(cv_text)

            data = {
                "Title": [title],
                "Name": [name],
                "Email": [email],
                "Phone": [phone],
                "LinkedIn": [linkedin],
                "Github": [github],
                "Summary": [summary],
                "Education": [education],
                "Internships":[internship],
                "Professional Experience": [experience],
                "Projects": [projects],
                "Awards and Certifications":[certifications],
                "Skills": [skills]
            }

            extracted_data.append(data)

        # Two lists of sentences
        sentences1 = job_description

        sentences2 = cv_data

        #Compute embedding for both lists
        embeddings1 = model.encode(sentences1, convert_to_tensor=True)
        embeddings2 = model.encode(sentences2, convert_to_tensor=True)

        #Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        Scores = []

        #Output the pairs with their score
        for i in range(len(sentences2)):
            score = cosine_scores[0][i]
            Scores.append(score)

        st.write("### Extracted Data:")
        final_df = pd.DataFrame(extracted_data)
        final_df['Score'] = Scores
        df_sorted = final_df.sort_values(by='Score', ascending=False)

        # Extract information for the top students
        top_cvs = df_sorted.head(no_of_candidates)

        top_cv_list = []
        top_emails = top_cvs['Email'].values

        
        for email in top_emails:
            for cv in cv_data:
                if email[0] in cv:
                    top_cv_list.append(cv) 

        st.write(df_sorted)

        st.subheader(f"Top {no_of_candidates} Candidates's cv")
        st.write(top_cv_list)

if __name__ == "__main__":
    main()