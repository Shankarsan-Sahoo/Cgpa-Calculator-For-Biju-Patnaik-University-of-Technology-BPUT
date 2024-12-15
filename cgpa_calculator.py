import streamlit as st

# Function to calculate CGPA to percentage
def calculate_percentage(sgpas, credits):
    total_score = sum(sgpa * credit for sgpa, credit in zip(sgpas, credits))
    total_credits = sum(credits)
    cgpa = total_score / total_credits
    percentage = (cgpa - 0.5) * 10
    return cgpa, percentage

# Streamlit app
st.title("CGPA to Percentage Calculator for BPUT")
st.write("This calculator helps BPUT(Biju Patnaik University of Technology) students convert their CGPA to percentage based on their SGPA and credit points.")

# Explanation section
with st.expander("Click here to see how the calculator works"):
    st.write("""
    ### How the Code Works:
    1. **Inputs Required:**
       - **SGPA for each semester:** You need to enter the SGPA for each semester.
       - **Credits for each semester:** Default credit points are pre-filled as per BPUT standards but can be adjusted if necessary.
    2. **Default Credit Points:**
       - The app uses standard BPUT credit values:
         - For **regular students**, the credits are:  
           `[26, 26, 24, 24, 24, 24, 20, 16]` (1st to 8th semester).  
         - For **lateral entry students**, the credits are:  
           `[24, 24, 24, 24, 20, 16]` (3rd to 8th semester).
    3. **Calculation Formula:**
       - **CGPA** is calculated as:  
         \[
         \text{CGPA} = \frac{\sum (\text{SGPA} \times \text{Credits})}{\text{Total Credits}}
         \]
       - **Percentage** is calculated as:  
         \[
         \text{Percentage} = (\text{CGPA} - 0.5) \times 10
         \]
    4. **How to Use:**
       - Select whether you are a **regular** or **lateral entry** student.
       - Enter your SGPA for the relevant semesters.
       - Verify or modify the credit points for each semester.
       - Click **Calculate** to see your CGPA and percentage.
    """)

# Ask if the user is a lateral entry student
lateral_entry = st.radio("Are you a lateral entry student?", ("No", "Yes"))

# Default BPUT credit points
if lateral_entry == "Yes":
    default_credits = [24, 24, 24, 24, 20, 16]  # Credits for 3rd to 8th semester
    semesters = range(3, 9)
else:
    default_credits = [26, 26, 24, 24, 24, 24, 20, 16]  # Credits for 1st to 8th semester
    semesters = range(1, 9)

# Input SGPA for each semester and allow modifying credit points
sgpas = []
modified_credits = []

st.write("### Enter SGPA and Modify Credits (if needed):")
for i, sem in enumerate(semesters):
    col1, col2 = st.columns(2)
    with col1:
        sgpas.append(st.number_input(f"SGPA for Semester {sem}", min_value=0.0, max_value=10.0, step=0.01))
    with col2:
        modified_credits.append(st.number_input(f"Credits for Semester {sem}", value=default_credits[i], min_value=1, max_value=30))

# Calculate CGPA and percentage
if st.button("Calculate"):
    cgpa, percentage = calculate_percentage(sgpas, modified_credits)
    st.write("### Result:")
    st.write(f"**CGPA:** {cgpa:.2f}")
    st.write(f"**Percentage:** {percentage:.2f}%")

st.write("---")
st.write("### Credits :")
st.write("Developed with ❤️ Shankarsan.")
st.write("For any issues, contact me at: (kirantechno7@gmail.com).")
