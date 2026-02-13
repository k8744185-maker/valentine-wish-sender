# Quick Setup Guide 🚀

## Step 1: Create Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new sheet
3. In the first row, add these headers:
   ```
   Sender Name | Sender Email | Partner Name | Partner Email | Unique Code
   ```
4. Copy the Sheet ID from URL (the long code between `/d/` and `/edit`)
   - Example: `https://docs.google.com/spreadsheets/d/1ABC123xyz/edit`
   - Sheet ID = `1ABC123xyz`

## Step 2: Get Google Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select existing)
3. Enable Google Sheets API:
   - Click "APIs & Services" → "Library"
   - Search "Google Sheets API"https://console.cloud.google.com/
   - Click "Enable"
4. Create Service Account:
   - Click "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "Service Account"
   - Fill name and click "Create"
5. Download credentials:
   - Click on created service account
   - Go to "Keys" tab
   - Click "Add Key" → "Create new key"
   - Select "JSON"
   - Download and save as `credentials.json` in this folder
6. Share your Google Sheet:
   - Open your Google Sheet
   - Click "Share"
   - Copy the email from `credentials.json` (client_email)
   - Share the sheet with this email (Editor access)

## Step 3: Setup Gmail (OPTIONAL)

**Note:** Email is optional! Without email setup, the app will generate the link and you can share it manually.

To enable automatic email sending:
1. Enable 2-Step Verification in your Google Account
2. Create App Password:
   - Go to Google Account → Security
   - Search "App passwords"
   - Create new app password for "Mail"
   - Copy the 16-character password

## Step 4: Update .env file

Edit the `.env` file with your values:

```env
EMAIL_USER=your-gmail@gmail.com
EMAIL_PASSWORD=xxxx-xxxx-xxxx-xxxx  (16 character app password)
GOOGLE_CREDENTIALS_PATH=./credentials.json
GOOGLE_SHEET_ID=your-sheet-id-here
BASE_URL=http://localhost:8501
```

## Step 5: Run the App

```bash
streamlit run app.py
```

## Files Needed:
✅ `.env` - Environment variables (already created)
❌ `credentials.json` - Google Service Account key (download from step 2)

---

**Current Status:**
- ✅ .env file created
- ❌ credentials.json missing - Follow Step 2 above (REQUIRED)
- ⚠️ Email not configured - Follow Step 3 above (OPTIONAL - app works without it)
- ❌ Sheet ID not set - Follow Step 1 above (REQUIRED)

**Quick Start:** Setup only Steps 1 & 2 to test the app. Email can be added later!
