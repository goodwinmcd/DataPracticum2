This project was for a data practicum course. The goal of it was to generate
lyrics based on a give data set of lyrics. I orginally wrote 500_top_albums.py
to collect the lyrical data from a top albums of all time dataset. Instead of
reinvinting the wheel, I started looking for already existing datasets of lyrcs.
I found the archive.zip file containing ~50 artist and all the lyrics for that
artist.

Ultimately I used GPT-2 to generate the lyrics. You fine tune the model with
custom input text files and it goes on to generate text heavily biased towards
the last bit of data used to train it. I included the Google collab notebook
that I followed to achieve this. I also included the *results.txt files as sample
output.