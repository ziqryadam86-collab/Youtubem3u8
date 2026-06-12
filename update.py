import yt_dlp
import os

def get_m3u8_url(url):
    # Kita guna user_agent pelayar telefon supaya YouTube tak block
    ydl_opts = {
        'format': 'hls',
        'quiet': True,
        'user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info.get('url')
        except Exception as e:
            print(f"Error: {e}")
            return None

def update_index(m3u8_url):
    content = f"""#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=390000,CODECS="avc1.4d0015,mp4a.40.2",RESOLUTION=426x240
{m3u8_url}
"""
    with open("index.m3u8", "w") as f:
        f.write(content)

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=HgWz05AsLxw" 
    m3u8_url = get_m3u8_url(url)
    
    if m3u8_url:
        update_index(m3u8_url)
        print("Berjaya!")
    else:
        print("Gagal.")
        exit(1)
        
