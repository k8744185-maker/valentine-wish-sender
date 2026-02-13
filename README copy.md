# Valentine's Day Wish Sender 💕

A beautiful Streamlit web application to send personalized Valentine's Day wishes via email with unique links. All data is automatically saved to Google Sheets.

## Features

✅ User-friendly form to collect sender and partner details  
✅ Generates unique links for each wish  
✅ Sends beautiful HTML emails to partners  
✅ Displays personalized Valentine's wishes  
✅ Automatically saves all data to Google Sheets  
✅ Beautiful animated Valentine's Day theme  
✅ Built with Python & Streamlit

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Email (Gmail)

1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Generate an App Password:
   - Go to Security → 2-Step Verification → App passwords
   - Select "Mail" and your device
   - Copy the 16-character password

### 3. Configure Google Sheets API

#### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Sheets API:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

#### Step 2: Create Service Account

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "Service Account"
3. Fill in the details and click "Create"
4. Click on the created service account
5. Go to "Keys" tab
6. Click "Add Key" → "Create new key"
7. Choose "JSON" format
8. Download the JSON file and save it as `credentials.json` in your project root

#### Step 3: Create Google Sheet

1. Create a new Google Sheet
2. Add headers in the first row: `Sender Name | Sender Email | Partner Name | Partner Email | Unique Code`
3. Copy the Sheet ID from the URL:
   - URL format: `https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit`
4. Share the sheet with the service account email:
   - Open the `credentials.json` file
   - Copy the `client_email` value
   - Share your Google Sheet with this email (Editor access)

### 4. Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your values:
   ```env
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-16-char-app-password
   GOOGLE_CREDENTIALS_PATH=./credentials.json
   GOOGLE_SHEET_ID=your-google-sheet-id
   BASE_URL=http://localhost:8501
   ```

### 5. Run the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`

## Usage

1. Open `http://localhost:3000` in your browser
2. Fill in your details (name and email)
3. Fill in your partner's details (name and email)
4. Click "Generate & Send Link"
5. A unique link will be generated and sent to your partner's email
6. All data is automatically saved to Google Sheets

## Project Structure

```
valentine-wish-sender/
├── public/
│   app.py               # Main Streamlit application
├── wish_page.py         # Valentine's wish display page
├── requirements.txt     # Python dnvironment variables template
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## API Endpoints

### POST `/api/generate-wish`
Generates a unique wish link, saves data to Google Sheets, and sends email.

**RHow It Works

1. **Main Form (`app.py`)**: User fills in sender and partner details
2. **Generate Code**: System generates unique 6-character code
3. **Save to Sheets**: Data saved to Google Sheets automatically
4. **Send Email**: Beautiful HTML email sent to partner with wish link
5. **Wish Display (`wish_page.py`)**: Partner clicks link and sees personalized wish
1. Update `BASE_URL` in `.env` to your production domain
2. Use a proper email service (SendGrid, AWS SES, etc.) for better deliverability
3. Consider using environment variables from your hosting platform
4. Ensure `credentials.json` is securely stored (not in version control)

### Recommended Hosting Platforms:
- Heroku
- Railway
- Render
- Google Cloud Run
- AWS Elastic Beanstalk

## Security Notes

⚠️ **IMPORTANT:**
- Never commit `.env` or `credentials.json` to version control
- Use environment variables in production
- Keep your Google Service Account credentials secure
- Use App Passwords for Gmail (never use your actual password)

## Troubleshooting

### Email not sending?
- Check your Gmail App Password is correct
- Ensure 2-Step Verification is enabled
- Check if "Less secure app access" is needed (not recommended)

### Google Sheets not working?
- Verify the service account email has access to your sheet
- Check the Sheet ID is correct
- Ensure Google Sheets API is enabled in your project

### Link not working?
- Check `BASE_URL` in `.env` matches your actual URL
- Streamlit Community Cloud (Free!)
- Heroku
- Railway
- Render
- Google Cloud Run to use and modify!

## Support

For issues or questions, please check the troubleshooting section above.

---

Made with ❤️ for Valentine's Day 2026
