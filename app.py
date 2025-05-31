import streamlit as st
from utils import generate_resume, generate_cover_letter, analyze_skills, generate_interview_questions, match_jobs_with_resume

st.set_page_config(page_title="Smart Resume Builder", layout="centered")
st.title("🧠 Smart Resume & Cover Letter Generator (Offline LLM)")

st.markdown("Powered by Gemma 2B via Ollama | Created by Vansh Dudeja")

with st.form("resume_form"):
    name = st.text_input("Your Full Name")
    education = st.text_area("Education")
    experience = st.text_area("Experience")
    skills = st.text_area("Skills (comma-separated)")
    job_desc = st.text_area("Paste the Job Description")
    keyword = st.text_input("Job Search Keyword (e.g. Data Scientist, Python Developer)", value="Data Scientist")

    submit = st.form_submit_button("Generate Resume & Letter")

if submit:
    with st.spinner("Generating..."):
        user_bio = f"{name}\nEducation: {education}\nExperience: {experience}\nSkills: {skills}"

        resume = generate_resume(user_bio)
        cover_letter = generate_cover_letter(user_bio, job_desc)
        skills_gap = analyze_skills(skills, job_desc)
        questions = generate_interview_questions(job_desc)

        st.success("✅ Generated Successfully!")
        st.subheader("📄 Resume")
        st.code(resume, language='markdown')

        st.subheader("📬 Cover Letter")
        st.code(cover_letter, language='markdown')

        st.subheader("🧠 Skills Gap Analysis")
        st.info(skills_gap)

        st.subheader("🗣️ Interview Questions")
        st.warning(questions)

        st.subheader("💼 Matching Job Listings")
        job_matches = match_jobs_with_resume(user_bio, keyword=keyword)

        if job_matches:
            for match in job_matches:
                st.markdown(f"### {match['title']} at {match['company']}")
                st.markdown(f"**Why it's a match:** {match['reason']}")
                st.markdown(f"[Apply Here]({match['link']})")
                st.markdown("---")
        else:
            st.info("No good matches found. Try adjusting the job title or resume details.")
