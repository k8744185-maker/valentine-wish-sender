# 🚀 வலைதளத்தை ஆன்லைனில் வெளியிடுவது (Deploy Online)

## Step 1: GitHub Repository உருவாக்குங்கள்

### 1.1 GitHub Account உருவாக்கவும்
- https://github.com இல் sign up செய்யுங்கள் (இலவசம்)

### 1.2 Repository உருவாக்கவும்
```bash
cd /home/venkadesan.k/Documents/Personalcode
git init
git add .
git commit -m "Valentine's Day Wish Sender App"
```

GitHub-இல்:
1. "New Repository" கிளிக் செய்யுங்கள்
2. பெயர்: `valentine-wish-sender`
3. Public select செய்யுங்கள்
4. Create repository கிளிக் செய்யுங்கள்

பிறகு terminal-இல்:
```bash
git remote add origin https://github.com/YOUR_USERNAME/valentine-wish-sender.git
git branch -M main
git push -u origin main
```

---

## Step 2: Streamlit Cloud-இல் Deploy செய்யுங்கள் (இலவசம்!)

### 2.1 Streamlit Cloud Account
1. https://share.streamlit.io இல் செல்லுங்கள்
2. GitHub account உடன் sign in செய்யுங்கள்
3. "New app" கிளிக் செய்யுங்கள்

### 2.2 App Settings
- **Repository:** `YOUR_USERNAME/valentine-wish-sender`
- **Branch:** `main`
- **Main file path:** `app.py`

### 2.3 Secrets Configuration
"Advanced settings" → "Secrets" இல் கீழ்கண்டவற்றை add செய்யுங்கள்:

```toml
EMAIL_USER = "k8744185@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
GOOGLE_SHEET_ID = "1PSZdOhikbe5C2QbsicpXDKESY7qj_pZ9k7W3td90ebE"
BASE_URL = "https://your-app-name.streamlit.app"
GOOGLE_CREDENTIALS_PATH = "credentials.json"
```

### 2.4 Upload credentials.json
"Advanced settings" → "Secrets" இன் கீழே:
```toml
# Google Service Account Credentials
[gcp_service_account]
# உங்கள் credentials.json-இன் content-ஐ paste செய்யுங்கள்
```

### 2.5 Deploy!
- "Deploy!" பட்டனை கிளிக் செய்யுங்கள்
- 2-3 நிமிடங்களில் உங்கள் app live ஆகிவிடும்!

---

## Step 3: உங்கள் Live URL

உங்கள் app இப்போது இதில் available:
```
https://your-app-name.streamlit.app
```

இந்த link-ஐ யாருக்கு வேண்டுமானாலும் share செய்யலாம்! 🎉

---

## 🔧 Update செய்வது எப்படி?

Code மாற்றினால்:
```bash
git add .
git commit -m "Updated features"
git push
```

Streamlit Cloud தானாகவே update ஆகிவிடும்!

---

## ⚠️ முக்கியமான குறிப்புகள்

1. **.env** file-ஐ GitHub-இல் upload செய்யாதீர்கள் (security!)
2. **credentials.json**-ஐ Streamlit Secrets-இல் மட்டுமே add செய்யுங்கள்
3. Gmail App Password உருவாக்க:
   - Google Account → Security → 2-Step Verification
   - App passwords → Generate new password

---

## 💝 வெற்றி!

உங்கள் Valentine's Wish Sender இப்போது:
- ✅ உலகம் முழுவதும் accessible
- ✅ இலவசம்
- ✅ தானாக update ஆகும்
- ✅ Professional URL

யாருக்கு வேண்டுமானாலும் link share செய்யுங்கள்! 🎉💕
