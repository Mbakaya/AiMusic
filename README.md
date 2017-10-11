# AiMusic
Training machine to make some music for us
Machine Learning allows us to make Ai generated music by training the machine to over a dataset then have it generate its own music.
This is possible by learning the MELODY & HARMONY  of the of the music notes
This is because of Recurrent Neural Network(RNN) which are neural network  with loops in them, allowing information to persist.
We use RNN in this case because the melodies and harmony are constantly looping to give us the music.

We also implement a special RNN  -Long short term memory(LSTM) which makes the machine remember not only the music we trained it on 
but also spot similar melodies & harmonies in different music than the trained one to finally generate its own music!!


The MELODY is Menophonic :-Only one note is played at each step of the note.

MELODY+HARMONY = RNN

We put Melody & Harmony in each vector respectively and combine the two vectors to make one vector.

Call the train method & make the machine learn to make its own music.

Dependencies
Urlib - python packages to handle urls
Zipfile - python package to handled ziped files 
Our dataset
 rnn -importing the Recurrent neural network in our file

