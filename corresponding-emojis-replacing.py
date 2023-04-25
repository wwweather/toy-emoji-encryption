import re
from typing import Dict

EMOJIS = {
    "smile": ["😊", "😆"],
    "laugh": ["🤣", "😂"],
    # add more mappings here...
}

def replace_words_with_emojis(text: str) -> str:
    def handle_pair(match):
        emoji = match.group(0)
        return [emoji] if len(EMOJIS[emoji]) == 1 else EMOJIS[emoji][::-1]

    result = []
    for word, emojis in EMOJIS.items():
        result.append("({})".format("|".join([re.escape(e) for e in emojis])) + "\w*")
    
    pattern = r"\b(?:{})\b".format("|".join(result))
    matches = re.finditer(pattern, text)

    for i, match in enumerate(matches, start=1):
        if (i % 5) == 0:
            print(f"{i}: '{match.group(0)}' => {''.join(handle_pair([match.group() for _ in range(len(word))]))}")

        replacement = match.group(2)
        if not replacement:
            continue
        
        for pair in handle_pair(replacement[:6]):
            print("Embedding pair '{}', {}th iteration...".format(pair, len(replace_words_with_emojis)))
            # TODO: embed this pair into the resulting text by replacing its first occurrence with one emoji from each pair in this order: 1st, then 3rd, then 2nd. Remove all other occurrences of the original word.

    return "The output after converting every fifth pair:\n\n" + finalized_string
