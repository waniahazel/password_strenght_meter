# Password Strength Meter

## Overview
This is a Streamlit-based web application that allows users to check the strength of their passwords or generate a strong password. The application evaluates the password based on several criteria, including length, the presence of uppercase and lowercase letters, digits, and special characters. It also provides feedback on how to improve the password's strength.

## Features
1. **Password Strength Checker**:
   - Evaluates the strength of a password based on the following criteria:
     - Minimum length of 8 characters.
     - Presence of at least one uppercase letter.
     - Presence of at least one lowercase letter.
     - Presence of at least one digit.
     - Presence of at least one special character (`!@#$%^&*`).
   - Provides a strength score out of 5 and detailed feedback on how to improve the password.

2. **Strong Password Generator**:
   - Generates a random 12-character password that includes a mix of uppercase and lowercase letters, digits, and special characters.

## How to Use
1. **Check Password Strength**:
   - Select the "Check Password Strength" option.
   - Enter your password in the text box.
   - Click the "Check Strength" button to see the strength score and feedback.

2. **Generate a Strong Password**:
   - Select the "Generate a Strong Password" option.
   - Click the "Generate Password" button to create a strong password.
   - The generated password will be displayed on the screen.

## Installation
To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/password-strength-meter.git
   cd password-strength-meter
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages using pip:
   ```bash
   pip install streamlit
   ```

3. **Run the Application**:
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the name of your Python file if it's different.

4. **Access the App**:
   Open your web browser and go to `http://localhost:8501` to use the application.

## Code Structure
- **`check_password_strength(password)`**: Function to evaluate the strength of a password and provide feedback.
- **`generate_strong_password()`**: Function to generate a strong password.
- **`main()`**: The main function that runs the Streamlit app and handles user interactions.

## Dependencies
- **Streamlit**: For building and running the web application.
- **Python**: The programming language used.
- **re**: For regular expression operations.
- **random**: For generating random passwords.

## Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and create a pull request with your changes.

## License
This project is open-source and available under the MIT License.

---

Enjoy using the Password Strength Meter! If you have any questions or feedback, feel free to reach out.
