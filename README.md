# Firefox-Media-Center
A webpage that acts as a media center within Firefox

Dependencies:
Well, you should be using:
Firefox
gecko-mediaplayer

Issues:
Video doesn't load if the file size is too large (?) or the bitrate is too high (?)
Whatever the issue is, not everything loads, which is an issue.

Major things todo:
  Make it look nice:
    Get better fonts  
    Get better colors
    Get better design  
  Create a tool for assembling the necessary metadata / make a system that isn't as dependent on the metadata (unlikely w/o AJAX)
  learn how to format these readmes




create.py

scans the file system and creates the appropriate metadata text files, for the names of series, the names of subseries within franchises, and everything's episode lists. will generate everything such that it works with the webpage iff: everything has a cover and a desc.txt, franchise sub-series numbering must have an _ between the entry# and the title. For example, the folder "Franchise: Star Wars"  may contain a bunch of sub-folders named according to the following pattern: "1_The Phantom Menace".

_ is used to indicate that something is a subseries of a franchise. Where the number to the left of it indicates its place in order in the franchise, and the text to the right is the title. 

Franchise.html must be in the 'root' directory of the program- it will be copied into franchises as necessary.
At the moment I believe that all files will open up properly in the player. However, because some test files are seemingly too large or too high bitrate, I can't actually watch. That said, if the runtime of the file displays, that means it has loaded enough so so as to indicate that it can access the file
