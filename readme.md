# Advanced Password Strength Analyzer

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-GPLv3-blue.svg)

A comprehensive password strength checking tool with both GUI and CLI interfaces. This application helps users create and validate secure passwords using advanced strength checking algorithms.

*Replace this with a screenshot or GIF of your application's GUI and CLI.*
![App Screenshot](./screenshot.png)

## ✨ Features

-   **Dual Interface:** Choose between a user-friendly Graphical User Interface (GUI) or an efficient Command-Line Interface (CLI).
-   **Advanced Strength Analysis:** Uses the powerful **zxcvbn** algorithm for realistic password strength assessment that recognizes common patterns, words, and substitutions.
-   **Secure Password Generation:** Create strong, random passwords of a customisable length.
-   **Comprehensive Checks:** Validates passwords against multiple criteria, including minimum length, character complexity (uppercase, lowercase, numbers, symbols), and lists of common or banned passwords.
-   **Improvement Suggestions:** Get specific, actionable recommendations to strengthen weak passwords.
-   **Export Functionality:** Save detailed password check results to a JSON file directly from the GUI.
-   **Detailed Logging:** Automatically tracks all password check operations in a local log file for auditing purposes.

## 🧠 Core Concepts Explained

This tool uses several methods to determine password strength:

-   **Entropy:** This is a measure of a password's unpredictability and randomness. It's calculated based on the password's **length** and the size of the **character pool** (e.g., lowercase, uppercase, numbers, symbols used). Higher entropy means it's exponentially harder for a computer to brute-force.

-   **Pattern Matching:** The checker actively looks for lazy and predictable patterns that weaken a password, such as:
    -   **Sequences:** `abc`, `123`, `qwerty`
    -   **Repetitions:** `aaaa`, `1111`, `!!!`

-   **Data Breach Check (k-Anonymity):** The tool checks your password against a database of billions of breached passwords using a secure model that protects your privacy.
    1.  Your password is **never** sent over the internet.
    2.  It is hashed (scrambled) locally on your computer.
    3.  Only the **first 5 characters** of the hash are sent to the Have I Been Pwned API.
    4.  Your computer does the final check locally, ensuring your password remains anonymous.

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/password-strength-checker.git](https://github.com/yourusername/password-strength-checker.git)
    cd password-strength-checker
    ```
    *Remember to replace `yourusername` with your actual GitHub username.*

2.  **Install dependencies:**
    ```bash
    pip install zxcvbn
    ```

3.  **Required Wordlists:**
    Ensure the following files are present in the project directory:
    * `weak_passwords.txt`: A list of commonly used weak passwords.
    * `banned_passwords.txt`: A list of company-specific or otherwise banned passwords.

## 🚀 Usage

You can run the application in either GUI or CLI mode.

### GUI Mode
Launch the graphical interface by running the script without any arguments:
```bash
python password_strength_checker.py
```

### CLI Mode
For command-line operations, use the following commands.

-   **Launch Interactive CLI:**
    ```bash
    python password_strength_checker.py --cli
    ```

-   **Check a specific password directly:**
    ```bash
    python password_strength_checker.py --check "your_password_here"
    ```

-   **Generate a strong password:**
    ```bash
    # Generate a password with default length (16)
    python password_strength_checker.py --generate

    # Generate a password with a custom length
    python password_strength_checker.py --generate --length 20
    ```

## 🛠️ Command-Line Arguments

| Argument            | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `--cli`             | Launch the application in interactive CLI mode.       |
| `--check PASSWORD`  | Check the strength of a specific password directly.   |
| `--generate`        | Generate a new strong, random password.               |
| `--length N`        | Specify the length for the generated password.        |

## 🔐 Security Notes

Your security is the top priority. Please note the following:
-   **No Permanent Storage:** Passwords entered for checking are never stored permanently.
-   **Local Processing:** All password analysis is done locally on your machine.
-   **No External API Calls:** This tool does not make any external network calls to check passwords, ensuring your data remains private.
-   **Secure Generation:** New passwords are created using Python's `secrets` module for cryptographically strong randomness.

## 📜 Logging

The application logs all password check operations to `password_checker.log`. Each log entry includes a timestamp, the action performed (e.g., `CHECK_PASSWORD`), and the strength result.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests for any bugs or improvements.

## 📄 License

This project is licensed under the GPL 3.0 License. See the `LICENSE` file for details.