---
title: "Upload my guitar repo"
date: 2021-07-02T23:49:33-04:00
draft: false

tags: [tabs]
categories: [Programming, Guitar]
---


I uploaded my entire guitar folders up to this point. About ~700 ish tabs, mostly/all fingerstyles (no chords btw). Note that they're mostly anime
 (though, imo, all of the songs in there are very good OP/ED. At least the one you can play on guitar anyway). 
They're mostly public, although quite hard to find (some sites I used is gametabs.net and online Youtubers).

Access it at http://triet-guitar.s3-website-us-east-1.amazonaws.com

Please don't flood it with download request. As in don't intentionally DDOS it. Your normal download's gonna be fine. AWS charges me half a cent
for 1000 requests. I also have 20k free s3 requests each month, and this site uses around 25% of it.

Also, there's no logging, as in I won't be tracking your IP. This isn't a honeypot. Just go around and see which tab you'd like, and download it.

If you have additional ~~anime~~ tabs that you would like to contribute, please feel free to send it. I think I'm missing a lot from Bunny Girl Senpai
and Sakurasou (especially Prime Numbers - Sakurasou ED 2, I digged the whole Internet and found nothing). I have a couple MIDI and sheet music in there,
but I forgot how to read sheet music so...

You might have noted that it's not my website, and you'd be correct. This website fetchs stuff from an S3 bucket through
API Gateway, even though I have no intention (or idea) of running any Lambda stuff yet. This isn't really a static website; I can
setup a login mechanism, although I'm probably too dumb, poor and lazy to do that.

Also, there's a whole file directory setup. That's not your browser; that's my index.html and some scripts I ~~stole~~ copied off Github.
Script at: https://gist.github.com/glowinthedark/625eb4caeca12c5aa52778a3b4b0adb4#file-generate_directory_index_caddystyle-py

Also, I learned how painful it is to directorify (or whatever) a folder. Apparently Python doesn't like Unicode or weird characters,
so I have to sanitize all folder's name before even trying anything. Also for API Gateway's purpose, all directory needs to be without whitespace or weird character.
I wrote a small script to recursively sanitize all directory's name, if anyone's interested. It's in the root directory.

Last note: ~~You can actually access the same thing on my website at https://trietmvo.com/guitar. It's kinda the same thing, but because
I cannot set up API Gateway to save my life, everything in there is almost nearly broken and very annoying to use.
If you don't happen to be on the FBI watchlist and need HTTPS, the S3 link should do just fine.~~

No longer relevant. I decided that it's too much of a pain since deploy took more than 5 seconds (that's 5 seconds less of my lifespan) so I moved it to another S3 bucket
and deleted the /guitar directory from my website.

Setting up API Gateway is a pain. If anyone know how to set this stuff up and how to tell API Gateway to just copy whatever S3 bucket endpoint is doing,
please teach me. I'm tired, haven't finished Duolingo (pretty sure that bird knocked last night at 3 AM), and still need to prepare to teach Algebra tomorrow.
This is actual pain.