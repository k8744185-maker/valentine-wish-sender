# 🚀 Deploy Your Valentine's Wish Sender Online (FREE!)

## Quick Start Guide

### Step 1: Push to GitHub (5 minutes)

```bash
cd /home/venkadesan.k/Documents/Personalcode

# Initialize git
git init
git add .
git commit -m "Initial commit: Valentine's Wish Sender"

# Create repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/valentine-wish-sender.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud (2 minutes)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `valentine-wish-sender`
5. Main file: `app.py`
6. Click "Advanced settings" → "Secrets"

Add these secrets:
```toml
EMAIL_USER = "k8744185@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
GOOGLE_SHEET_ID = "1PSZdOhikbe5C2QbsicpXDKESY7qj_pZ9k7W3td90ebE"
BASE_URL = "https://your-app-name.streamlit.app"
GOOGLE_CREDENTIALS_PATH = "credentials.json"

# Paste your Google Service Account JSON:
[gcp_service_account]
type = "service_account"
project_id = "personaldata-487210"
# ... rest of credentials.json content
```

7. Click "Deploy!"

### Step 3: Your App is LIVE! 🎉

Your app will be available at:
```
https://your-app-name.streamlit.app
```

Share this URL with anyone! It's publicly accessible.

---

## 📱 To Update Your App

```bash
# Make changes to app.py
git add .
git commit -m "Updated features"
git push
```

Streamlit Cloud auto-deploys in 1-2 minutes!

---

## 🔐 Security Tips

✅ **DO:**
- Use Streamlit Secrets for sensitive data
- Keep credentials.json in secrets only
- Use .gitignore for .env files

❌ **DON'T:**
- Commit .env to GitHub
- Share credentials.json publicly
- Hardcode passwords in code

---

## 🆓 Free Forever!

Streamlit Cloud free tier includes:
- ✅ Unlimited public apps
- ✅ 1 GB resources per app
- ✅ Auto-deployment from GitHub
- ✅ Custom subdomain
- ✅ HTTPS included

Perfect for your Valentine's Wish Sender! 💕

---

## 🆘 Need Help?

1. **Check deployment logs** in Streamlit Cloud
2. **Verify secrets** are correctly formatted
3. **Test locally** with `streamlit run app.py`
4. **Check GitHub** repo has all files

Your app is ready to go live! 🚀
