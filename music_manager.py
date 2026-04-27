import random

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

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

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
        if self.head.song.songId == songId:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.song.songId == songId:
                curr.next = curr.next.next
                return
            curr = curr.next

class Song:
    def __init__(self, songId, title, artist, genre):
        self.songId = songId
        self.title = title
        self.artist = artist
        self.genre = genre
        self.playCount = 0

class MusicManager:
    def __init__(self):
        self.queue = []
        self.playlists = {}
        self.allSongs = []

    def shufflePlay(self):
        n = len(self.queue)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def getTrendingSong(self):
        pq = PriorityQueue()
        for s in self.allSongs: pq.enqueue(s)
        return pq.dequeue()

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
                self.queue.append(curr.song)
                curr = curr.next

    def searchSongs(self, q, field="title"):
        q = q.lower()
        return [s for s in self.allSongs if q in getattr(s, field, "").lower()]
