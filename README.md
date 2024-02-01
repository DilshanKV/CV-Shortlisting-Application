<h1>CV Shortlisting App</h1>

<h2>Introduction</h2>
<p>This Streamlit application allows you to shortlist candidates based on their resumes (CVs) by comparing them to a provided job description. The app extracts relevant information from the CVs, computes a similarity score between each CV and the job description, and presents the top candidates based on this score.</p>

<h2>Installation</h2>

<h3>Requirements</h3>
<ul>
    <li>Python 3.6 or later</li>
    <li>pip (package installer for Python)</li>
</ul>

<h3>Steps</h3>
<ol>
    <li>Clone the repository:</li>
    <code>git clone https://github.com/yourusername/cv_shortlisting_app.git</code>
    <li>Change directory to the project folder:</li>
    <code>cd cv_shortlisting_app</code>
    <li>Install the required packages:</li>
    <code>pip install -r requirements.txt</code>
</ol>

<h2>Usage</h2>

<ol>
    <li>Run the Streamlit app:</li>
    <code>streamlit run app.py</code>
    <li>Open the app in your browser by following the link displayed in the terminal.</li>
    <li>Provide the job description in the text area.</li>
    <li>Upload multiple CV files (in PDF format) using the file uploader.</li>
    <li>Select the number of candidates you want to shortlist.</li>
    <li>Click the "Extract Data" button.</li>
    <li>View the extracted data and the shortlisted candidates with their similarity scores.</li>
</ol>

<h2>Model Information</h2>
<p>The app uses the Sentence Transformers library with the 'all-MiniLM-L6-v2' pre-trained model for calculating the similarity scores between the job description and CVs.</p>

<h2>Notes</h2>
<ul>
    <li>Ensure that the CVs are in PDF format for proper extraction of information.</li>
    <li>The app displays the extracted data and the top candidates based on the similarity score.</li>
    <li>The extracted data includes information such as Name, Email, Phone, LinkedIn, GitHub, Summary, Education, Internships, Professional Experience, Projects, Awards and Certifications, and Skills.</li>
</ul>

<p>Feel free to customize the app according to your specific needs and preferences.</p>
