# NOTIBIT: Bitmain Website Notification

## Overview

This application will check the Bitmain website for availability to purchase
Antminer miners, and then notify SMS subscribers and post on
the twitter account when the miner is available. It is convoluted and doesn't
serve much of a purpose. It has only been tested with Python 3.6 on Ubuntu 17.10
with an Android phone.

## Installation

Visit https://bitmain.com and decide which product you would like to monitor.
Once you have found a product, grab the URL and TINYURL it.

### Twitter Setup

The first step is to create a Twitter App at https://apps.twitter.com/
Click the “Create New App” button and fill out the fields on the next page.
You will need to save all of the keys that it gives you.

### IFTTT Setup

Create an IFTTT account at https://ifttt.com/
Download the Android app, install and sign in.
Navigate to "My Applets" and click "New Applet".
Click on "+THIS" and choose "Webhooks".
Now click "Receive a web request".
In the "Event Name" field, type:
'''
notify
'''
Click "Create Trigger".
Click on "+THAT" and choose "Android SMS".
Now click "Send an SMS.
In the "Phone number" field, enter number you want to receive SMS messages.
In the "Message" field, type:
'''
Antminer for sale at [your_tinyURL]
'''
Click "Create Action"
Click "Finish"
In the top left, click "webhooks".
In the top right, click "Documentation"
Now copy your key and you are done.

### Clone this repository and navigate to it's directory

### Install required libraries
'''
pip install --upgrade pip
pip install -r requirements.txt
'''

### Configure

Open config.py and enter in all of your keys.
For product, enter the full BItmain product URL.
For message, enter the message you used for IFTTT

## Usage

## To run program type:
'''
python notibit.py
'''

## To run program in the background, type:
'''
nohup notibit &
'''




