'''The "History" Stack (LIFO)
This manages the songs that have already been played, most recent on top.
- add_to_history(song): (Push) Adds a song that just finished playing to the top of the history.
- go_back(): (Pop) Removes and returns the most recently played song so it can be replayed.
- see_last_played(): (Peek) Shows the user which song was most recently played without removing it.
- clear_history(): Removes all songs from the history if the user wants to start fresh.'''

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class HistoryStack:
    """
    History Stack (LIFO)
    Manages songs that have already been played, most recent on top.
    Songs get pushed when they finish playing; popped when the user goes back.
    """
    def __init__(self):
        self.top = None    # most recently played song
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_to_history(self, song):
        """Push: Adds a song that just finished playing to the top of the history."""
        new_node = Node(song)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"'{song}' added to history.")

    def go_back(self):
        """Pop: Removes and returns the most recently played song so it can be replayed."""
        if self.is_empty():
            raise Exception("No history yet — no songs have been played.")
        result = self.top.song
        self.top = self.top.next
        self.size -= 1
        print(f"Going back to: '{result}'")
        return result

    def see_last_played(self):
        """Peek: Shows which song was most recently played without removing it."""
        if self.is_empty():
            return "No songs in history yet."
        return f"Last played: '{self.top.song}'"

    def clear_history(self):
        """Removes all songs from the history so the user can start fresh."""
        self.top = None
        self.size = 0
        print("History cleared.")

    def display(self):
        """Displays all songs in history, most recent first."""
        if self.is_empty():
            print("History is empty.")
            return
        current = self.top
        print("History (most recent first):", end=" ")
        while current:
            print(current.song, end=" -> " if current.next else "\n")
            current = current.next
