from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, APIC
import sys
import os

def get_song_info(mp3_path: str):
    mp3_path = os.path.expanduser(mp3_path)

    if not os.path.exists(mp3_path):
        print(f"[ERROR] File not found: {mp3_path}")
        sys.exit(1)

    audio = MP3(mp3_path, ID3=ID3)
    tags = audio.tags

    title = tags.get("TIT2")
    artist = tags.get("TPE1")
    cover = tags.get("APIC:")

    print(f"🎵 Title:  {title.text[0] if title else 'Unknown'}")
    print(f"🎤 Artist: {artist.text[0] if artist else 'Unknown'}")

    if cover:
        cover_path = os.path.splitext(mp3_path)[0] + ".jpg"
        with open(cover_path, "wb") as f:
            f.write(cover.data)
        print(f"🖼️  Cover saved as: {cover_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_song_info.py <path-to-mp3>")
        sys.exit(1)

    get_song_info(sys.argv[1])
