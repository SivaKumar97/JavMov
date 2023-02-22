from moviepy.editor import VideoFileClip, concatenate_videoclips
import cv2
from time import sleep
import sys
# URLs of the .ts files to download


# Download the .ts files and save them locally
# for i in range(1, 2):
#     link = f'https://delivery212.akamai-cdn-content.com/hls2/01/11420/i7fn8o9yvchd_h/seg-{i}-v1-a1.ts?t=Ld0elPIakm2cQ7WWSiX6v8cyDColNEwTTyX6auVHcGc&s=1677064838&e=10800&f=57110103&srv=sto248&client=202.53.4.17'
#     r = requests.get(link)
#     with open(f"file{i}.ts", "wb") as f:
#         print(f"Download : {i}")
#         f.write(r.content)
def printProgressBar(i,max):
    n_bar =10 #size of progress bar
    j= i/max
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {int(100 * j)}% : {counter}")
    sys.stdout.flush()
# Merge the .ts files into a single video file
video_files = []
for i in range(1, 742):
    video_files.append(f"seg-{i}-v1-a1.ts")

max = len(video_files)

print("Videos Files Length: ",len(video_files))

cap = cv2.VideoCapture(video_files[0])
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.release()
out = cv2.VideoWriter('merged_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
counter = 0
for file in video_files:
    cap = cv2.VideoCapture(file)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    counter = counter + 1
    printProgressBar(counter,max)
    cap.release()

# Release the video writer object
out.release()



# function dwn(count, limit){
#         if(count <limit){
#             setTimeout(()=>{
#                 var link = `https://delivery372.akamai-cdn-content.com/hls2/01/11420/i7fn8o9yvchd_n/seg-${count}-v1-a1.ts?t=cSJYE7WL21uIdfWwsTCMUDW3Qa5HkUPa6CZiJMrr5Ho&s=1677070214&e=10800&f=57104481&srv=sto248&client=202.53.4.17`;
#                 console.log("Count :",count)
#                 window.location.href = link
#                 count = count + 1;
#                 dwn(count,limit)
#                 console.log(link)
#             },1000)
#         }
# }
