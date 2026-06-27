import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="ResuMatch AI", page_icon="💜")
st.title("💜 ResuMatch AI")
st.subheader("Your Smart Career Partner")
st.markdown("---")
resume_text = st.text_area("📄 Paste Your Resume Text Here", height=200)
job_description = st.text_area("📝 Paste Job Description Here", height=200)
if st.button("🔍 Analyze My Resume"):
    if resume_text and job_description:
        docs = [resume_text, job_description]
        vec = TfidfVectorizer()
        mat = vec.fit_transform(docs)
        score = round(cosine_similarity(mat[0], mat[1])[0][0]*100, 2)
        skills = ["python","sql","excel","tally","communication",
                 "data","accounting","microsoft","software","ms-cit"]
        missing = [s for s in skills if s in job_description.lower()
                  and s not in resume_text.lower()]
        st.markdown("---")
        if score < 50:
            st.error(f"⚠️ Low Match: {score}%")
        elif score < 75:
            st.warning(f"👍 Decent Match: {score}%")
        else:
            st.success(f"🌟 Great Match: {score}%")
        st.progress(int(score))
        if missing:
            st.markdown("### ❌ Missing Skills:")
            for s in missing:
                st.markdown(f"- ➕ Add **{s}** to your resume")
        else:
            st.success("✅ No major skills missing!")
    else:
        st.error("Please paste both resume and job description!")
