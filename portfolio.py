import streamlit as st

#Set page title and icon

st.set_page_config(page_title="Student Portfolio",page_icon="🎓")

#Sidebar naviagtion

st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go To:",
	   ["Home","Projects","Skills","Settings","Contact"])
#Home section

if page =="Home":
	st.title("🎓 Student Portfolio")

	#Profile image
	uploaded_image = st.file_uploader("Uplaod Profile Picture", type=["jpg","png"])
	if uploaded_image is not None:
		st.image(uploaded_image, width=150, caption="Uploaded image")
	else:
		st.image("person.jpg", width=150, caption="Default image")
	#Student details (Editable!)
	name = st.text_input("Name: ", "IGIRANEZA Fabrice")
	location = st.text_input("Location: ", "Musanze,Rwanda")
	field_of_study = st.text_input("Field of Study: ",
	                               "Computer Science, SWE (year 3 A)")
	university = st.text_input("University: ", "INES - Ruhengeri")

	st.write(f"📍{location}")
	st.write(f"📚{field_of_study}")
	st.write(f"🎓{university}")

	# Resume download button
	with open("resume.pdf", "rb") as file:
		resume_bytes = file.read()
	st.download_button(label="📄Download Resume",
		data=resume_bytes,file_name="resume.pdf",
		mime="application/pdf")

	st.markdown("---")
	st.subheader("About Me")
	about_me = st.text_area("Short introduction about myself:" "I'm a third-year Computer Science - Software Engineering student passionate about web and software development. Currently working on a **Digital Marketplace Management System** for my final year project.")
	st.write(about_me)

#Projects section
elif page =="Projects":
	st.title("💻 My Projects")

	with st.expander("🏡 Virunga homestay"):
		st.write("Project Type: (Web application)")
		st.write(" Brief Description: (an airbnb-like platform for booking homestays in the Virunga region, Rwanda. It allows users to view available homestays, book a stay, and leave reviews.)")

	with st.expander("⛰️ Day tour agency"):
		st.write("Project Type: (Tour website)")
		st.write("Description: (A tourism open source website for a daytour agancy company used to manage, plan and share tours) ")

	with st.expander("🏗️ Construction assistance platform"):
		st.write("Project Type: (Current Dissertation/Final Year Project )")
		st.write("Description: (This platform connects engineers and homebuilders, providing guidance, resources, and expert consultations for construction projects. It aims to bridge the information gap, streamline project management, and connect users with suppliers for materials and services.) ")

elif page =="Skills":
	st.title("🏹Skills and Achievements")

	st.subheader("Programming Languages ")
	skill_python = st.slider("Python",10,100,90)
	st.progress(skill_python)

	skill_js = st.slider("JavaScript",0,100,75)
	st.progress(skill_js)
	skill_SQL = st.slider("SQL",0,100,65)
	st.progress(skill_SQL)
	st.subheader("Machine Learning ")
	skill_DS = st.slider("Data Science ", 20, 100, 80)
	st.progress(skill_DS )
	st.subheader("Web Development")
	skill_HTML = st.slider("HTML", 20, 100, 80)
	st.progress(skill_HTML)
	skill_CSS = st.slider("CSS", 20, 100, 80)
	st.progress(skill_CSS)
	skill_React = st.slider("React", 20, 100, 80)
	st.progress(skill_React)
	skill_Flask = st.slider("Flask", 20, 100, 80)
	st.progress(skill_Flask)
	st.subheader("Cerfications & Achievements")
	st.write("✅ Completed Microsoft Office specialist in Powerpoint,word adn Excel ")
	st.write("✅ Certified backend developer using django from Natcom academy")

elif page == "Settings":
	st.title("🎨 Customize your profile")

	st.subheader("Upload a Profile Picture")
	uploaded_image = st.file_uploader("Choose a file", type=["jpg","png"])
	if uploaded_image:
		st.image(uploaded_image, width=150)

	st.subheader("✍ Edit Personal Info")

elif page =="Contact":
	st.title("🤳 Contact Me")

	with st.form("contact_form"):
		name = st.text_input("your name")
		email = st.text_input("Your Email")
		message=st.text_area("Your message 💌")

		submitted = st.form_submit_button("Send Message")
		if submitted:
			st.success("✅ Message sent successfully")

		st.write("📧 Email: ug2322084@ines.ac.rw")
		st.write("[🔗LinkedIn](https://www.linkedin.com/in/igiraneza-fabrice-16b2b2355?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")
		st.write("[📂GitHub](https://github.com/IGIRANEZAFabrice)")

	st.sidebar.write("---")
	st.sidebar.write(" Designed by fab")