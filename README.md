# 🛡️ ScamShield

### Think Before You Trust.

ScamShield is a Django-based web application that helps users identify potential warning signs in suspicious messages, emails, and job offers. It analyzes submitted text using rule-based keyword detection and provides a risk category with safety recommendations.

## ✨ Features

- **Scam Message Analysis:** Submit suspicious text for analysis.
- **Keyword-Based Detection:** Identifies warning signs related to prize claims, OTP requests, job registration fees, urgent payments, sensitive information, and suspicious link language.
- **Risk Classification:** Displays Low, Medium, or High risk based on the warning signs detected by the current rules.
- **Warning Explanations:** Shows the potential warning signs found in the submitted message.
- **Safety Awareness:** Encourages users to verify unexpected requests and protect sensitive information.
- **Responsive Interface:** A clean, styled interface designed for desktop and mobile screens.

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3

## ⚙️ How It Works

1. The user pastes a suspicious message, email, or job offer.
2. ScamShield checks the text against predefined keyword rules.
3. The application identifies matching warning signs.
4. A risk category is assigned based on the number of warning signs detected.
5. The results are displayed to help the user make a more informed decision.

## 🚀 Getting Started

### Prerequisites

- Python installed
- pip package manager
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Akshaya-11-byte/Scam_shield.git
```

**2. Navigate to the project directory**

```bash
cd Scam_shield
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the virtual environment**

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Install Django**

```bash
python -m pip install django
```

**6. Apply database migrations**

```bash
python manage.py migrate
```

**7. Start the development server**

```bash
python manage.py runserver
```

**8. Open the application**

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```text
scam_shield/
├── detector/
│   ├── static/
│   │   └── detector/
│   │       └── style.css
│   ├── templates/
│   │   └── detector/
│   │       └── home.html
│   └── views.py
├── scam/
├── manage.py
└── README.md
```

## 🔒 Important Security Note

ScamShield is an educational project that uses basic rule-based detection. Its results are not a guarantee that a message is genuine or fraudulent. Messages that do not match the current rules may still be scams. Always verify unexpected requests through official channels.

## 🔮 Future Enhancements

- Improve detection rules and test coverage.
- Add more detailed, context-aware explanations.
- Explore machine-learning-based scam classification.
- Add optional analysis history with appropriate privacy protections.
- Improve accessibility and user experience.

## 👩‍💻 Author

**Akshaya-11-byte**

GitHub: [Akshaya-11-byte](https://github.com/Akshaya-11-byte)

---

*Built to promote online safety and scam awareness.*