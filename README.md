# [SpotifyAdSkipperGithub](https://github.com/nikhi1g/SpotifyAdSkipper)
Skips Spotify Advertisements, works so far with Mac.

This project was created over Thankgiving 2021 as a means to get rid of Spotify Advertisements. It works by adding song names (along with other items) to a dictionary, pretty printing that dictionary, and then updating the output if the old output does not match the new getted output. Funny thing is, an advertisement cannot be added to this dictionary, and I get errors. I catch these Errors as e (thanks StackExchange!) and then print them out to the console. I use the [os library](https://docs.python.org/3/library/os.html) to quit, open, [play](https://pypi.org/project/osascript/), and minimize Spotify in less than a second. The result: Ad Skipping! 
