class Song:
  def __init__(self,title,artist,duration,genre):
    self.title = title
    self.artist = artist
    self.duration = duration
    self.genre = genre

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
    
class PlaylistManager:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def insertion(self,title,artist,duration,genre):
    new_song = Song(title,artist,duration,genre)
    new_node = Node(new_song)
  
  
  def deletion(self,title):
    pass
  
  def traversal(self):
    pass