import os
from musicManager import MusicManager, Song

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. INITIALIZATION
mm = MusicManager()
songs_data = [
    Song(1, "One Dance", "Drake", "Rap"),
    Song(2, "Sorry", "Justin Beiber", "Pop"),
    Song(3, "Passionfruit", "Drake", "Rap"),
    Song(4, "Nokia", "Drake", "Rap"),
    Song(5, "Favorite Girl", "Justin Beiber", "Pop")
]
for s in songs_data:
    mm.addSongToSystem(s)

def run_demo():
    print("===CSCI046 FINAL PROJECT: UNIFIED MUSIC MANAGER===")
    print("Strategy: Demonstrating 4 custom data structures (Queue, Stack, BST, Linked List)\n")

    # 2. SEARCH SYSTEM
    print("--- STEP 1: Search & Queue ---")
    query = "Drake"
    print(f"Searching for artist: '{query}'...")
    results = mm.searchSongs(query, field="artist")
    
    # 3. QUEUE OPERATIONS
    for s in results:
        mm.upcoming.addToQueue(s)
    
    print(f"Next in queue: {mm.upcoming.seeNext()}")
    mm.upcoming.display()        
    input("\n[Press Enter to Play next song...]")

    # 4. PLAY LOGIC
    clear()
    print("--- STEP 2: Play & History ---")
    played = mm.playNext()
    print(f"▶️ Now Playing: {played}")
    print(f"{played.title} play count is now: {played.playCount}")
    
    # 5. STACK OPERATIONS
    print(mm.history.seeLastPlayed()) 
    mm.history.display()             
    
    input("\n[Press Enter to simulate 'Back' button...]")
    prev = mm.history.goBack()       
    print(f"Back Button Pressed: Returned to '{prev}'")
    input("\n[Press Enter to explore Playlists...]")

    # 6. PLAYLISTS
    clear()
    print("--- STEP 3: Playlist Management (Linked List) ---")
    p_name = "Gym Mix"
    mm.createPlaylist(p_name)
    
    song_to_add1 = songs_data[1]
    song_to_add2 = songs_data[4]
    mm.addSongToPlaylist(p_name, song_to_add1) 
    mm.addSongToPlaylist(p_name, song_to_add2) 
    
    print(f"Created playlist '{p_name}' with 2 songs.")
    
    removed_song = song_to_add1
    mm.deleteSongFromPlaylist(p_name, removed_song.songId) 
    print(f"Removed '{removed_song.title}' (ID: {removed_song.songId}) from '{p_name}' via pointer redirection.")
    
    mm.loadPlaylistToQueue(p_name)
    print(f"Loaded '{p_name}' into the upcoming queue.")
    mm.upcoming.display()
    input("\n[Press Enter to see Trending & Shuffle...]")

    # 7. TRENDING CHART
    clear()
    print("--- STEP 4: Advanced Features (BST & Shuffle) ---")
    for _ in range(10): songs_data[3].playCount += 1
    
    trending = mm.getTrendingSong() 
    print(f"Most Popular Song (Rightmost BST node): {trending}")
    
    # 8. SHUFFLE
    print("\nOriginal Queue:")
    mm.upcoming.display()
    mm.shufflePlay()
    print("Shuffled Queue:")
    mm.upcoming.display()
    input("\n[Press Enter to Clear all data...]")

    # 9. CLEANUP
    clear()
    print("--- STEP 5: Resetting System ---")
    mm.upcoming.clearQueue()
    mm.history.clearHistory()
    mm.upcoming.display()
    mm.history.display()
    print("\nDemo Complete. All methods verified.")

if __name__ == "__main__":
    run_demo()
