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

        if score < 50:
            st.error(f"⚠️ Low Match: {score}%")
        elif score < 75:
            st.warning(f"👍 Decent Match: {score}%")
        else:
            st.success(f"🌟 Great Match: {score}%")

        st.progress(int(min(score, 100)))

        skills = ["python","sql","excel","tally","communication",
                 "data","accounting","microsoft","software","ms-cit",
                 "english","hindi","computer","programming","java"]
        missing = [s for s in skills if s in job_description.lower()
                  and s not in resume_text.lower()]

        if missing:
            st.markdown("### ❌ Missing Skills:")
            for s in missing:
                st.markdown(f"- ➕ Add **{s}** to your resume")
        else:
            st.success("✅ No major skills missing!")
    else:
        st.error("Please fill both fields!")
