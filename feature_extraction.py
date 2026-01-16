import re
import tldextract
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # URL length
    features.append(len(url))

    # HTTPS
    features.append(1 if url.startswith("https") else 0)

    # Penalize HTTP
    if not url.startswith("https"):
        features[1] = 0

    # IP address in URL
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)

    # @ symbol
    features.append(1 if "@" in url else 0)

    # Hyphen in domain
    features.append(1 if "-" in url else 0)

    # Number of dots
    features.append(url.count("."))

    # URL shortener
    shorteners = ["bit.ly", "tinyurl", "goo.gl"]
    features.append(1 if any(s in url for s in shorteners) else 0)

    # Login + Brand keywords
    keywords = [
        "login", "verify", "secure", "account",
        "update", "signin", "bank", "confirm",
        "paypal", "google", "facebook", "amazon"
    ]
    features.append(1 if any(k in url.lower() for k in keywords) else 0)

    # Domain age (heuristic)
    features.append(10 if "-" in url or "login" in url else 500)

    return features
