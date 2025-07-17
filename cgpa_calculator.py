import streamlit as st

# Function to calculate CGPA to percentage
def calculate_percentage(sgpas, credits):
    total_score = sum(sgpa * credit for sgpa, credit in zip(sgpas, credits))
    total_credits = sum(credits)
    cgpa = total_score / total_credits
    percentage = (cgpa - 0.5) * 10
    return cgpa, percentage

# Streamlit app
st.title("BPUT CGPA to Percentage Calculator")
st.write("This calculator helps BPUT (Biju Patnaik University of Technology) students convert their CGPA to percentage based on SGPA and credit points.")

# Explanation section
with st.expander("Click here to see how the calculator works"):
    st.write("""
    ### How the Calculator Works:
    1. **Inputs Required:**
       - **SGPA for each semester**: Placeholder asks you to enter SGPA manually.
       - **Credits for each semester**: Default credit points are pre-filled based on BPUT standards but can be adjusted if needed.
    2. **Default Credit Points:**
       - **Regular Students**:  
         Credits for all 8 semesters are `[26, 26, 24, 24, 24, 24, 20, 16]`.
       - **Lateral Entry Students**:  
         Credits for semesters 3 to 8 are `[22, 24, 22, 22, 23, 6]`.
    3. **Calculation Formula**:
       - CGPA = (Sum of SGPA * Credits) / Total Credits.
       - Percentage = (CGPA - 0.5) * 10.
    4. **How to Use**:
       - Select whether you are a **regular** or **lateral entry** student.
       - Enter your SGPA for each semester.
       - Verify or change the credit points if needed.
       - Click **Calculate** to see your CGPA and percentage.
    """)

# Additional guide for getting SGPA and Credits
with st.expander("📚 How to Get Your Semester-wise SGPA and Credits"):
    st.write("""
    To get your semester-wise **SGPA** and **credit details** from the official BPUT portal, follow these steps:

    1. Visit: [https://exam.bput.ac.in/](https://exam.bput.ac.in/)
    2. Click on **BPUT Student Login** and log in using your credentials.
    3. On the **top-left corner**, click the **☰ hamburger menu icon**.
    4. Choose **Exam History** from the menu.
    5. You will see each semester's **SGPA** and **Total Credits**.

    > ℹ️ Use this data to fill the SGPA and credit inputs in the calculator above.
    """)

# Shortcut: Direct CGPA to Percentage Converter
st.subheader("🎯 Already Know Your CGPA?")
with st.expander("Click here to directly convert CGPA to Percentage"):
    col1, col2 = st.columns(2)
    with col1:
        user_cgpa = st.number_input("Enter your Final CGPA", min_value=0.0, max_value=10.0, step=0.01)
    with col2:
        user_credits = st.number_input("Enter your Total Earned Credits", min_value=1, step=1)

    if st.button("Convert to Percentage"):
        percentage = (user_cgpa - 0.5) * 10
        st.success(f"Your Percentage is: **{percentage:.2f}%**")
        st.caption("📌 Formula used: (CGPA - 0.5) × 10")
        st.info(f"Based on a total of **{user_credits} credits**.")

# Ask if the user is a lateral entry student
lateral_entry = st.radio("Are you a lateral entry student?", ("No", "Yes"))

# Default BPUT credit points
if lateral_entry == "Yes":
    default_credits = [22, 24, 22, 22, 23, 6]  # 3rd to 8th semester
    semesters = range(3, 9)
else:
    default_credits = [26, 26, 24, 24, 24, 24, 20, 16]  # 1st to 8th semester
    semesters = range(1, 9)

# Input SGPA and credits
sgpas = []
modified_credits = []

st.write("### 📝 Enter SGPA and Modify Credits (if needed):")
for i, sem in enumerate(semesters):
    col1, col2 = st.columns(2)
    with col1:
        sgpas.append(
            st.text_input(f"SGPA for Semester {sem}", placeholder="Enter SGPA")
        )
    with col2:
        modified_credits.append(
            st.number_input(f"Credits for Semester {sem}", value=default_credits[i], min_value=1, max_value=30)
        )

# Calculate CGPA and Percentage for any filled semester
if st.button("Calculate"):
    valid_sgpas = []
    valid_credits = []

    for i in range(len(sgpas)):
        if sgpas[i].strip() != "":
            try:
                sgpa_val = float(sgpas[i])
                valid_sgpas.append(sgpa_val)
                valid_credits.append(modified_credits[i])
            except ValueError:
                st.error(f"Invalid SGPA input in Semester {semesters[i]}")

    if len(valid_sgpas) == 0:
        st.error("Please enter at least one valid SGPA to calculate!")
    else:
        cgpa, percentage = calculate_percentage(valid_sgpas, valid_credits)
        st.success("### Result:")
        st.write(f"**CGPA (based on {len(valid_sgpas)} semester(s))**: {cgpa:.2f}")
        st.write(f"**Percentage:** {percentage:.2f}%")

st.markdown("---")
st.markdown("Developed with ❤️ by Shankarsan.") 
For any issues, contact me at: [kirantechno7@gmail.com](mailto:kirantechno7@gmail.com)")
