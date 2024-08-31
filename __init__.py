from picard import log
from picard.metadata import register_album_post_save_processor
import os

PLUGIN_NAME = "Generate JMusicBot Playlist"
PLUGIN_AUTHOR = "HeavyGee"
PLUGIN_DESCRIPTION = "Automatically generate a playlist for JMusicBot when saving an album with Docker-friendly paths."
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["2.0"]

def generate_playlist(album):
    # Define your base paths
    windows_path_1 = "E:\\Backups\\Music"
    docker_path_1 = "/data/music"
    
    windows_path_2 = "E:\\Music"
    docker_path_2 = "/data/cleaned/music"

    # Create the playlist file path
    playlist_dir = os.path.expanduser("~\\Documents\\docker\\jmusicbot\\Playlists\\")
    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)
    
    playlist_name = f"{album.metadata['albumartist']}-{album.metadata['album']}.txt".replace(' ', '').lower()
    playlist_path = os.path.join(playlist_dir, playlist_name)

    # Open the playlist file for writing
    with open(playlist_path, 'w') as playlist_file:
        for track in album.tracks:
            file_path = track.filename
            # Replace Windows paths with Docker-friendly paths
            if file_path.startswith(windows_path_1):
                docker_friendly_path = file_path.replace(windows_path_1, docker_path_1)
            elif file_path.startswith(windows_path_2):
                docker_friendly_path = file_path.replace(windows_path_2, docker_path_2)
            else:
                docker_friendly_path = file_path  # Unchanged if not matching either path
            # Write to the playlist
            playlist_file.write(f"{docker_friendly_path}\n")
    
    log.info(f"JMusicBot playlist created: {playlist_path}")

# Register the plugin to run after album save
register_album_post_save_processor(generate_playlist)
