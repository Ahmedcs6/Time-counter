from pytube import YouTube, Playlist
import math

def get_duration(URL):
    try:
        ln = YouTube(URL)
        duration = ln.length
        if duration is None:
            return 0 
        return duration
    except Exception as e:
        print(f"Error fetching duration for {URL}: {e}")
        return 0 

def get_progress(count, length):
    pro = math.floor((count / length) * 58)
    return pro

def transformer(s):
    hours = s // 3600
    minutes = (s % 3600) // 60
    seconds = s % 60
    return hours, minutes, seconds

def main():
    print("=" * 60)
    print("=" * 12 + "YouTube Playlist Duration Calculator" + "=" * 12)
    print("=" * 60)
    
    url = input("Enter playlist URL: ")
    yt = Playlist(url)
    total_time = 0
    lens = len(yt)
    counter = 0
    
    for i in yt.video_urls:
        d = get_duration(i)
        counter += 1
        total_time += d
        h, m, se = transformer(d)
        pro = get_progress(counter, lens)
        pas = 58 - pro
        print(f"{m}:{se}")
        print(i)
        print("%"+str((counter/lens)*100))
        print("[" +"=" * pro +" " * pas+"]")
    
    th, tm, tse = transformer(total_time)
    print(f"Total Playlist Duration: {th}:{tm}:{tse}")

main()