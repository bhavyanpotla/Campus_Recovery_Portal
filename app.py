import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "findit_secret_key_123"


# ---------- DATABASE SETUP ----------
def init_db():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            location TEXT,
            status TEXT,
            contact TEXT,
            category TEXT,
            owner TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()


# ---------- EMAIL OTP ----------
def send_email_otp(receiver_email, otp):

    sender_email = "collegerecovery9@gmail.com"
    app_password = "dqnzjosyurrlqewt"

    subject = "FindIt Login OTP"
    body = f"Your FindIt verification OTP is: {otp}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


# ---------- HOME ----------
@app.route('/')
def home():

    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    conn.close()

    return render_template('index.html', items=items, email=session.get('email'))


# ---------- ADD ITEM ----------
@app.route('/add', methods=['POST'])
def add_item():

    if not session.get('logged_in'):
        return redirect(url_for('login'))

    name = request.form['name']
    description = request.form['description']
    location = request.form['location']
    status = request.form['status']
    contact = request.form['contact']
    category = request.form['category']   # NEW
    owner = session.get('email')

    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO items (name, description, location, status, contact, category, owner)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, description, location, status, contact, category, owner))

    conn.commit()
    conn.close()

    return redirect('/')


# ---------- DELETE (OWNER ONLY) ----------
@app.route('/delete/<int:item_id>')
def delete_item(item_id):

    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    c.execute("SELECT owner FROM items WHERE id=?", (item_id,))
    item = c.fetchone()

    if item is None:
        conn.close()
        return redirect('/')

    owner_email = item[0]

    if owner_email != session.get('email'):
        conn.close()
        return "<h3 style='color:red;text-align:center;margin-top:40px;'>⚠️ You cannot delete another user's post.</h3>"

    c.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

    return redirect('/')


# ---------- LOGIN ----------
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/send_otp', methods=['POST'])
def send_otp():

    email = request.form['email']
    otp = random.randint(1000, 9999)

    session['otp'] = str(otp)
    session['email'] = email

    send_email_otp(email, otp)

    return render_template("login.html",
                           message="OTP sent to your email (check spam if not received).",
                           saved_email=email)


@app.route('/verify_otp', methods=['POST'])
def verify_otp():

    user_otp = request.form['user_otp']

    if 'otp' in session and user_otp == session['otp']:
        session['logged_in'] = True
        return redirect(url_for('home'))

    return render_template("login.html",
                           error="Invalid OTP. Try again.",
                           saved_email=session.get('email'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ---------- DEMO DATA (RUN ONLY ONCE) ----------
def insert_demo_data():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()

    # prevent duplicate insertion
    c.execute("SELECT COUNT(*) FROM items")
    count = c.fetchone()[0]

    if count > 0:
        print("Demo data already exists")
        conn.close()
        return

    demo_items = [

        # bhavyan (2 items)
        ("Realme wired bluetooth", "reported item", "library", "Found", "bhavyanpotla@gmail.com", "Bluetooth", "bhavyanpotla@gmail.com"),
        ("1+ NORD CE5 mobile case", "reported item", "ab2 101", "Lost", "bhavyanpotla@gmail.com", "Mobile Case", "bhavyanpotla@gmail.com"),

        # hemanth (3 items)
        ("Pods", "reported item", "ab1 101", "Lost", "hemanth.yuki5@gmail.com", "Bluetooth", "hemanth.yuki5@gmail.com"),
        ("Iphone charger", "reported item", "canteen", "Found", "hemanth.yuki5@gmail.com", "Charger", "hemanth.yuki5@gmail.com"),
        ("College ID Card", "reported item", "main block", "Lost", "hemanth.yuki5@gmail.com", "ID Card", "hemanth.yuki5@gmail.com"),

        # suhaas (remaining)
        ("Classmate black notebook", "reported item", "AI LAB", "Found", "suhaas.sarabu@gmail.com", "Books", "suhaas.sarabu@gmail.com"),
        ("Yamaha bike keys", "reported item", "parking", "Lost", "suhaas.sarabu@gmail.com", "Keys", "suhaas.sarabu@gmail.com"),
        ("Scientific calculator", "reported item", "exam hall", "Found", "suhaas.sarabu@gmail.com", "Calculator", "suhaas.sarabu@gmail.com")
    ]

    for item in demo_items:
        c.execute("""
            INSERT INTO items (name, description, location, status, contact, category, owner)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, item)

    conn.commit()
    conn.close()
    print("Demo data inserted successfully!")

if __name__ == "__main__":
    insert_demo_data()
    app.run(debug=True)

