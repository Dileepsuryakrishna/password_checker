# Advanced Password Strength Analyzer

A command-line tool built with Python to analyze password strength based on multiple security criteria, including length, character variety, entropy, and exposure in known data breaches via the 'Have I Been Pwned' API.

## Key Features ✨

-   **Length & Variety Analysis:** Checks for password length and the use of uppercase letters, lowercase letters, numbers, and symbols.
-   **Pattern Detection:** Identifies weak patterns like character sequences (`abc...`) and repetitions (`aaa...`).
-   **Entropy Calculation:** Measures the true randomness of the password in bits using the formula `E = L * log2(N)`.
-   **Data Breach Check:** Securely checks if the password has been exposed in a data breach using the Pwned Passwords API and the k-Anonymity model.
-   **Detailed Feedback:** Provides a final score, a rating from "Weak" to "Very Strong", and actionable feedback with colored output for readability.
-   **Secure Input:** Uses `getpass` to ensure passwords are not echoed to the terminal when entered interactively.

## Security Concepts Demonstrated 🛡️

-   **Entropy:** The core measure of a password's unpredictability against brute-force attacks.
-   **k-Anonymity:** The privacy-preserving model used to interact with the HIBP API. The tool only sends the first 5 characters of a password's SHA-1 hash, protecting the full password from exposure.

## Installation ⚙️

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/password-strength-analyzer.git](https://github.com/YOUR_USERNAME/password-strength-analyzer.git)
    cd password-strength-analyzer
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 🚀

You can run the script in two ways:

1.  **Interactive Mode (Recommended & Secure):**
    ```bash
    python strength_checker.py
    ```
    You will be prompted to enter a password securely.

2.  **Argument Mode:**
    ```bash
    python strength_checker.py "Your-Password-Here-123!"
    ```

### **Security Disclaimer**

This is an educational project. While the HIBP API check is designed to be secure, **never enter sensitive passwords into tools or websites you do not fully trust.**