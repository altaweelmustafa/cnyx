import os
import subprocess
import sys

def search_and_download(query: str):
    output_dir = os.path.expanduser("~/nyx/songs")
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n[SEARCH] Searching and downloading: {query}")
    print(f"[SAVE] Saving to: {output_dir}\n")

    subprocess.run([
        "yt-dlp",
        f"ytsearch1:{query}",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--output", f"{output_dir}/%(title)s.%(ext)s",
        "--no-playlist",
        "--embed-thumbnail",        
        "--embed-metadata",        
        "--parse-metadata", "%(title)s:%(meta_title)s",  
        "--add-metadata",
    ])

def main():
    if len(sys.argv) < 2:
        print("Usage: cnyx <song-name> <author-name>")
        print("Example: cnyx Genesis Grimes")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    search_and_download(query)

if __name__ == "__main__":
    main()
