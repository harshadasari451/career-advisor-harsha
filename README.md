# Career Advisor: AI-Driven Career and Compensation Guide

## Team Name: PathFinders

## Team Members:
- **Harsha Vardhan**
- **Suayash Madhavi**
- **Anirudh Sharma**
- **Aditya Malkar**

## Overview
Career Advisor is an AI-powered assistant designed to democratize career advancement by transforming complex compensation data into personalized guidance. By leveraging conversational AI, interactive visualizations, and analytical simulations, Career Advisor helps individuals make informed career decisions, optimize their earning potential, and plan strategic skill development.

## Motivation
### Confronting a Global Issue
The modern job market is rapidly evolving, and professionals often struggle with fragmented and complex salary information when considering career changes. Many individuals, like those transitioning from marketing to product management, find it difficult to assess the long-term financial impact of their decisions.

Despite the vast availability of compensation data, there is a lack of intuitive tools that translate this data into actionable career insights. Career Advisor bridges this gap by providing tailored career guidance using AI-driven data analysis and interactive simulations.

## Market Need
Career decision-making has become more complex, with skills taking priority over traditional job titles. According to research:
- **78%** of workers are unaware of career choices that would optimize their salary.
- **65%** lack confidence in salary negotiations due to information asymmetry.

Career Advisor addresses these challenges by providing structured, personalized insights that empower individuals to navigate career transitions and salary negotiations effectively.

## Features & User Journey
### 1. **Initial Evaluation and Standardization**
- Users begin by asking: *"How does my salary compare to industry norms?"*
- Career Advisor benchmarks salaries against industry data, considering experience, location, and skills.
- Example: A software engineer finds they are in the 45th percentile for salary, but peers with cloud technology skills earn **22% more**.

### 2. **Competency-Based Professional Development**
- Users ask: *"Which skills will boost my earning potential the most?"*
- Career Advisor identifies high-demand skills that align with the user's career trajectory.
- Example: A software engineer is recommended **Kubernetes, serverless architecture, and machine learning**, with predicted earnings after skill acquisition.

### 3. **Professional Career Simulation**
- Users explore: *"What if I switch to a different role?"*
- Career Advisor simulates multiple career paths, predicting salary trends and skill requirements.
- Example: A software engineer considers DevOps, viewing salary projections, required certifications, and market demand.

### 4. **Negotiation Strategy**
- Users ask: *"How can I maximize my salary in my current role?"*
- Career Advisor provides data-driven negotiation strategies, including personalized scripts and optimal timing for discussions.

## Technical Implementation
### AI Integration
Career Advisor is built primarily on **AWS** infrastructure, leveraging cloud-based AI models and scalable computing power. Key components include:

- **Model Selection in AWS:**
  - **Bedrock:** Utilizes **Llama 3** for text generation to power conversational AI.
  - **Titan Image Generator:** Used for generating visualizations based on salary trends and career paths.

- **Data Processing and Access:**
  - AWS CLI is used to access and manage models securely.
  - Data is fetched, cleaned, and processed in AWS-based environments for efficient querying and model training.
  
- **Frontend Development:**
  - **Streamlit** is used to create an interactive and user-friendly interface for Career Advisor, allowing real-time engagement and career simulations.

- **Data Storage and Management:**
  - The salary dataset is sourced from Kaggle and stored in AWS S3 for scalability and accessibility.
  - Dataset links:
    - [EDA Data](https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/data?select=eda_data.csv)
    - [Glassdoor Jobs Data](https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor/data?select=glassdoor_jobs.csv)
  
- **Visualization Tools:**
  - **Interactive heat maps** linking skills to compensation.
  - **Career path trees** to visualize earnings potential.
  - **Dynamic dashboards** for personalized career projections.

### Confidentiality & Data Protection
- Utilizes **federated learning** to process salary data locally before aggregating insights.
- Implements **end-to-end encryption** to protect user information.

## Impact & Future Outlook
Career Advisor empowers professionals across all backgrounds by:
- Providing **personalized salary intelligence** to level the playing field.
- Addressing **compensation disparities** and market inefficiencies.
- Offering **company-specific promotion trend analysis** in future updates.
- Detecting **bias in salary structures** and recommending **high-value learning paths**.

## Conclusion
Career Advisor transforms career decision-making into an empowering, data-driven experience. By integrating AI, advanced analytics, and visualization, it serves as a **career companion** that grows with the user, providing guidance at every professional crossroad.

In a world where career choices impact lifetime earnings, Career Advisor ensures decisions are based on **data, not speculation**.

---
### 📌 Get Started
- Clone the repository: `git clone https://github.com/your-repo/career-advisor.git`
- Follow setup instructions in [INSTALLATION.md](INSTALLATION.md)

### 🔗 Connect with Us
For updates and contributions, feel free to open issues or submit pull requests. Your feedback helps us improve Career Advisor!

🚀 **Empower your career with data-driven decisions!**

