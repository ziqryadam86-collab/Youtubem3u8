import yt_dlp
import os

def get_m3u8_url(url):
    ydl_opts = {'format': 'hls', 'quiet': True}
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
    # Ganti dengan link anda
    url = "https://m.youtube.com/@alanbecker/live" 
    m3u8_url = get_m3u8_url(url)
    
    if m3u8_url:
        update_index(m3u8_url)
        print("index.m3u8 berjaya dikemaskini!")
    else:
        print("Gagal mendapatkan pautan m3u8.")
        exit(1) # Keluar dengan error jika gagal
  
