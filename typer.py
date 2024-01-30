import time
import keyboard
import random

def extract_text(data):
    first_letter = data.get('firstLetter', '')
    remaining_words = data.get('words', '')

    print(f"First Letter: {first_letter}")
    print(f"Remaining Words: {remaining_words}")

def introduce_typing_errors(word, current_wpm, error_slowdown=6):
    error_probability = 0.006
    error_word = ""

    for char in word:
        if random.random() < error_probability:
            error_word += random.choice('abcdefghijklmnopqrstuvwxyz')
            current_wpm -= error_slowdown
        else:
            error_word += char

    return error_word, current_wpm

def hold_and_release_key(key):
    start_time = time.time()
    keyboard.press(key)
    while keyboard.is_pressed(key):
        pass
    key_down_duration = time.time() - start_time
    keyboard.release(key)

    random_key_delay = max(0, random.uniform(0.007, 0.09) - key_down_duration)
    time.sleep(random_key_delay)

def type_text_at_wpm(text, target_wpm=200, stop_key='tab'):
    print(f"Press '{stop_key}' to stop typing.")
    time.sleep(5)

    current_wpm = target_wpm
    words_per_second = current_wpm / 1

    for word in text.split():
        word_delay = max(0, 1 / words_per_second)
        word_delay += random.uniform(-0.05, 0.05)

        error_word, current_wpm = introduce_typing_errors(word, current_wpm)
        for char in error_word:
            keyboard.write(char)
            key_delay = max(0, random.uniform(0.007, 0.09))
            time.sleep(key_delay)

        hold_and_release_key('space')

        word_pause = max(0, random.uniform(0.01, 0.1))
        time.sleep(word_pause)

        if keyboard.is_pressed(stop_key):
            print("\nTyping stopped.")
            return

if __name__ == "__main__":
    text_to_type = input("Enter the text to type: ")

    try:
        type_text_at_wpm(text_to_type)
    except KeyboardInterrupt:
        print("\nTyping interrupted.")
