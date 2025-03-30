
import streamlit as st
import json
import boto3
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize AWS Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

# User database simulation (in production, use a real database)
if 'users_db' not in st.session_state:
    st.session_state.users_db = {}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Authentication functions
def create_account(username, password):
    if username in st.session_state.users_db:
        return False
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    st.session_state.users_db[username] = {
        'password_hash': hashed_pw,
        'profile_complete': False
    }
    return True

def login(username, password):
    if username not in st.session_state.users_db:
        return False
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if st.session_state.users_db[username]['password_hash'] == hashed_pw:
        st.session_state.current_user = username
        return True
    return False

# Profile management
def save_profile(role, salary, location, skills, experience, education):
    st.session_state.user_data = {
        "current_role": role,
        "current_salary": salary,
        "location": location,
        "skills": skills,
        "years_experience": experience,
        "education": education
    }
    st.session_state.users_db[st.session_state.current_user]['profile_complete'] = True

# App layout
st.set_page_config(layout="wide", page_title="AI Career Navigator", page_icon="💼")

# Authentication sidebar
with st.sidebar:
    st.title("Account")
    
    if st.session_state.current_user is None:
        # Login/Signup form
        auth_tab = st.radio("", ["Login", "Sign Up"])
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if auth_tab == "Login":
            if st.button("Login"):
                if login(username, password):
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid credentials")
        else:
            if st.button("Create Account"):
                if create_account(username, password):
                    st.success("Account created! Please login.")
                else:
                    st.error("Username already exists")
    else:
        # Profile management
        st.success(f"Welcome, {st.session_state.current_user}!")
        if st.button("Logout"):
            st.session_state.current_user = None
            st.rerun()
        
        # Profile edit form
        with st.expander("Edit Profile"):
            role = st.selectbox(
                "Current Role",
                options=['Data Scientist', 'Software Engineer', 'Data Analyst', 
                        'ML Engineer', 'Product Manager', 'DevOps Engineer'],
                index=0 if 'current_role' not in st.session_state.user_data else None,
                key='profile_role'
            )
            
            salary = st.number_input(
                "Current Salary ($)",
                min_value=30000,
                max_value=500000,
                value=90000 if 'current_salary' not in st.session_state.user_data else st.session_state.user_data['current_salary'],
                step=5000,
                key='profile_salary'
            )
            
            location = st.selectbox(
                "Location",
                options=['Austin, TX', 'San Francisco, CA', 'New York, NY', 
                        'Chicago, IL', 'Seattle, WA', 'Remote'],
                index=0 if 'location' not in st.session_state.user_data else None,
                key='profile_location'
            )
            
            experience = st.slider(
                "Years of Experience",
                min_value=0,
                max_value=30,
                value=3 if 'years_experience' not in st.session_state.user_data else st.session_state.user_data['years_experience'],
                key='profile_experience'
            )
            
            skills = st.multiselect(
                "Your Skills",
                options=['Python', 'R', 'SQL', 'Machine Learning', 'AWS', 
                        'TensorFlow', 'PySpark', 'Tableau', 'Java', 'JavaScript',
                        'Docker', 'Kubernetes', 'React', 'Node.js'],
                default=['Python', 'Machine Learning', 'SQL'] if 'skills' not in st.session_state.user_data else st.session_state.user_data['skills'],
                key='profile_skills'
            )
            
            education = st.selectbox(
                "Highest Education",
                options=["Bachelor's", "Master's", "PhD", "Bootcamp", "Other"],
                index=0 if 'education' not in st.session_state.user_data else None,
                key='profile_education'
            )
            
            if st.button("Save Profile"):
                save_profile(role, salary, location, skills, experience, education)
                st.success("Profile saved!")
# Data visualization generation with Titan
def generate_visualization_data(prompt):
    response = bedrock.invoke_model(
        modelId="amazon.titan-text-express-v1",
        body=json.dumps({"inputText": prompt})
    )
    result = json.loads(response['body'].read())
    print("Model response:", result)  # Add this line to check the response
    try:
        return json.loads(result['results'][0]['outputText'])
    except Exception as e:
        print("Error parsing response:", e)  # Log any errors during parsing
        return {"error": "Failed to parse visualization data"}


# Resume processing
# def extract_text_from_file(uploaded_file):
#     if uploaded_file.type == "application/pdf":
#         reader = PdfReader(uploaded_file)
#         return "\n".join([page.extract_text() for page in reader.pages])
#     elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
#         doc = Document(uploaded_file)
#         return "\n".join([para.text for para in doc.paragraphs])
#     return uploaded_file.getvalue().decode("utf-8")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

# Load CSV file
file_path = "/content/eda_data.csv"
df = pd.read_csv(file_path)



# Ensure salary columns are numeric
df['min_salary'] = pd.to_numeric(df['min_salary'], errors='coerce')
df['max_salary'] = pd.to_numeric(df['max_salary'], errors='coerce')
df['avg_salary'] = pd.to_numeric(df['avg_salary'], errors='coerce')

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def skill_assessment_radar(user_data, df):
    skills = ['python_yn', 'R_yn', 'spark', 'aws', 'excel']  # Skills from dataset

    # User's skill proficiency levels (0-10 scale)
    user_skills = {
        'python_yn': 8 if 'Python' in user_data['skills'] else 3,
        'R_yn': 6 if 'R' in user_data['skills'] else 3,
        'spark': 7 if 'Spark' in user_data['skills'] else 3,
        'aws': 9 if 'AWS' in user_data['skills'] else 2,
        'excel': 7 if 'Excel' in user_data['skills'] else 3
    }

    # Filter dataset for same job role
    role_df = df[df['Job Title'] == user_data['current_role']]

    # Compute mean industry skill levels (1 if skill present, 0 otherwise)
    industry_means = role_df[skills].mean() * 10  # Scale to 0-10

    # Prepare data for plotting
    user_scores = [user_skills[skill] for skill in skills]
    industry_scores = [industry_means[skill] for skill in skills]

    angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
    user_scores += user_scores[:1]  # Close the circle
    industry_scores += industry_scores[:1]
    angles += angles[:1]

    # Plot radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, user_scores, linewidth=2, linestyle='solid', label="Your Skills", color='b')
    ax.fill(angles, user_scores, alpha=0.25, color='b')

    ax.plot(angles, industry_scores, linewidth=2, linestyle='dashed', label="Industry Average", color='r')
    ax.fill(angles, industry_scores, alpha=0.15, color='r')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(['Python', 'R', 'Spark', 'AWS', 'Excel'])
    ax.set_title(f"{user_data['current_role']} Skill Comparison", size=14)
    ax.legend(loc="upper right")

    st.pyplot(fig)



def salary_projection(user_data):
    st.warning("📢 Coming soon when sufficient data is available!")
    return
    current_salary = user_data['current_salary']
    years_experience = user_data['years_experience']
    
    # Simple salary projection (can be made more complex with models)
    projection_years = [years_experience + i for i in range(1, 6)]
    projected_salary = [current_salary * (1 + 0.05)**i for i in range(1, 6)]  # Assuming 5% annual growth
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(projection_years, projected_salary, marker='o')
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary ($)")
    ax.set_title(f"5-Year Salary Projection for {user_data['current_role']}")
    ax.grid(True)
    st.pyplot(fig)

def location_salary_comparison(user_data, df):
    
    location = user_data['location']
    location_data = df[df['Location'] == location]
    
    # Box plot for salary comparison based on location
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Location', y='avg_salary', data=location_data)
    plt.title(f"Salary Distribution in {location}")
    plt.ylabel("Average Salary ($)")
    st.pyplot(plt)





def education_salary_comparison(user_data, df):
    if df.empty or 'education' not in df.columns or 'avg_salary' not in df.columns:
        st.warning("📢 Coming soon when sufficient data is available!")
        return
    education = user_data['education']
    education_data = df[df['education'] == education]
    
    # Bar chart comparing salaries based on education level
    education_salary = education_data.groupby('education')['avg_salary'].mean()
    
    education_salary.plot(kind='bar', figsize=(8, 5))
    plt.title(f"Average Salary by Education Level for {user_data['current_role']}")
    plt.ylabel("Average Salary ($)")
    st.pyplot(plt)

def skills_vs_salary(user_data, df):
    if df.empty or not set(user_data['skills']).intersection(df.columns):
        st.warning("📢 Coming soon when sufficient data is available!")
        return
    skills = user_data['skills']
    
    # Create a filter based on skills and salary
    skill_salary_data = df[df[skills].notnull()]
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='skills', y='avg_salary', data=skill_salary_data)
    plt.title(f"Salary Distribution by Skills for {user_data['current_role']}")
    plt.ylabel("Average Salary ($)")
    st.pyplot(plt)



# Main app content
if st.session_state.current_user is None:
    st.warning("Please login or create an account to continue")
else:
    # Check if profile is complete
    if not st.session_state.users_db[st.session_state.current_user]['profile_complete']:
        st.warning("Please complete your profile in the sidebar")
    else:
        # Tab navigation
        tab1, tab2 = st.tabs(["🏠 Career Chat", "📊 Career Insights"])
        
        with tab1:
            st.header("AI Career Assistant")
            
            

            # Ensure chat history is a dictionary
            if "chat_history" not in st.session_state or not isinstance(st.session_state.chat_history, dict):
                st.session_state.chat_history = {}

            # Ensure user data exists
            if "user_data" not in st.session_state:
                st.session_state.user_data = {
                    "current_role": "Unknown",
                    "current_salary": 0,
                    "location": "Unknown",
                    "years_experience": 0,
                    "skills": [],
                    "education": "Unknown"
                }

            # Ensure chat history for current user
            if st.session_state.current_user not in st.session_state.chat_history:
                st.session_state.chat_history[st.session_state.current_user] = []

            # Get the current user's chat history
            current_chat = st.session_state.chat_history[st.session_state.current_user]

            # Chat interface
            user_input = st.chat_input("Ask about salaries, skills...")

            if user_input:
                # Add user message to chat history
                current_chat.append({"role": "user", "content": user_input})

                # Generate response with context
                context = f"""
                User Profile:
                - Role: {st.session_state.user_data['current_role']}
                - Salary: ${st.session_state.user_data['current_salary']:,}
                - Location: {st.session_state.user_data['location']}
                - Experience: {st.session_state.user_data['years_experience']} years
                - Skills: {', '.join(st.session_state.user_data['skills'])}
                - Education: {st.session_state.user_data['education']}
                """

                prompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
                You are a career advisor with access to this user profile:
                {context}
                Provide personalized advice based on their details.<|eot_id|>
                <|start_header_id|>user<|end_header_id|>
                {user_input}<|eot_id|>
                <|start_header_id|>assistant<|end_header_id|>"""

                response = bedrock.invoke_model(
                body=json.dumps({
                    "prompt": prompt,
                    "max_gen_len": 1024,
                    "temperature": 0.7
                }),
                modelId="meta.llama3-70b-instruct-v1:0"
                )

                # Read the content of the StreamingBody
                body_content = response['body'].read().decode('utf-8')  # Properly decode the byte stream to string

                # Parse the response into JSON
                try:
                  reply = json.loads(body_content)  # Assuming the response is in JSON format
                  generation = reply.get('generation', 'No response generated')
                except json.JSONDecodeError:
                  st.error("Failed to decode the response body.")

                # Display the result from the model
                if 'generation' in reply:
                  with st.chat_message("assistant"):
                    st.write(reply['generation'])

        
        with tab2:
            st.header("AI-Powered Career Visualizations")

            with st.expander("🛠️ Skill Assessment Radar"):
                if st.button("Generate Skill Radar"):
                    skill_assessment_radar(st.session_state.user_data, df)

            # Salary Projection
            with st.expander("💰 Salary Growth Projection"):
                if st.button("Generate Salary Projection"):
                    salary_projection(st.session_state.user_data)

            # Location-based Salary Comparison
            with st.expander("📍 Location-based Salary Comparison"):
                if st.button("Generate Location Salary Comparison"):
                    location_salary_comparison(st.session_state.user_data, df)

            # # Education-based Salary Comparison
            with st.expander("🎓 Education vs Salary Comparison"):
                if st.button("Generate Education Salary Comparison"):
                    education_salary_comparison(st.session_state.user_data, df)

            # Skills vs Salary Comparison
            with st.expander("💡 Skills vs Salary Comparison"):
                if st.button("Generate Skills Salary Comparison"):
                    skills_vs_salary(st.session_state.user_data, df)
