import random

def introduce_typo(word):
    if len(word) <= 1:
        return word
    typo_type = random.choice(["swap", "delete", "replace"])
    if typo_type == "swap" and len(word) > 1:
        i = random.randint(0, len(word) - 2)
        return word[:i] + word[i+1] + word[i] + word[i+2:]
    elif typo_type == "delete":
        i = random.randint(0, len(word) - 1)
        return word[:i] + word[i+1:]
    elif typo_type == "replace":
        i = random.randint(0, len(word) - 1)
        return word[:i] + random.choice("abcdefghijklmnopqrstuvwxyz") + word[i+1:]
    return word

def introduce_typos_to_text(text, typo_chance=0.1):
    words = text.split()
    new_words = []
    for word in words:
        if random.random() < typo_chance:
            new_words.append(introduce_typo(word))
        else:
            new_words.append(word)
    return ' '.join(new_words)

