'''The "Upcoming" Queue (FIFO)
This manages the songs waiting to be played in the order they were added.
- add_to_queue(song): (Enqueue) Adds a new song to the very end of the list.
- get_next_song(): (Dequeue) Removes and returns the song at the front of the queue to start playing it.
- see_next(): (Peek) Shows the user which song is at the front of the queue without playing it yet.
- clear_queue(): Removes all songs from the upcoming list if the user wants to start fresh.'''

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class SongQueue:
    """
    Upcoming Queue (FIFO)
    Manages songs waiting to be played in the order they were added.
    New songs join at the back; the next song to play is always at the front.
    """
    def __init__(self):
        self.head = None   # front of queue — next song to play
        self.tail = None   # back of queue — last song added
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_to_queue(self, song):
        """Enqueue: Adds a new song to the very end of the upcoming list."""
        new_node = Node(song)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        print(f"'{song}' added to the upcoming queue.")

    def get_next_song(self):
        """Dequeue: Removes and returns the song at the front of the queue to start playing it."""
        if self.is_empty():
            raise Exception("The upcoming queue is empty — no songs left to play.")
        result = self.head.song
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        print(f"Now playing: '{result}'")
        return result

    def see_next(self):
        """Peek: Shows which song is at the front of the queue without playing it yet."""
        if self.is_empty():
            return "No upcoming songs in the queue."
        return f"Up next: '{self.head.song}'"

    def clear_queue(self):
        """Removes all songs from the upcoming list so the user can start fresh."""
        self.head = None
        self.tail = None
        self.size = 0
        print("Upcoming queue cleared.")

    def display(self):
        """Displays all songs currently waiting in the upcoming queue, front to back."""
        if self.is_empty():
            print("Upcoming queue is empty.")
            return
        current = self.head
        print("Upcoming Queue:", end=" ")
        while current:
            print(current.song, end=" -> " if current.next else "\n")
            current = current.next
