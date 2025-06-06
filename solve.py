def load_dictionary(dict_path: str) -> tuple[set[str], set[str]]:
    """
    Generates a legal words set and a prefix set for efficiency during word searching. 
    """
    word_set = set()
    prefix_set = set()
    
    with open(dict_path, 'r') as f:
        for line in f:
            word = line.strip().lower()
            if not word:
                continue
            
            word_set.add(word)
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
    
    return word_set, prefix_set

def get_tiles():
    input_tiles: list[str]
    input_tiles = []
    print("Enter each tile one by one")
    for i in range(20):
        tile = input().strip().lower()
        if tile:
            input_tiles.append(tile)
        else:
            print("Tile cannot be empty")
            while not tile:
                tile = input().strip().upper()
                if tile:
                    input_tiles.append(tile)
    
    return input_tiles

def find_valid_words(tiles: list[str], word_set: set[str], prefix_set: set[str]) -> dict[int, list[list[str]]]:
    """
    Generate valid words from the given tiles using up to 4 tiles per word.
    tiles: List of tile strings
    word_set: legal words

    Returns dictionary where keys are tile counts (1-4) and values are lists of valid word breakdowns.
    """
    valid_words = {1: [], 2: [], 3: [], 4: []}
    
    for i, tile in enumerate(tiles):
        add_tile(valid_words, [tile], tiles[:i] + tiles[i+1:], word_set, prefix_set, 1)
    
    return valid_words


def add_tile(valid: dict[int, list[list[str]]], curr: list[str], left: list[str],
             word_set: set[str], prefix_set: set[str], count: int):
    """
    Recursively builds words by adding one tile at a time
    """
    word = ''.join(curr)
    
    if word not in prefix_set:
        return
    
    if word in word_set:
        valid[count].append(curr.copy())
    
    if count == 4 or not left:
        return 
    
    for i, tile in enumerate(left):
        add_tile(valid, curr + [tile], left[:i] + left[i+1:], word_set, prefix_set, count + 1)
        

def display_valid_words(valid_words: dict[int, list[list[str]]]):
    """
    Answers display for now
    """
    for count in range(1, 5):
        print(f"{count} tiles:")
        for word_tiles in valid_words[count]:
            print(f"  {''.join(word_tiles)} ({' + '.join(word_tiles)})")
        print()
        
    

def solve_puzzle(tiles):
    dictionary, prefix = load_dictionary("dictionary.txt")
    valid_words = find_valid_words(tiles, dictionary, prefix)
    
    solutions = {}
    for count in range(1, 5):
        solutions[count] = []
        for word_tiles in valid_words[count]:
            word = ''.join(word_tiles)
            breakdown = ' + '.join(word_tiles)
            solutions[count].append((word, breakdown))
    return solutions

    

if __name__ == "__main__":
    dictionary, prefix = load_dictionary("dictionary.txt")
    tiles = get_tiles()
    valid_words = find_valid_words(tiles, dictionary, prefix)
    display_valid_words(valid_words)
