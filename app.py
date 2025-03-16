import streamlit as st
import re
import random

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check (Minimum 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase Letter Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one uppercase letter (A-Z).")

    # Lowercase Letter Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one lowercase letter (a-z).")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one digit (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 5:
        feedback.append("✅ Strong Password! Great job!")
    elif score >= 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    return feedback, score

# Function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))  # Generate a 12-character password
    return password

# Streamlit App
def main():
    st.title("🔐 Password Strength Meter")
    st.write("Welcome to the Password Strength Meter! Check your password's strength or generate a strong one.")

    # Menu
    option = st.radio("Choose an option:", ["Check Password Strength", "Generate a Strong Password"])

    if option == "Check Password Strength":
        password = st.text_input("Enter your password:", type="password", key="password_input")
        
        # Add a button to check strength
        if st.button("Check Strength"):
            if password:
                feedback, score = check_password_strength(password)
                for message in feedback:
                    if message.startswith("❌"):
                        st.error(message)
                    elif message.startswith("⚠️"):
                        st.warning(message)
                    else:
                        st.success(message)
                
                # Display strength score
                st.write(f"**Strength Score:** {score}/5")
            else:
                st.warning("Please enter a password to check its strength.")

    elif option == "Generate a Strong Password":
        if st.button("Generate Password"):
            strong_password = generate_strong_password()
            st.success(f"🔒 Generated Strong Password: `{strong_password}`")

# Run the app
if __name__ == "__main__":
    main()