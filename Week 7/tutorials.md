
# Tutorials To follow


## Email Sending

First I recommend making an account with gmail. If you do already have an email account, please do make a separate email account, as you may get blocked/banned if you make mistakes (such as sending far too many emails): https://accounts.google.com/SignUp?hl=en

Once you have made the gmail account, you need to allow less secure apps (i.e., a Python program) to access your gmail account. You can do so right here, in just 1 click: https://myaccount.google.com/lesssecureapps

Now you are ready to automate email sending below:
https://automatetheboringstuff.com/chapter16/

If you get stuck, I have an example program for automating email sending in the file "emailSender.py" in this file. It's not the cleanest program, but it works.


## Playing online games 

Start with learning how to use pyautogui, a python library that allows you to control the keyboard and mouse: https://automatetheboringstuff.com/chapter18/
(You'll need to install pyautogui with pip)

If you feel comfortable with the commands provided, you can jump straight to applying pyautogui to play your favorite game (online or offline)

If you would like some practice building a bot to play a game, then you can try following this tutorial on how to play sushi-go-round! https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117

From there I recommend building bots to play Facebook/Messenger games.

## Generating Trump Speeches with Markov Chains and LSTMs (Quite open-ended)

Download the respository at: https://github.com/ryanmcdermott/trump-speeches

You'll particularly need the file "speeches.txt" to be in the same folder as the python script you make in the following tutorial!

Follow this tutorial: https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6

When you're done, try applying it to other kinds of data. Will more data make the sentences more coherent?

You can:

- Try your favorite author at: https://www.gutenberg.org/
- Use Trump Tweets: http://www.trumptwitterarchive.com/
- Maybe even concatenate you own essays into a single file and model your own 

Notice that each word in the generated sequence is only directly dependent on the word before it. Can you try to use the last 2 or 3 words? If you're stuck, I have an implementation of using the last "n" words in "last_n_words.py".

Try playing with the parameter "n" to see what makes a good model. Can you balance between the model memorizing/plagarizing and trying to say new things?

The models previously provided are far from state of the art. The best predictive text these days use LSTM models, and if you want to understand how they work conceputally, follow this tutorial by Andrey Karpathy here: http://karpathy.github.io/2015/05/21/rnn-effectiveness/

He provides a link to example code that requires python2. If you need help using python2, feel free to ask.

## Scheduling Your programs (MacOS)

Unfortunately the method for doing this that was initially planned is now no longer in use. I couldn't locate a better tutorial for doing this, although it likely exists.

## Scheduling Your programs (Windows)

This brief tutorial will merely show you how to schedule your programs: http://desktop.arcgis.com/en/arcmap/10.3/analyze/executing-tools/scheduling-a-python-script-to-run-at-prescribed-times.htm

## Making a Tweetbot

Unfortunately, the as of June this year, building a Twitter app requires applying for a Twitter Developer Account. Your account application will probably not be approved soon enough to build a tweetbot today.

Once your application is approved, you should be able to follow this tutorial: https://scotch.io/tutorials/build-a-tweet-bot-with-python

##  
