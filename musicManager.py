import random

class Song:
    def __init__(self, songId, title, artist, genre):
        self.songId = songId
        self.title = title
        self.artist = artist
        self.genre = genre
        self.playCount = 0

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SongQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addToQueue(self, song):
        newNode = Node(song)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def getNextSong(self):
        if self.isEmpty(): return None
        res = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty(): self.tail = None
        return res

    def clearQueue(self):
        self.head = self.tail = None
        self.size = 0

class HistoryStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addToHistory(self, song):
        newNode = Node(song)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def goBack(self):
        if self.isEmpty(): return None
        res = self.top.data
        self.top = self.top.next
        self.size -= 1
        return res

class BstNode:
    def __init__(self, song):
        self.song = song
        self.left = None
        self.right = None

class TrendingBst:
    def __init__(self):
        self.root = None

    def insert(self, song):
        if not self.root:
            self.root = BstNode(song)
        else:
            self.insertNode(self.root, song)

    def insertNode(self, curr, song):
        if song.playCount < curr.song.playCount:
            if not curr.left: curr.left = BstNode(song)
            else: self.insertNode(curr.left, song)
        else:
            # Songs with same playCount go to the right to keep them together
            if not curr.right: curr.right = BstNode(song)
            else: self.insertNode(curr.right, song)

    def findMax(self):
        if not self.root: return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.song

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, song):
        if not self.head:
            self.head = Node(song)
            return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(song)

    def remove(self, songId):
        if not self.head: return
        if self.head.data.songId == songId:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.data.songId == songId:
                curr.next = curr.next.next
                return
            curr = curr.next

class MusicManager:
    def __init__(self):
        self.upcoming = SongQueue()
        self.history = HistoryStack()
        self.playlists = {}
        self.allSongs = []

    def playNext(self):
        song = self.upcoming.getNextSong()
        if song:
            song.playCount += 1
            self.history.addToHistory(song)
            return song
        return None

    def shufflePlay(self):
        temp = []
        curr = self.upcoming.head
        while curr:
            temp.append(curr.data)
            curr = curr.next
        random.shuffle(temp)
        self.upcoming.clearQueue()
        for s in temp: self.upcoming.addToQueue(s)

    def getTrendingSong(self):
        bst = TrendingBst()
        for s in self.allSongs:
            if s.playCount > 0: bst.insert(s)
        return bst.findMax()

    def createPlaylist(self, name):
        if name not in self.playlists: self.playlists[name] = LinkedList()

    def addSongToPlaylist(self, name, song):
        if name in self.playlists: self.playlists[name].append(song)

    def deleteSongFromPlaylist(self, name, songId):
        if name in self.playlists: self.playlists[name].remove(songId)

    def loadPlaylistToQueue(self, name):
        if name in self.playlists:
            curr = self.playlists[name].head
            while curr:
                self.upcoming.addToQueue(curr.data)
                curr = curr.next

    def searchSongs(self, q, field="title"):
        q = q.lower()
        return [s for s in self.allSongs if q in getattr(s, field, "").lower()]

    def addSongToSystem(self, song):
        self.allSongs.append(song)
