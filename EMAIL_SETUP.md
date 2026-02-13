# Email Setup Guide 📧

## Step 1: Enable 2-Step Verification

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Click on "2-Step Verification"
3. Follow the steps to enable it (you'll need your phone)

## Step 2: Create App Password

1. After enabling 2-Step Verification, go back to [Security](https://myaccount.google.com/security)
2. Scroll down to "How you sign in to Google"
3. Click on "2-Step Verification"
4. Scroll to the bottom and click on "App passwords"
5. Select "Mail" and your device
6. Click "Generate"
7. Copy the 16-character password (format: xxxx xxxx xxxx xxxx)

## Step 3: Update .env File

Open `.env` file and update:

```env
EMAIL_USER=k8744185@gmail.com
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx  # Paste your 16-character app password here
```

**Remove spaces from the app password!** Example:
- If you got: `abcd efgh ijkl mnop`
- Use: `abcdefghijklmnop`

## Step 4: Restart Streamlit

Stop the current Streamlit app (Ctrl+C) and run again:
```bash
streamlit run app.py
```

## Test

Submit the form and the email will be sent automatically to the partner's email! ✅

---

**Troubleshooting:**
- If still not working, make sure 2-Step Verification is ON
- Check that you copied the app password correctly (no spaces)
- Make sure you're using the correct Gmail address
