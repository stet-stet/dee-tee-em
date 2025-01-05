# The problem with using Kontakt Drums on a basic Keyboard + Mouse environment

In the default configuration of Abbey Road Modern Drummer, different articulations of a snare is distributed with no apparent pattern whatsoever.

I dunno if this is more convenient for people on other types of controllers, but for me, who does everything on a mouse, 
I feel like my creativity is dying when I drag notes up and down up and down up and down for the gazillionth time to check what note is what articulation. More so if I only need the snares.

## Solution

Fortunately, the drum libraries support user-made MIDI mapping. I wrote a python script to (partly) congregate the articulations of each instrument into one cluster. Process goes as follows.

1. Go to "midi mapping" section of your drum instrument, and click on the floppy disk icon so that the plugin saves a new mapping in the "user area".
2. Identify where the newly made custom presets are. In my case this is `Users\(username)\AppData\Local\(Instrument name)\Data`. There are three `.nka` files, each ending in `_presets.nka`, `_data.nka`, and `_names.nka`.
3. come back to this folder and then `python "(the name of folder)"`.
4. Open your drum instrument, and then switch to the custom mapping. Enjoy!