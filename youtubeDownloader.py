#!/usr/bin/python

from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

#Title of video
Title = yt.title
print("Title: ",yt.title)

#Number of views of video
#print("Number of views: ",yt.views)

#Length of the video
#print("Length of video: ",yt.length,"seconds")

#Description of video
#print("Description: ",yt.description)

#Rating
print("Ratings: ",yt.rating)


#these print to a file to remember

f = open("/home/noah/Videos/YTvids/" + Title + ".txt", "a")

print("Title: ",yt.title, file=f)

#Number of views of video
print("Number of views: ",yt.views, file=f)

#Length of the video
print("Length of video: ",yt.length,"seconds", file=f)

#Description of video
print("Description: ",yt.description, file=f)

#Rating
print("Ratings: ",yt.rating, file=f)

f.close()


#not probably necacery for streams

#printing all the available streams
#print(yt.streams)

print("\nthese are the audio only:\n")
print(yt.streams.filter(only_audio=True))
print(\
        )

print("these are the video only:\n")
print(yt.streams.filter(only_video=True))
print(\
        )

print("these are the audio and video ones:\n")
print(yt.streams.filter(progressive=True))

##################################################


#ys = yt.streams.get_highest_resolution()

ys = yt.streams.get_by_itag(input("\n choose your tag for file: "))

ys.download("/home/noah/Videos/YTvids/")
