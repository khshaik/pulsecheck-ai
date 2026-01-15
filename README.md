# PulseCheck AI 🚀

An intelligent interview preparation assistant powered by Google Generative AI and Streamlit.

## Features

- 🤖 AI-powered interview coaching
- 💬 Real-time conversational responses
- 🎯 Personalized feedback and guidance
- 🚀 Built with Streamlit for easy deployment

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PulseCheck.git
   cd PulseCheck
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   # Edit .streamlit/secrets.toml and add your Google API key
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

## Deployment

### Deploy on Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy PulseCheck AI"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your repository and branch
   - Set main file to `app.py`
   - Click "Deploy"

3. **Add Secrets**
   - Go to app settings (gear icon)
   - Click "Secrets"
   - Add your Google API key:
     ```toml
     GOOGLE_API_KEY = "your-api-key-here"
     ```
   - Save and redeploy

## Configuration

### Environment Variables

The app supports two ways to configure the Google API key:

- **Local Development**: Use `.env` file (not committed to git)
- **Production (Streamlit Cloud)**: Use Streamlit Secrets

### Streamlit Configuration

Customize the app appearance in `.streamlit/config.toml`:
- Theme colors
- Font settings
- Logger level
- Client settings

## Project Structure

```
PulseCheck/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
├── README.md                        # This file
├── DEPLOYMENT.md                   # Detailed deployment guide
├── .env                            # Local environment variables (not committed)
├── .gitignore                      # Git ignore rules
└── .streamlit/
    ├── config.toml                 # Streamlit configuration
    └── secrets.toml.example        # Secrets template
```

## Security

- ✅ API keys stored in environment variables
- ✅ `.env` file excluded from git
- ✅ Streamlit Secrets for production
- ✅ No hardcoded credentials in source code

## Requirements

- Python 3.8+
- Google API Key (get one [here](https://makersuite.google.com/app/apikey))
- Streamlit Cloud account (optional, for deployment)

## Troubleshooting

### API Key Not Found
- Ensure `.env` file exists locally with `GOOGLE_API_KEY`
- On Streamlit Cloud, verify secrets are added in app settings

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

## License

MIT License - feel free to use this project for your own purposes.

## Support

For issues and questions, please create an issue in the GitHub repository.
