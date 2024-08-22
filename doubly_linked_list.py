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
    self.prev = None
      
class PlaylistManager:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add_song(self,title,artist,duration,genre):
    new_song = Song(title,artist,duration,genre)
    new_node = Node(new_song)
    
    if not self.head:
      self.head = new_node
      self.tail = new_node
      
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
  
  def insertion(self,position,title,artist,duration,genre):
    new_song = Song(title,artist,duration,genre)
    new_node = Node(new_song)
    if not self.head:
      self.head = new_node
      self.tail = new_node
      return 
    if position == 0:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    else:
      current = self.head
      current_position = 0
      while current != None and current_position < position:
        current = current.next
        current_position +=1
      
      if current is None:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
      else:
        current.prev.next = new_node
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
    
  def deletion(self,title):
    current = self.head
    while current:
      if current.song.title == title:
        if current == self.head:
          self.head = current.next
        if current == self.tail:
          self.tail = current.prev
        if current.prev:
          current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        return True
      current = current.next
    return False
    
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