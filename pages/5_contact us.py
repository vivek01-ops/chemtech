import streamlit as st
import smtplib
from email.message import EmailMessage
import os

# Function to send email
def send_email(name, email, message):
    # Replace with your email and credentials
    sender_email = os.getenv("SENDER_EMAIL")  # Use environment variables for email credentials
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("chaudharivivek.512@gmail.com")  # The email where you'll receive responses

    # Create email content
    msg = EmailMessage()
    msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg['Subject'] = f"New Contact Form Submission from {name}"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Sending email using Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Failed to send email. Error: {e}")
        return False

# Streamlit UI for the Contact Us form
def contact_form():
    st.title("Contact Us")

    # Create form fields
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        # Submit button
        submit_button = st.form_submit_button("Submit")

    # Handle form submission
    if submit_button:
        if name and email and message:
            if send_email(name, email, message):
                st.success("Thank you for reaching out! Your message has been sent.")
        else:
            st.error("Please fill out all the fields.")

# Display the Contact Us form
contact_form()
