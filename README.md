# BOTW to mp3
This is a simple python script that extracts the music/sound files from Nintendo games (WiiU and Switch .BFSTM, .BARS, ... files) and converts them into a playable format (mp3) while keeping the tree structure of the original files.

***Note :** This script was made for personal use, with The Legend of Zelda : Breath of the Wild for WiiU in mind. It may not work with other games.*

## Disclaimer
It is expected that you have legally dumped the game files of your purchased copy of the game you want to extract the music from. *(See [ZeldaMods Wiki - Help:Dumping_games](https://zeldamods.org/wiki/Help:Dumping_games) for help)*

## Installation
1. Install from the [releases](https://github.com/AlexZeGamer/botw-to-mp3/releases/) or clone the repository.
2. If you cloned the repository, install [vgmstream](https://vgmstream.org) and write the location of the executable in the `VGMSTREAM_PATH` variable in `convert.py`. (It is already included if you downloaded from the [releases](https://github.com/AlexZeGamer/botw-to-mp3/releases/))
1. Install Python3 and the required libraries (see [Dependencies](#dependencies)).

*Not tested on other platforms than Windows 11.*

## Dependencies
- [Python 3](https://www.python.org/downloads/)
- Python libraries *(see `requirements.txt`, run `pip install -r requirements.txt` to install)*
- [`vgmstream`](https://vgmstream.org) *(see [Installation](#installation))* - Used to convert the `.bfstm`, `.bfstp` and `.bfwav` music files into `.mp3` files.

## Credits
- I used [SamusAranX](https://github.com/SamusAranX)'s ["BARS format (to the best of my knowledge)" (GihHub Gist)](https://gist.github.com/SamusAranX/6eb8b6fd1777b17afc3107a979c2409a) as a base for the `bars_extractor.py` file, used to extract the music from the `.bars` files into `.bfstm` files.
- [ZeldaMods Wiki - Help:Sound_modding](https://zeldamods.org/wiki/Help:Sound_modding) - Helped me understand the structure of the music files.

## Usage
Run `main.py` and select the folder containing the music files you want to extract (likely the game directory) and the folder where you want to extract them to.

## TODO :
- [ ] Refactor `bars_extractor.py` into functions
- [ ] Implement `bars_extractor.py` into `main.py`
- [ ] Make tkinter optional
- [x] Find a name for the repo
  - Nintendo to mp3
  - BOTW to mp3