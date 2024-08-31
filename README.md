# Generate JMusicBot Playlist Plugin

Automatically generate playlists for JMusicBot when saving an album in MusicBrainz Picard. This plugin is designed to create `.txt` playlist files with Docker-friendly paths, ideal for use with JMusicBot, a popular Discord music bot that supports playlist files.

## Features

- Automatically generates a `.txt` playlist file when you save an album in Picard.
- Converts Windows file paths to Docker-friendly paths, making it easy to use your music with JMusicBot running in a Docker container.
- Playlist filenames use "slugged" versions of the artist and album names, making them URL-friendly and easy to manage.
- Configurable paths and playlist directory to suit different setups.

## Installation

1. Download or clone this repository.
2. Copy the `generate_jmusicbot_playlist` directory to the MusicBrainz Picard plugin directory:
   - **Windows**: `C:\Users\YourUsername\AppData\Roaming\MusicBrainz\Picard\plugins\`
   - **Mac**: `~/Library/Preferences/MusicBrainz/Picard/plugins/`
   - **Linux**: `~/.config/MusicBrainz/Picard/plugins/`
3. Open MusicBrainz Picard.
4. Go to `Options` -> `Plugins`.
5. Enable the `Generate JMusicBot Playlist` plugin.

## Configuration

Before using the plugin, you need to configure the paths according to your environment:

1. Open MusicBrainz Picard.
2. Go to `Options` -> `Plugins`.
3. Select `Generate JMusicBot Playlist` and click on `Options...` or `Settings...`.
4. Configure the following paths:

   - **Windows Path 1**: The first base path on your system (e.g., `E:\Backups\Music`).
   - **Docker Path 1**: The corresponding Docker-friendly path (e.g., `/data/music`).
   - **Windows Path 2**: The second base path on your system (e.g., `E:\Music`).
   - **Docker Path 2**: The corresponding Docker-friendly path (e.g., `/data/cleaned/music`).
   - **Playlist Directory**: The directory where the playlists will be saved (e.g., `C:\Users\YourUsername\Documents\docker\jmusicbot\Playlists\`).

## Usage

1. Load an album in MusicBrainz Picard.
2. Save the album.
3. The plugin will automatically generate a playlist file in the configured directory.
4. The playlist file will be named using slugged versions of the artist and album names (e.g., `artistname-albumname.txt`) and will contain the paths to the saved tracks, converted to Docker-friendly paths.

## Example

Suppose you have an album by "Richard Cheese" titled "Blue No Matter Who" saved in `E:\Backups\Music\AlbumName`. The plugin will create a playlist file named `richardcheese-bluenomatterwho.txt` in the configured playlist directory, with each track listed as `/data/music/AlbumName/TrackName.mp3`.

## About JMusicBot

[JMusicBot](https://github.com/jagrosh/MusicBot) is a popular music bot for Discord that supports playing music from local files, streams, and playlists. This plugin makes it easy to generate playlists that are compatible with JMusicBot running inside Docker.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
