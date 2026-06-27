import streamlit as st

st.set_page_config(page_title="ResuMatch AI", page_icon="💜")
st.title("💜 ResuMatch AI")
st.subheader("Your Smart Career Partner")
st.markdown("---")

resume_text = st.text_area("📄 Paste Your Resume Text", height=200)
job_description = st.text_area("📝 Paste Job Description", height=200)

if st.button("🔍 Analyze"):
    if resume_text and job_description:
        resume_words = set(resume_text.lower().split())
        job_words = set(job_description.lower().split())
        common = resume_words & job_words
        score = round(len(common)/len(job_words)*100, 2)
        st.success(f"✅ Match Score: {score}%")
        st.progress(int(min(score, 100)))
    else:
        st.error("Please fill both fields!")
