from http import client
import requests
import json
import pandas as pd
import time
#import matplotlib.pyplot as plt
import datetime
from meteostat import Point, Daily

from requests_oauthlib import OAuth2Session
from requests_oauthlib import OAuth1Session
import os
import json
from datetime import date
from datetime import timedelta
import tweepy
import schedule
import sys
import os
import config

def klima():

    ####Klimadaten###
    gestern=date.today()-timedelta(days=1)
    monat=gestern.month
    tag=gestern.day


    # Create Point for Vancouver, BC
    berlin = Point(52.4938, 13.4447)


    df=pd.DataFrame()
    x=1900
    for i in range (1,124):
        start = datetime.datetime(x, monat, tag)
        end = datetime.datetime(x, monat, tag)
        x+=1
        data = Daily(berlin, start, end)
        data = data.fetch()
        print(data)

        df=df.append(data.iloc[[0]])

    #calculate average in ten year intervalls

    df2=pd.DataFrame(columns=['Jahrzehnt',"Tagestemperatur"])




    #erstes Jahrzehnt

    x=0
    null=0
    y=1899
    for i in range(0,10):
        y+=1
        
        null=null+df.iloc[x,0]
        x+=1
        if i ==9:
            null=round((null/(i+1)),2)

    df3=pd.DataFrame(columns=['Jahrzehnt',"Tagestemperatur"])
    df3.loc[0, "Jahrzehnt"]="1900-1909"
    df3.loc[0, "Tagestemperatur"]=null


    df2=df2.append(df3)


    x=9
    zehn=0
    for i in range(0,10):
        y+=1
        
        x+=1
        zehn=zehn+df.iloc[x,0]
        if i ==9:
            zehn=round((zehn/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1910-1919"
    df3.loc[0, "Tagestemperatur"]=zehn



    df2=df2.append(df3)




    x=19
    zwanzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        zwanzig=zwanzig+df.iloc[x,0]
        if i ==9:
            zwanzig=round((zwanzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1920-1929"
    df3.loc[0, "Tagestemperatur"]=zwanzig

    df2=df2.append(df3)



    x=29
    dreißig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        dreißig=dreißig+df.iloc[x,0]
        if i ==9:
            dreißig=round((dreißig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1930-1939"
    df3.loc[0, "Tagestemperatur"]=dreißig

    df2=df2.append(df3)



    x=39
    vierzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        vierzig=vierzig+df.iloc[x,0]
        if i ==9:
            vierzig=round((vierzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1940-1949"
    df3.loc[0, "Tagestemperatur"]=vierzig

    df2=df2.append(df3)



    x=49
    fünfzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        fünfzig=fünfzig+df.iloc[x,0]
        if i ==9:
            fünfzig=round((fünfzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1950-59"
    df3.loc[0, "Tagestemperatur"]=fünfzig

    df2=df2.append(df3)



    x=59
    sechzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        sechzig=sechzig+df.iloc[x,0]
        if i ==9:
            sechzig=round((sechzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1960-1969"
    df3.loc[0, "Tagestemperatur"]=sechzig

    df2=df2.append(df3)



    x=69
    siebzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        siebzig=siebzig+df.iloc[x,0]
        if i ==9:
            siebzig=round((siebzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1970-79"
    df3.loc[0, "Tagestemperatur"]=siebzig

    df2=df2.append(df3)



    x=79
    achtzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        achtzig=achtzig+df.iloc[x,0]
        if i ==9:
            achtzig=round((achtzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1980-89"
    df3.loc[0, "Tagestemperatur"]=achtzig

    df2=df2.append(df3)


    x=89
    neunzig=0
    for i in range(0,10):
        y+=1
        
        x+=1
        neunzig=neunzig+df.iloc[x,0]
        if i ==9:
            neunzig=round((neunzig/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="1990-1999"
    df3.loc[0, "Tagestemperatur"]=neunzig

    df2=df2.append(df3)




    x=99
    tausend=0
    for i in range(0,10):
        y+=1
        
        x+=1
        tausend=tausend+df.iloc[x,0]
        if i ==9:
            tausend=round((tausend/(i+1)),2)

    df3.loc[0, "Jahrzehnt"]="2000-2009"
    df3.loc[0, "Tagestemperatur"]=tausend

    df2=df2.append(df3)


    x=109
    zwanzigzehn=0
    for i in range(0,10):
        y+=1
        
        x+=1

        zwanzigzehn=zwanzigzehn+df.iloc[x,0]
        

        if i ==9:
            zwanzigzehn=round((zwanzigzehn/(i+1)),2)
    df3.loc[0, "Jahrzehnt"]="2010-2019"
    df3.loc[0, "Tagestemperatur"]=zwanzigzehn

    df2=df2.append(df3)


    #erstes halbes Jahrhundert
    bismitte1950=round(((df["tavg"].iloc[0:51].sum(axis=0))/51),2)
    df3.loc[0, "Jahrzehnt"]="1900-1950"
    df3.loc[0, "Tagestemperatur"]=bismitte1950
    df2=df2.append(df3)


    #today
    x=-1
    today=df.iloc[x,0]

    heute = datetime.datetime.today()
    yesterday = heute - timedelta(days=1)

    yesterday=yesterday.strftime("%d.%m.%Y")

    df3.loc[0, "Jahrzehnt"]=yesterday
    df3.loc[0, "Tagestemperatur"]=today


    df2=df2.append(df3)
    df2=df2.reset_index(drop=True)
    #print(df2)

    unterschiedingrad=round((df2.at[13,"Tagestemperatur"])-(df2.at[12,"Tagestemperatur"]),2)
    unterschiedinprozent=round(((df2.at[13,"Tagestemperatur"])*100/(df2.at[12,"Tagestemperatur"]))-100)
    #print(unterschiedinprozent)
    if unterschiedinprozent>0:
        unterschiedinprozent="+"+str(unterschiedinprozent)

    text1="Temperatur am """+str(yesterday)+""": """+str(df2.at[13,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n\nVergleich: 1900-1950: """+ str(df2.at[12,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\nUnterschied: """+str(unterschiedingrad)+""" \N{DEGREE SIGN}C / """+str(unterschiedinprozent)+"""% \n\nSource: Meteostat (https://meteostat.net/de/) für Berlin (Deutschland)\n\n#klimawandel #fridaysforfuture #klimakrise #climatejustice #savetheplanet #klimanotstand
    """
    

    text2="""
Historische Mittelwerte:\n
1900-1909: """+ str(df2.at[0,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1910-1919: """+ str(df2.at[1,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1920-1929: """+ str(df2.at[2,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1930-1939: """+ str(df2.at[3,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1940-1949: """+ str(df2.at[4,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1950-1959: """+ str(df2.at[5,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1960-1969: """+ str(df2.at[6,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1970-1979: """+ str(df2.at[7,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1980-1989: """+ str(df2.at[8,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
1990-1999: """+ str(df2.at[9,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
2000-2009: """+ str(df2.at[10,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
2010-2019: """+ str(df2.at[11,"Tagestemperatur"])+""" \N{DEGREE SIGN}C\n
    """
    print(text1)
    print(text2)




    df.to_csv("test.csv")
    liste5=[text1,text2]
    return liste5
def tweet():
    liste6=klima()


    client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
    )

    client.create_tweet(text=liste6[0])
    time.sleep(15)


def retweet():
    liste6=klima()
    auth_token=config.auth_token
    headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer "+auth_token
    }



    url = 'https://api.twitter.com/2/tweets/search/recent?query=from%3Ahistory_climate'




    r = requests.get(url=url,headers=headers)


    json_data = json.loads(r.text)
    print(json_data)
    data=json_data['data']
    x=-1
    liste=[]
    for i in data:
        x=x+1
        id_tweet=data[x].get("id")
        liste.append(id_tweet)

    print(liste)

    client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
    )

    client.create_tweet(text=liste6[1],in_reply_to_tweet_id=liste[0])
    
    
def monitoring():
    url="https://webexapis.com/v1/messages"


    headers={
        "Authorization": f"Bearer {config.webex_api_key}"
    }
    data={
        "toPersonId":config.person_id,
        "markdown":"### Info\n\n"
        "Twitter Boty hat funktioniert"

    }

    r = requests.post(url, data=data,headers=headers)



def ticker():
    """
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("Twitterbot: Warten.")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("Twitterbot: Warten..")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("Twitterbot: Warten...")
    
    for x in range (0,4):
        time.sleep(1)
        print("\r", end="")
        print("Twitterbot: Warten auf 09:00 Uhr"+"."*x, end="")
        if x==3:
            time.sleep(1)
            print("\r", end="")
            print("Twitterbot: Warten auf 09:00 Uhr"+" "*x, end="")
"""

    jetzt=datetime.datetime.now()

    start_time = datetime.time(jetzt.hour,jetzt.minute)
    stop_time = datetime.time(9,0)

    tommorrow=jetzt+datetime.timedelta(days=1)

    date = datetime.date(tommorrow.year, tommorrow.month, tommorrow.day)

    datetime1 = datetime.datetime.combine(jetzt, start_time)
    datetime2 = datetime.datetime.combine(date, stop_time)

    delta=datetime2-datetime1


    date_time = datetime.datetime.strptime(str(delta), "%H:%M:%S")
    a_timedelta = date_time - datetime.datetime(1900, 1, 1)
    seconds = a_timedelta.total_seconds()



    def progression_bar(total_time=seconds):
        num_bar = 100
        sleep_intvl = total_time/num_bar
        print("Nils' Twitterbot - Start des nächsten Durchgangs: ")
        for i in range(1,num_bar):
            print("\r", end="")
            print("{:.1%} ".format(i/num_bar),"-"*i, end="")

            if i >=2:
                time.sleep(sleep_intvl)
    
    progression_bar()


    

def alles():
    tweet()
    retweet()
    monitoring()


print("""
'    _   _ _ _     _   _______       _ _   _            _           _   
'   | \ | (_) |   ( ) |__   __|     (_) | | |          | |         | |  
'   |  \| |_| |___|/     | |_      ___| |_| |_ ___ _ __| |__   ___ | |_ 
'   | . ` | | / __|      | \ \ /\ / / | __| __/ _ \ '__| '_ \ / _ \| __|
'   | |\  | | \__ \      | |\ V  V /| | |_| ||  __/ |  | |_) | (_) | |_ 
'   |_| \_|_|_|___/      |_| \_/\_/ |_|\__|\__\___|_|  |_.__/ \___/ \__|
'                                                                       
'                                                                       
""")

schedule.every().day.at("09:00").do(alles)



while True:

    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

    ticker()
    

    






