class Song:
  def __init__(self,title,artist,duration,genre):
    self.title = title
    self.artist = artist
    self.duration = duration
    self.genre = genre

class Node:
  def __init__(self,song):
    self.song = song
    self.next = None
      
class PlaylistManager:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add_song(self,title,artist,duration,genre):
    new_song = Song(title,artist,duration,genre)
    new_node = Node(new_song)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    
  def insertion(self,position,title,artist,duration,genre):
    new_song = Song(title,artist,duration,genre)
    new_node = Node(new_song)
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      if not self.tail:
        self.tail = new_node
    else:
      current = self.head
      previous = None
      current_position = 0
      while current != None and current_position < position:
        previous = current
        current = current.next
        current_position += 1
      previous.next = new_node
      new_node.next = current
      if current is None:
        self.tails = new_node
      
  def deletion(self,title):
    if not self.head:
      print("Not Songs in Playlist")
      return 
    
    if self.head.song.title == title:
      self.head = self.head.next
      return
    prev = None
    current = self.head
    while current:
      if current.song.title == title:
        prev.next = current.next
        return
      prev = current
      current = current.next
    print("{} was not found in playlist.".format(title))
  
  def traversal(self):
    if not self.head:
      print("No Songs in Playlist")
      return 
    current = self.head
    print("playlist:")
    while current:
      song = current.song
      print("Title: {}, Artist: {}, Duration: {} seconds, Genre: {}".format(song.title,song.artist,song.duration,song.genre))
      print("<---------------------------->")
      current = current.next
playlist_manager = PlaylistManager()
     
def adding_song():
  while True:
    adding_song_input_choice = input("Please Choose a menu option: [A]dd to end [C]hoose Position, [E]xit\n").upper()
    if adding_song_input_choice == "A":
      title = input("Title of Song: ")
      artist =input("Artist of Song: ")
      duration = input("Duration Seconds: ")
      genre = input("Genre of song: ")
      playlist_manager.add_song(title,artist,duration,genre)
      
    elif adding_song_input_choice =="C":
      title = input("Title of Song: ")
      artist =input("Artist of Song: ")
      duration = input("Duration Seconds: ")
      genre = input("Genre of song: ")
      position = int(input("Enter Position to be added"))
      playlist_manager.insertion(position,title,artist,duration,genre)
      
    elif adding_song_input_choice == "E":
      print("Returning to Main Menu...")
      break
    
    else:
      print("Invalid Input")
    
def app():
  while True:
    print("Welcome to Playlist Manager:")
    user_choice = input("Please Choose a menu option: [A]dd Song [V]iew Playlist [D]elete Song [E]nd\n").upper()
    if user_choice == "A":
      adding_song()
    elif user_choice == "V":
      playlist_manager.traversal()
    elif user_choice == "D":
      title = input("Enter Title to Delete: ")
      playlist_manager.deletion(title)
    elif user_choice =="E":
      print("Thank you for using Playlist Manager")
      break
    else:
      print("Invalid Input")
      
      
app()