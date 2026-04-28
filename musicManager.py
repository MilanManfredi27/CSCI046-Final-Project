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
        if self.isEmpty():
            return None
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty():
            self.tail = None
        return result

    def seeNext(self):
        if self.isEmpty():
            return "No upcoming songs."
        return f"Up next: {self.head.data}"

    def clearQueue(self):
        self.head = None
        self.tail = None
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
        if self.isEmpty():
            return None
        result = self.top.data
        self.top = self.top.next
        self.size -= 1
        return result

    def seeLastPlayed(self):
        if self.isEmpty():
            return "No history."
        return f"Last played: {self.top.data}"

    def clearHistory(self):
        self.top = None
        self.size = 0

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, song):
        self.heap.append(song)
        self.siftUp(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0)
        return res

    def siftUp(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i].playCount > self.heap[p].playCount:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else: break

    def siftDown(self, i):
        while True:
            l, r, m = 2*i + 1, 2*i + 2, i
            if l < len(self.heap) and self.heap[l].playCount > self.heap[m].playCount: m = l
            if r < len(self.heap) and self.heap[r].playCount > self.heap[m].playCount: m = r
            if m != i:
                self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
                i = m
            else: break

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
        tempList = []
        curr = self.upcoming.head
        while curr:
            tempList.append(curr.data)
            curr = curr.next
        
        n = len(tempList)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            tempList[i], tempList[j] = tempList[j], tempList[i]
        
        self.upcoming.clearQueue()
        for s in tempList:
            self.upcoming.addToQueue(s)

    def getTrendingSong(self):
        pq = PriorityQueue()
        for s in self.allSongs:
            if s.playCount > 0:
                pq.enqueue(s)
        return pq.dequeue()

    def createPlaylist(self, name):
        if name not in self.playlists:
            self.playlists[name] = LinkedList()

    def addSongToPlaylist(self, name, song):
        if name in self.playlists:
            self.playlists[name].append(song)

    def deleteSongFromPlaylist(self, name, songId):
        if name in self.playlists:
            self.playlists[name].remove(songId)

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
