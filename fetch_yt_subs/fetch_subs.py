# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "yt-dlp",
#     "requests",
# ]
# ///

import sys
import re
import requests
import yt_dlp

def fetch_subtitles(url):
    """Fetch subtitles from a YouTube video."""
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        # Find English subtitles URL
        subtitles = info.get('requested_subtitles', {})
        if not subtitles or 'en' not in subtitles:
            print("No English subtitles found.")
            return None

        subtitle_url = subtitles['en']['url']

        # Fetch subtitle content
        try:
            response = requests.get(subtitle_url)
            content = response.text

            # Clean up subtitle text
            content = re.sub(r'^\s*$', '', content, flags=re.MULTILINE)
            content = re.sub(r'^\d.*$', '', content, flags=re.MULTILINE) # remove lines which start with a number
            content = re.sub(r'^.*<[^>]+>.*$', '', content, flags=re.MULTILINE) # remove lines which contain HTML tags
            content = re.sub(r'\n\n+', '\n', content) # remove empty lines
            lines = content.split('\n')
            seen = set()
            unique_lines = [line for line in lines if not (line in seen or seen.add(line))]
            cleaned_content = ' '.join(unique_lines)

            return cleaned_content
        except Exception as e:
            print(f"Error fetching subtitles: {e}")
            return None

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run fetch_subs.py <youtube_url> <question>")
        sys.exit(1)

    url = sys.argv[1]

    print(fetch_subtitles(url))

if __name__ == "__main__":
    main()