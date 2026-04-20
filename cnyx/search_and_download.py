import os
import subprocess

def search_and_download(query: str):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "songs")
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n🔍 Searching and downloading: {query}")
    print(f"📁 Saving to: {output_dir}\n")

    subprocess.run([
        "yt-dlp",
        f"ytsearch1:{query}",        # search YouTube for best match
        "--extract-audio",            # extract audio only
        "--audio-format", "mp3",      # save as mp3
        "--audio-quality", "0",       # best quality
        "--output", f"{output_dir}/%(title)s.%(ext)s",
        "--no-playlist",
    ])

def main():
    query = input("Enter song name (+ artist for best results): ").strip()
    if not query:
        print("No input provided. Exiting.")
        return
    search_and_download(query)

if __name__ == "__main__":
    main()
