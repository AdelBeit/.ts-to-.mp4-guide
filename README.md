# how to grab .ts files from a video stream and convert them into an mp4 file



## 1) Get .ts URL

Head over to your favorite streaming site. Open developer tools in whatever browser you're using. 

Find the link to the .ts file in the network monitor of your developer tools

![devtools](/img/dev-tools.PNG)



## 2) Download all .ts files
Copy the link. Find the segment number in the link.

Open up main.py

Replace the value of the source variable with your own link

Replace the segment number in the url with {0} in the source variable

Run the main.py file (using Terminal or Command prompt), note it's written in Python 2

P.S. use pip to install grequest and request libraries. 



## 3) Combine all .ts files into one

You should have a bunch of .ts file after the python file has finnished downloading.

Navigate to the folder containing all the .ts files

Open the command prompt in the same folder as all of your .ts files and type this command:

  | type *.ts > video.mp4 |

If you have a Mac or Linux use this command:

  | cat *.ts > video.mp4  |
  
  

## 4) Convert the .ts file to an .mp4 file

Install ffmpeg

Open command prompt/terminal in the same folder as the big .ts file and run this command:

  ffmpeg -i video.ts -bsf:a aac_adtstoasc -acodec copy -vcodec copy video.mp4

and you're done!

