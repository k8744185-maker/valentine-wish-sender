import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import os
from dotenv import load_dotenv
from PIL import Image
import io
import base64

# Love messages collection
LOVE_MESSAGES = [
    {
        "msg1": "On this special day of love and romance, I want you to know how much you mean to me.",
        "msg2": "Every moment with you is a treasure, every smile you share lights up my world.",
        "msg3": "You make every day feel like Valentine's Day with your warmth, kindness, and love.",
        "msg4": "Thank you for being the amazing person you are. Here's to many more beautiful moments together! 🌹"
    },
    {
        "msg1": "Happy Valentine's Day to the one who makes my heart skip a beat!",
        "msg2": "Your love is the greatest gift I've ever received, and I cherish every moment we share.",
        "msg3": "You bring so much joy and happiness into my life, and I'm grateful for you every single day.",
        "msg4": "I love you more than words can express. Here's to our beautiful journey together! 💖"
    },
    {
        "msg1": "To my dearest Valentine, you are my sunshine on cloudy days and my comfort in stormy weather.",
        "msg2": "Your love fills my life with happiness, laughter, and endless beautiful memories.",
        "msg3": "Every day with you is an adventure, and I wouldn't want to share it with anyone else.",
        "msg4": "Thank you for being my partner, my love, and my best friend. Forever yours! 💕"
    },
    {
        "msg1": "This Valentine's Day, I want to remind you of how special you are to me.",
        "msg2": "Your smile brightens my darkest days, and your love gives me strength to face any challenge.",
        "msg3": "I'm so lucky to have you in my life, and I promise to cherish you today and always.",
        "msg4": "You are my forever Valentine! Here's to endless love and countless happy moments! 🌹❤️"
    },
    {
        "msg1": "My beloved, you are the reason my heart sings and my soul dances with joy!",
        "msg2": "In your eyes, I found my home. In your heart, I found my love. In your soul, I found my mate.",
        "msg3": "Every beat of my heart whispers your name, and every breath I take is filled with thoughts of you.",
        "msg4": "You complete me in ways I never knew possible. Happy Valentine's Day, my love! 💝"
    },
    {
        "msg1": "To the love of my life, you make everything more beautiful just by being in it.",
        "msg2": "Your love is like a beautiful melody that plays in my heart all day long.",
        "msg3": "I fall in love with you more and more each day, and I can't imagine my life without you.",
        "msg4": "Thank you for loving me and letting me love you. You're my forever! 💗"
    }
]

# Load environment variables
load_dotenv()

# Try Streamlit secrets first, then fall back to .env
def get_env(key, default=""):
    """Get environment variable from Streamlit secrets or .env"""
    if hasattr(st, 'secrets') and key in st.secrets:
        return st.secrets[key]
    return os.getenv(key, default)

# Page configuration
st.set_page_config(
    page_title="Valentine's Day Wish Sender",
    page_icon="💕",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    .main {
        background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 50%, #6c5b7b 100%);
        padding: 2rem 1rem !important;
    }
    .stApp {
        background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 50%, #6c5b7b 100%);
    }
    
    /* Main container styling */
    .block-container {
        max-width: 800px !important;
        padding: 2rem 1rem !important;
    }
    
    /* Section headers */
    h3 {
        color: #ff1744 !important;
        font-size: 1.4em !important;
        font-weight: 600 !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem !important;
        border-bottom: 3px solid #ff1744 !important;
    }
    
    /* Input fields - white background, clean look */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: white !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        color: #333 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #ff1744 !important;
        box-shadow: 0 0 0 3px rgba(255, 23, 68, 0.1) !important;
        outline: none !important;
    }
    
    /* Labels styling */
    .stTextInput label, .stTextArea label, .stRadio label, .stFileUploader label {
        color: #333 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Radio buttons */
    .stRadio > div {
        background: white !important;
        padding: 1rem !important;
        border-radius: 12px !important;
        border: 2px solid #e0e0e0 !important;
    }
    
    .stRadio > div > label > div {
        font-size: 1rem !important;
        color: #333 !important;
    }
    
    /* File uploader */
    .stFileUploader > div {
        background: white !important;
        border: 3px dashed #ff1744 !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stFileUploader > div:hover {
        border-color: #c51162 !important;
        background: #fff5f7 !important;
    }
    
    .stFileUploader label {
        color: #ff1744 !important;
        font-weight: 600 !important;
    }
    
    /* Main title */
    h1 {
        color: #ff1744 !important;
        text-align: center !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2) !important;
        font-size: 2.5em !important;
        margin-bottom: 0.5rem !important;
    }
    
    .subtitle {
        text-align: center;
        color: white !important;
        margin-bottom: 2rem;
        font-size: 1.2rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
        font-weight: 400;
    }
    
    /* Submit button */
    .stButton>button {
        background: linear-gradient(135deg, #ff1744 0%, #f50057 50%, #c51162 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 1rem 2rem !important;
        border-radius: 30px !important;
        border: none !important;
        width: 100% !important;
        font-size: 1.2em !important;
        box-shadow: 0 6px 20px rgba(255, 23, 68, 0.4) !important;
        transition: all 0.3s ease !important;
        margin-top: 2rem !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-4px) scale(1.03) !important;
        box-shadow: 0 8px 30px rgba(255, 23, 68, 0.6) !important;
    }
    
    /* Success message */
    .success-box {
        background: white !important;
        color: #155724 !important;
        padding: 2rem !important;
        border-radius: 15px !important;
        border: 3px solid #28a745 !important;
        margin-top: 1.5rem !important;
        box-shadow: 0 6px 20px rgba(40, 167, 69, 0.3) !important;
    }
    
    .success-box h3 {
        color: #28a745 !important;
        border: none !important;
        margin-top: 0 !important;
    }
    
    /* Error message */
    .stAlert {
        background: white !important;
        border-radius: 12px !important;
        padding: 1rem 1.5rem !important;
        border-left: 5px solid #dc3545 !important;
    }
    
    /* Info/Warning messages */
    .stInfo, .stWarning {
        background: white !important;
        border-radius: 12px !important;
        padding: 1rem 1.5rem !important;
    }
    
    /* Spacing helpers */
    .stMarkdown {
        margin-bottom: 0.5rem !important;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main { padding: 1rem 0.5rem !important; }
        h1 { font-size: 1.8em !important; }
        .subtitle { font-size: 1em !important; }
        h3 { font-size: 1.2em !important; }
        .stButton>button { font-size: 1em !important; padding: 0.8rem 1.5rem !important; }
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            font-size: 0.95rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Functions
def generate_unique_code():
    """Generate a random 6-character unique code"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def compress_image(image_bytes, max_width=800, quality=70):
    """
    Compress and resize image to reduce base64 size
    Args:
        image_bytes: Original image bytes
        max_width: Maximum width in pixels
        quality: JPEG quality (1-100)
    Returns:
        Compressed image as base64 string
    """
    try:
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Save to bytes with compression
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=quality, optimize=True)
        output.seek(0)
        
        # Convert to base64
        img_base64 = base64.b64encode(output.read()).decode()
        return img_base64
    except Exception as e:
        st.error(f"Error compressing image: {e}")
        return None

def save_to_google_sheets(sender_name, sender_email, partner_name, partner_email, unique_code, custom_message="", image_data=""):
    """Save data to Google Sheets"""
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            get_env('GOOGLE_CREDENTIALS_PATH', 'credentials.json'),
            scope
        )
        
        client = gspread.authorize(credentials)
        sheet = client.open_by_key(get_env('GOOGLE_SHEET_ID'))
        worksheet = sheet.sheet1
        # Columns: Sender Name | Sender Email | Partner Name | Partner Email | Code | Custom Message | Image Data | Viewed
        worksheet.append_row([sender_name, sender_email, partner_name, partner_email, unique_code, custom_message, image_data, "No"])
        return True
    except Exception as e:
        st.error(f"Error saving to Google Sheets: {str(e)}")
        return False

def send_notification_to_sender(sender_name, sender_email, partner_name):
    """Send notification email to sender when partner views the wish"""
    try:
        email_user = get_env('EMAIL_USER')
        email_password = get_env('EMAIL_PASSWORD')
        
        if not email_user or not email_password or email_user == 'your-email@gmail.com':
            return None  # Email not configured
        
        msg = MIMEMultipart('alternative')
        msg['From'] = email_user
        msg['To'] = sender_email
        msg['Subject'] = f"💕 {partner_name} viewed your Valentine's wish!"
        
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%); padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
                <h1 style="color: #ff1744; text-align: center;">💕 Great News!</h1>
                <h2 style="color: #333; text-align: center;">Your Valentine's wish was viewed!</h2>
                <p style="font-size: 18px; color: #555; line-height: 1.6;">
                    Hi {sender_name},
                </p>
                <p style="font-size: 18px; color: #555; line-height: 1.6;">
                    <strong>{partner_name}</strong> just opened your Valentine's Day wish! 💖
                </p>
                <p style="font-size: 16px; color: #666; line-height: 1.6;">
                    We hope your heartfelt message brings a smile to their face! ❤️
                </p>
                <div style="text-align: center; margin-top: 30px;">
                    <p style="font-size: 14px; color: #999;">With love,<br>Valentine's Wish Sender</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_user, email_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        # Silently fail, don't show error to partner
        return False

def send_email(sender_name, partner_name, partner_email, wish_link):
    """Send email with Valentine's wish link"""
    try:
        email_user = get_env('EMAIL_USER')
        email_password = get_env('EMAIL_PASSWORD')
        
        if not email_user or not email_password or email_user == 'your-email@gmail.com':
            return None  # Email not configured
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"💕 {sender_name} has sent you a Valentine's Day wish!"
        msg['From'] = f"Valentine's Wish <{email_user}>"
        msg['To'] = partner_email
        
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #ffeef8, #fff0f6); border-radius: 10px;">
                <h1 style="color: #ff1744; text-align: center;">💖 Happy Valentine's Day! 💖</h1>
                <p style="font-size: 18px; color: #333; text-align: center;">
                    <strong>{sender_name}</strong> has sent you a special Valentine's Day wish!
                </p>
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{wish_link}" 
                       style="background: linear-gradient(135deg, #ff1744, #f50057); 
                              color: white; 
                              padding: 15px 30px; 
                              text-decoration: none; 
                              border-radius: 25px; 
                              font-size: 16px;
                              display: inline-block;">
                        💕 View Your Valentine's Wish 💕
                    </a>
                </div>
                <p style="text-align: center; color: #666; font-size: 14px;">
                    Click the button above to see your personalized message!
                </p>
                <p style="text-align: center; color: #999; font-size: 12px; margin-top: 30px;">
                    Made with ❤️ on Valentine's Day 2026
                </p>
            </body>
        </html>
        """
        
        part = MIMEText(html, 'html')
        msg.attach(part)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_user, email_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

def get_wish_from_sheets(code):
    """Get wish data from Google Sheets"""
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            get_env('GOOGLE_CREDENTIALS_PATH', 'credentials.json'),
            scope
        )
        
        client = gspread.authorize(credentials)
        sheet = client.open_by_key(get_env('GOOGLE_SHEET_ID'))
        worksheet = sheet.sheet1
        
        all_values = worksheet.get_all_values()
        
        for row_index, row in enumerate(all_values[1:], start=2):
            if len(row) >= 5 and row[4] == code:
                # Get custom message and ensure it's not empty string
                custom_msg = row[5].strip() if len(row) > 5 else ""

                return {
                    'sender_name': row[0], 
                    'sender_email': row[1],
                    'partner_name': row[2],
                    'custom_message': custom_msg,
                    'image_data': row[6] if len(row) > 6 else "",
                    'viewed': row[7] if len(row) > 7 else "No",
                    'row_index': row_index
                }
        return None
    except Exception as e:
        return {'error': str(e)}

def mark_as_viewed_and_notify(code, wish_data):
    """Mark wish as viewed in Google Sheets and send notification"""
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            get_env('GOOGLE_CREDENTIALS_PATH', 'credentials.json'),
            scope
        )
        
        client = gspread.authorize(credentials)
        sheet = client.open_by_key(get_env('GOOGLE_SHEET_ID'))
        worksheet = sheet.sheet1
        
        # Update viewed status
        row_index = wish_data.get('row_index')
        if row_index:
            worksheet.update_cell(row_index, 8, "Yes")  # Column H = Viewed
        
        # Send notification email to sender
        send_notification_to_sender(
            wish_data['sender_name'], 
            wish_data['sender_email'], 
            wish_data['partner_name']
        )
        
        return True
    except Exception as e:
        # Silently fail
        return False

def show_wish_page():
    """Display the Valentine's wish page"""
    code = st.query_params.get("code", "")
    
    st.markdown("<h1 style='animation: pulse 2s ease-in-out infinite;'>💖 Happy Valentine's Day! 💖</h1>", unsafe_allow_html=True)
    
    if not code:
        st.error("❌ No wish code found!")
        return
    
    wish_data = get_wish_from_sheets(code)
    
    if wish_data and 'error' in wish_data:
        st.error(f"❌ Error: {wish_data['error']}")
    elif wish_data:
        # Mark as viewed and send notification (only if not already viewed)
        if wish_data.get('viewed') == "No":
            mark_as_viewed_and_notify(code, wish_data)
        
        # Build the complete message HTML
        message_content = ""
        
        # Check if custom message exists and is not empty
        if wish_data.get('custom_message') and len(wish_data.get('custom_message', '').strip()) > 0:
            # Use custom message - escape HTML entities
            custom_msg_escaped = wish_data['custom_message'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            message_content = f"<p style='font-size: 1.3em; line-height: 1.8; color: #333; margin-bottom: 15px; white-space: pre-wrap;'>{custom_msg_escaped}</p>"
        else:
            # Use random love message
            love_msg = random.choice(LOVE_MESSAGES)
            msg1_escaped = love_msg['msg1'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            msg2_escaped = love_msg['msg2'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            msg3_escaped = love_msg['msg3'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            msg4_escaped = love_msg['msg4'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            message_content = f"""<p style='font-size: 1.3em; line-height: 1.8; color: #333; margin-bottom: 15px;'>{msg1_escaped}</p>
                <p style='font-size: 1.3em; line-height: 1.8; color: #333; margin-bottom: 15px;'>{msg2_escaped}</p>
                <p style='font-size: 1.3em; line-height: 1.8; color: #333; margin-bottom: 15px;'>{msg3_escaped}</p>
                <p style='font-size: 1.3em; line-height: 1.8; color: #333; margin-bottom: 15px;'>{msg4_escaped}</p>"""
        
        # Build images HTML
        images_content = ""
        image_data_str = wish_data.get('image_data', '').strip()
        if image_data_str:
            # Split multiple images
            images = image_data_str.split("|||")
            images_content = "<div style='text-align: center; margin: 30px 0;'>"
            for img_data in images:
                img_data = img_data.strip()
                if img_data:
                    images_content += f"<img src='data:image/jpeg;base64,{img_data}' style='max-width: 85%; max-height: 400px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin: 10px;'/>"
            images_content += "</div>"
        
        # Display complete wish card as single HTML block
        partner_name_escaped = wish_data['partner_name'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        sender_name_escaped = wish_data['sender_name'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        complete_html = f"""<div style='background: linear-gradient(135deg, #fff5f7 0%, #ffe4ec 50%, #ffd6e0 100%); padding: 40px; border-radius: 25px; margin: 20px auto; max-width: 800px; border: 3px solid #ff1744; box-shadow: 0 15px 40px rgba(255, 23, 68, 0.4); position: relative; z-index: 10;'>
                <p style='font-size: 1.5em; line-height: 1.8; color: #333; margin-bottom: 25px; font-weight: 500;'>Dear <strong style='color: #ff1744; font-size: 1.1em;'>{partner_name_escaped}</strong>,</p>
                {message_content}
                {images_content}
                <p style='font-size: 1.6em; color: #ff1744; font-weight: bold; margin-top: 40px; text-align: center; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>With all my love,<br>{sender_name_escaped} 💕</p>
            </div>"""
        
        st.markdown(complete_html, unsafe_allow_html=True)
    else:
        st.error("❌ Wish not found!")
    
    st.markdown("""<p style='margin-top: 40px; text-align: center; color: white; font-style: italic; font-size: 0.9em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); position: relative; z-index: 10;'>Made with ❤️ on Valentine's Day 2026<br><span style='font-size: 0.8em;'>Celebrate love every day 💕</span></p>""", unsafe_allow_html=True)

def main():
    """Main form page"""
    st.markdown("<h1>💕 Send a Valentine's Wish 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Create a special link and send it to your loved one</p>", unsafe_allow_html=True)
    
    st.subheader("Your Details")
    sender_name = st.text_input("Your Name", placeholder="Enter your name", key="sender_name")
    sender_email = st.text_input("Your Email", placeholder="your.email@example.com", key="sender_email")
    
    st.subheader("Partner's Details")
    partner_name = st.text_input("Partner's Name", placeholder="Enter partner's name", key="partner_name")
    partner_email = st.text_input("Partner's Email", placeholder="partner.email@example.com", key="partner_email")
    
    st.subheader("Message Options")
    message_type = st.radio(
        "Choose message type:",
        ["Random Romantic Message", "Write My Own Message"],
        help="Select how you want to send your Valentine's wish",
        key="message_type"
    )
    
    # Show textbox only if "Write My Own Message" is selected
    custom_message = None  # Default to None instead of empty string
    if message_type == "Write My Own Message":
        custom_message = st.text_area(
            "Your Custom Message",
            placeholder="Write your personalized Valentine's message here...\n\nFor example:\nMy dearest love,\nYou are the sunshine of my life...",
            height=150,
            help="Write from your heart! This message will be shown to your partner.",
            key="custom_message"
        )
        # Convert empty input to None
        if not custom_message or not custom_message.strip():
            custom_message = None
    
    st.subheader("Add Photos (Optional)")
    uploaded_files = st.file_uploader(
        "Upload photos (Maximum 3 photos)",
        type=['png', 'jpg', 'jpeg'],
        help="Add romantic photos to make your wish extra special! Images will be automatically compressed.",
        key="photo_upload",
        accept_multiple_files=True
    )
    
    # Show warning if too many files
    if uploaded_files and len(uploaded_files) > 3:
        st.warning("⚠️ Please select maximum 3 photos. Only the first 3 will be used.")
        uploaded_files = uploaded_files[:3]
    
    submit_button = st.button("Generate & Send Link ❤️", use_container_width=True)
    
    if submit_button:
        if not sender_name or not sender_email or not partner_name or not partner_email:
            st.error("❌ Please fill in all fields!")
        elif "@" not in sender_email or "@" not in partner_email:
            st.error("❌ Please enter valid email addresses!")
        elif message_type == "Write My Own Message" and not custom_message:
            st.error("❌ Please write your custom message!")
        else:
            with st.spinner("Generating your special link..."):
                unique_code = generate_unique_code()
                
                # Prepare custom_message for saving (empty string if None)
                custom_msg_to_save = custom_message if custom_message else ""
                
                # Process images if uploaded
                image_data = ""
                if uploaded_files:
                    with st.spinner("Compressing photos..."):
                        # Convert all images to compressed base64
                        images_list = []
                        for uploaded_file in uploaded_files[:3]:  # Max 3 photos
                            bytes_data = uploaded_file.read()
                            compressed_img = compress_image(bytes_data, max_width=800, quality=70)
                            if compressed_img:
                                images_list.append(compressed_img)
                        
                        if images_list:
                            image_data = "|||".join(images_list)  # Use ||| as separator
                            st.success(f"✅ {len(images_list)} photo(s) compressed successfully!")
                
                sheets_success = save_to_google_sheets(
                    sender_name, sender_email, partner_name, partner_email, unique_code, custom_msg_to_save, image_data
                )
                
                if sheets_success:
                    base_url = get_env('BASE_URL', 'http://localhost:8501')
                    wish_link = f"{base_url}?code={unique_code}"
                    
                    email_success = send_email(sender_name, partner_name, partner_email, wish_link)
                    
                    if email_success:
                        st.markdown(
                            f"""
                            <div class='success-box'>
                                <h3>✅ Success!</h3>
                                <p>Valentine's wish link has been sent to <strong>{partner_email}</strong></p>
                                <p><small>Code: {unique_code}</small></p>
                                <p style="margin-top: 10px;">
                                    <a href="{wish_link}" target="_blank" style="color: #ff1744; font-weight: bold;">Preview →</a>
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f"""
                            <div class='success-box'>
                                <h3>✅ Link Generated!</h3>
                                <p>Share this link with your loved one:</p>
                                <p style="background: #fff; padding: 10px; border-radius: 5px; word-break: break-all;">
                                    <a href="{wish_link}" target="_blank">{wish_link}</a>
                                </p>
                                <p><small>Code: {unique_code}</small></p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.error("❌ Failed to save data. Check Google Sheets configuration.")

if __name__ == "__main__":
    # Debug: Show what parameters we received
    params = dict(st.query_params)
    
    # Check if code parameter exists
    if "code" in params and params["code"]:
        show_wish_page()
    else:
        main()
