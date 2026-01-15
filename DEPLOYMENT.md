# PulseCheck AI - Streamlit Deployment Guide

## Local Development Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key Locally
Create a `.env` file in the project root (already created):
```
GOOGLE_API_KEY=your-api-key-here
```

**Important:** The `.env` file is in `.gitignore` and will NOT be committed to GitHub.

### 3. Run Locally
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

---

## Streamlit Cloud Deployment

### 1. Push Code to GitHub
Ensure `.env` and `.streamlit/secrets.toml` are in `.gitignore` (already configured).

```bash
git add .
git commit -m "Initial PulseCheck AI setup"
git push origin main
```

### 2. Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Select your GitHub repository and branch
4. Set the main file path to `app.py`
5. Click "Deploy"

### 3. Add Secrets on Streamlit Cloud

After deployment:
1. Go to your app's settings (gear icon)
2. Click "Secrets"
3. Add your API key in TOML format:
```toml
GOOGLE_API_KEY = "AIzaSyCYgPZ9JkicbwGjRUqmCvvaVS6WDYSyAfo"
```

4. Save and the app will automatically redeploy

---

## Security Best Practices

✅ **What we've done:**
- API key stored in `.env` (local development only)
- `.env` file added to `.gitignore` (never committed)
- Streamlit Secrets used for production (Streamlit Cloud)
- `app.py` checks both sources securely

✅ **Never:**
- Commit `.env` file to GitHub
- Hardcode API keys in source code
- Share API keys in chat or emails

---

## File Structure
```
PulseCheck/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── .env                            # Local API key (NOT committed)
├── .gitignore                      # Prevents .env from being committed
├── .streamlit/
│   ├── config.toml                # Streamlit configuration
│   └── secrets.toml.example        # Template for secrets
└── DEPLOYMENT.md                   # This file
```

---

## Troubleshooting

### App won't start locally
- Ensure `.env` file exists with `GOOGLE_API_KEY`
- Run `pip install -r requirements.txt`
- Check Python version (3.8+)

### API key not found on Streamlit Cloud
- Verify secrets are added in app settings
- Secrets are case-sensitive
- Redeploy after adding secrets

### Import errors
- Delete `__pycache__` folder
- Reinstall dependencies: `pip install --upgrade -r requirements.txt`
