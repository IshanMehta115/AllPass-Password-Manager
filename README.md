# AllPass Password Manager

<p align="center">
  <img src="https://github.com/IshanMehta115/AllPass-Password-Manager/blob/main/pic.PNG" alt="Webpage Screenshot" width="800px">
</p>

AllPass Password Manager is a secure and user-friendly password management application built using Django and Bootstrap. It focuses on both cybersecurity and usability, providing a comprehensive solution for storing and managing user passwords.

## Features

- **OTP Verification**: During signup and login, users are sent a One-Time Password (OTP) to their registered email. The OTP must be entered into the application to proceed further, ensuring enhanced security.

- **Strong Password Suggestions**: When creating a master password and storing other passwords, the application suggests a strong password to the user. The suggested password is a combination of alphabets, numbers, and special characters of fixed length, further strengthening the security of user credentials.

- **Encryption**: All user credentials stored in the application's database are encrypted using industry-standard encryption schemes such as AES and SHA. This ensures that sensitive data remains secure even if the database is compromised.

- **Password Reset**: Users who have forgotten their password can easily reset it. The reset process includes OTP verification from the registered email address, followed by the creation of a new password.

- **Secure Input Fields and XSS Prevention**: Input fields such as username, email, password, and URL are protected against scripting attacks, ensuring that user data remains safe from potential vulnerabilities, including Cross-Site Scripting (XSS) attacks. The application employs input sanitization techniques to validate and clean user-supplied data, removing or encoding any potentially malicious code that could be injected into the application.

- **Password Management**: Once logged into the application, users can easily store passwords for their various accounts. They also have the ability to delete and modify stored passwords, providing flexibility and control over their credentials.

- **Search Functionality**: The application includes a search bar on the passwords page, allowing users to quickly find the credentials for a specific website or service.

- **Website Logo/Icon Retrieval**: When users enter the URL and credentials for a website, the application automatically retrieves and displays the corresponding website logo/icon. This feature enhances navigation and provides a visually pleasing experience.

- **CSRF Protection**: Cross-Site Request Forgery (CSRF) tokens are implemented to prevent unauthorized requests and protect against CSRF attacks.

- **User-Friendly Design**: The application features a simple color scheme and an easy-to-use interface, prioritizing usability and intuitive design.


## Local Setup and Installation

To run AllPass Password Manager locally on your machine, follow these steps:

1. Clone the repository:<br>
3. Install the required dependencies:<br>`cd allpass-password-manager`<br>`pip install -r requirements.txt`
4. Configure the database settings in the `settings.py` file.
5. Apply the database migrations:<br>`python manage.py migrate`
6. Start the development server:<br>`python manage.py runserver`
7. Access the application in your web browser at `http://localhost:8000`


## Usage

To access and use AllPass Password Manager, visit the project website [https://ishanmehta.pythonanywhere.com/](https://ishanmehta.pythonanywhere.com/)


## Contributing

Contributions to the AllPass Password Manager project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
