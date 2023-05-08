def word_play(input_str):
    words = input_str.split()
    processed_words = []
    for word in words:
        # a) Pick the odd position characters and move them ahead of the even-position characters
        processed_word = ''.join([word[i] for i in range(0, len(word), 2)] + [word[i] for i in range(1, len(word), 2)])
        # b) Reverse each word formed above
        processed_word = processed_word[::-1]
        # c) Take the first three characters of each of the reversed words & combine all of them using dashes('-')
        processed_words.append(processed_word[:3])
    # d) Return the final string as function output
    return '-'.join(processed_words)

