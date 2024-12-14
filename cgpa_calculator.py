import streamlit as st

def calculate_cgpa():
    st.title("CGPA to Percentage Calculator Biju Patnaik University of Technology (BPUT)")
    st.write("Enter your SGPA and Credits for each semester:")

    # Input the number of semesters
    num_semesters = st.number_input("Number of Semesters:", min_value=1, step=1)

    # Initialize lists to store SGPA and credits
    sgpa_list = []
    credits_list = []

    # Collect SGPA and credit inputs for each semester
    for i in range(num_semesters):
        sgpa = st.number_input(f"Enter SGPA for Semester {i+1}:", key=f"sgpa_{i}")
        credits = st.number_input(f"Enter Credits for Semester {i+1}:", key=f"credits_{i}")
        sgpa_list.append(sgpa)
        credits_list.append(credits)

    # Calculate CGPA and Percentage
    if st.button("Calculate"):
        total_weighted_sgpa = sum(s * c for s, c in zip(sgpa_list, credits_list))
        total_credits = sum(credits_list)

        if total_credits > 0:
            cgpa = total_weighted_sgpa / total_credits
            percentage = (cgpa - 0.5) * 10
            st.success(f"CGPA: {cgpa:.2f}")
            st.success(f"Percentage: {percentage:.2f}%")
        else:
            st.error("Please enter valid credit values.")

    # Add credits section
    st.markdown("---")  # Add a horizontal line
    st.markdown(
        """
        **Credits:**  
        Developed with love ❤️ Shankarsan.
        
        For any issues, contact me at (kirantechno7@gmail.com).
        """

    
    )

# Run the function
if __name__ == "__main__":
    calculate_cgpa()
