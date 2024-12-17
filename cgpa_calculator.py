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
st.write("This calculator helps BPUT(Biju Patnaik University of Technology) students convert their CGPA to percentage based on SGPA and credit points.")

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
         Credits for semesters 3 to 8 are `[24, 24, 24, 24, 20, 16]`.
    3. **Calculation Formula**:
       - CGPA = (Sum of SGPA * Credits) / Total Credits.
       - Percentage = (CGPA - 0.5) * 10.
    4. **How to Use**:
       - Select whether you are a **regular** or **lateral entry** student.
       - Enter your SGPA for each semester.
       - Verify or change the credit points if needed.
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
        # Use placeholder instead of default value
        sgpas.append(
            st.text_input(f"SGPA for Semester {sem}", placeholder="Enter SGPA")
        )
    with col2:
        modified_credits.append(
            st.number_input(f"Credits for Semester {sem}", value=default_credits[i], min_value=1, max_value=30)
        )

# Convert SGPA inputs from string to float, handling errors
try:
    sgpas = [float(sgpa) for sgpa in sgpas if sgpa.strip() != ""]
except ValueError:
    st.error("Please enter valid SGPA values!")

# Calculate CGPA and percentage
if st.button("Calculate"):
    if len(sgpas) != len(semesters):
        st.error("Please fill in SGPA values for all semesters!")
    else:
        cgpa, percentage = calculate_percentage(sgpas, modified_credits)
        st.write("### Result:")
        st.write(f"**CGPA:** {cgpa:.2f}")
        st.write(f"**Percentage:** {percentage:.2f}%")

st.write("---")
st.write("Developed with ❤️ by Shankarsan.")
st.write("For any issues, contact me at: (kirantechno7@gmail.com).")
st.write("For any issues, contact me at: (kirantechno7@gmail.com).")
