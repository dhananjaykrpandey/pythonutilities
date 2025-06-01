from mutagen.easyid3 import EasyID3
import mutagen

def update_title(file_path, new_title):
    try:
        audio = EasyID3(file_path)
    except mutagen.id3.ID3NoHeaderError:
        audio = mutagen.File(file_path, easy=True)
        if audio is None:
            raise Exception("Failed to open audio file. Format may not be supported.")
        audio.add_tags()

    audio['Album'] = new_title
    audio.save()
    print(f"Updated title to: {new_title}")

# Example usage
file_path = r'/home/yash/Downloads/Aparajita.mp3'
new_title = '01_Aparajita'
update_title(file_path, new_title)
