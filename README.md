# Campus_Recovery_Portal
post, search and recover items and acts like a lost and find portal.
# 📦 Campus Recovery Portal (FindIt)

## 👨‍💻 Team Details
**Team Name:** CODE BLOODED CREW  
**Project Type:** Web Application – Lost & Found Portal  

**Members:**

Bhavyan Potla(POC)

Suhaas Sarabu

Hemanth Batthala

Lokesh kumar

---

## ❗ Problem Statement
Students in college frequently lose personal belongings like ID cards, keys, wallets, notebooks, earphones, chargers and mobile accessories.  
Recovery usually depends on WhatsApp groups, security office boards or word of mouth. These methods are unorganized and many items never reach their rightful owner.

There is no centralized digital system inside the campus to report and find lost items efficiently.

---

## 💡 Our Solution
Campus Recovery Portal (FindIt) is a centralized web platform where students can report lost items and found items.  
The system directly connects the person who lost the item with the person who found it.

Users login using Email OTP verification to prevent fake posts and spam entries.

---

## ✨ Unique Features
- Secure login using Email OTP
- Post Lost or Found items
- Only owner can delete their post
- One-click contact owner (email or phone)
- Live search items
- Category filtering (Mobile, Keys, Books, Chargers, Bluetooth, etc.)
- Dark themed glassmorphism UI
- Cursor glow interactive effect
- Delete confirmation warning
- Auto-generated email message while contacting owner

---

## 🧰 Tech Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite3

### Authentication
- Gmail SMTP Email OTP verification

---

## ⚙️ How to Run the Project

### 1. Install Python
Download Python from:
https://www.python.org/downloads/

---

### 2. Install Flask
Open terminal inside project folder and run:

pip install flask

---

### 3. Enable Gmail App Password
1. Turn ON 2-Step Verification in Gmail
2. Go to Google Account → Security → App Passwords
3. Generate Mail app password
4. Paste in `app.py`:

sender_email = "yourgmail@gmail.com"
app_password = "16_digit_password"

---

### 4. Run Server

python app.py

Open browser and go to:

http://127.0.0.1:5000/

---

## 🎮 How to Use
1. Login using email
2. Enter OTP received in mail
3. Post a lost or found item
4. Other users contact owner
5. Owner deletes post after recovery

---

## 📚 Learnings
- Flask routing and sessions
- Email authentication using SMTP
- Database handling using SQLite
- UI design with Bootstrap and CSS
- Search and filtering with JavaScript

---

## ⚠ Challenges Faced
- Gmail SMTP authentication errors
- OTP verification handling
- Restricting delete access to owner
- UI visibility issues in dark mode
- Dynamic email compose links

---

## 🎥 Demo Video


---

## 🌐 Hosted Link
(Add deployment link if available)

---

## 🚀 Future Improvements
- Image upload for items
- AI matching of lost and found objects
- Mobile app version
- Notification system
- Admin dashboard

---

## 📌 Conclusion
Campus Recovery Portal digitizes the college lost-and-found system.  
It improves recovery chances, saves time, and helps students reconnect with their belongings through a secure and organized platform.

