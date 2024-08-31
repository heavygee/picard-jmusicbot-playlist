from picard import config, log
from picard.metadata import register_album_post_save_processor
from picard.plugin import PluginPriority
from picard.config import TextOption
import os
import re

PLUGIN_NAME = "Generate JMusicBot Playlist"
PLUGIN_AUTHOR = "HeavyGee"
PLUGIN_DESCRIPTION = "Automatically generate a playlist for JMusicBot when saving an album with Docker-friendly paths."
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]

# Define configuration options
config.setting.add_section("generate_jmusicbot_playlist")
config.setting["generate_jmusicbot_playlist"]["windows_path_1"] = TextOption("generate_jmusicbot_playlist", "windows_path_1", "")
config.setting["generate_jmusicbot_playlist"]["docker_path_1"] = TextOption("generate_jmusicbot_playlist", "docker_path_1", "")
config.setting["generate_jmusicbot_playlist"]["windows_path_2"] = TextOption("generate_jmusicbot_playlist", "windows_path_2", "")
config.setting["generate_jmusicbot_playlist"]["docker_path_2"] = TextOption("generate_jmusicbot_playlist", "docker_path_2", "")
config.setting["generate_jmusicbot_playlist"]["playlist_dir"] = TextOption("generate_jmusicbot_playlist", "playlist_dir", "~\\Documents\\docker\\jmusicbot\\Playlists\\")

def slugify(text):
    # Convert to lowercase
    text = text.lower()
    # Remove any characters that are not alphanumeric, underscores, or hyphens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    return text.strip('-')

def generate_playlist(album):
    # Retrieve user-configured paths
    windows_path_1 = config.setting["generate_jmusicbot_playlist"]["windows_path_1"]
    docker_path_1 = config.setting["generate_jmusicbot_playlist"]["docker_path_1"]
    windows_path_2 = config.setting["generate_jmusicbot_playlist"]["windows_path_2"]
    docker_path_2 = config.setting["generate_jmusicbot_playlist"]["docker_path_2"]
    playlist_dir = os.path.expanduser(config.setting["generate_jmusicbot_playlist"]["playlist_dir"])

    # Create the playlist directory if it doesn't exist
    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)
    
    # Generate slugged versions of artist and album names
    artist_slug = slugify(album.metadata['albumartist'])
    album_slug = slugify(album.metadata['album'])
    
    playlist_name = f"{artist_slug}-{album_slug}.txt"
    playlist_path = os.path.join(playlist_dir, playlist_name)

    # Open the playlist file for writing
    with open(playlist_path, 'w') as playlist_file:
        for track in album.tracks:
            file_path = track.filename
            # Replace Windows paths with Docker-friendly paths
            if windows_path_1 and file_path.startswith(windows_path_1):
                docker_friendly_path = file_path.replace(windows_path_1, docker_path_1)
            elif windows_path_2 and file_path.startswith(windows_path_2):
                docker_friendly_path = file_path.replace(windows_path_2, docker_path_2)
            else:
                docker_friendly_path = file_path  # Unchanged if not matching either path
            # Write to the playlist
            playlist_file.write(f"{docker_friendly_path}\n")
    
    log.info(f"JMusicBot playlist created: {playlist_path}")

# Register the plugin to run after album save
register_album_post_save_processor(generate_playlist, priority=PluginPriority.LOW)
