import os

MAX_TRIES = 7
DEFAULT_FILE_PATH = 'words.txt'
HANGMAN_PHOTOS = {1: """x-------x\n""",
                  2: """    x-------x
    |
    |
    |
    |
    |                        """,
                  3: """    x-------x
    |       |
    |       0
    |
    |
    |
                            """,
                  4: """    x-------x
    |       |
    |       0
    |       |
    |
    |
                        """,
                  5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
                       """,
                  6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
                  7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def start_game():
    """
    function prints out the word HANGMAN to start the game
    :return: prints out the word HANGMAN
    """
    print("""
        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/ 
                           """)
    print("You have 6 chances to guess the secret word, "
          "LET'S GET THIS PARTY STARTED!!\n")


def choose_word(index, file_path=DEFAULT_FILE_PATH):
    """
    function get a file with words and an index, and prints out a word from
    this file according to the index
    :param file_path: file path
    :param index: will be used to select the word
    :type file_path: str
    :type index : int
    :return: the chosen word from the file
    """
    with open(file_path) as file:
        word_file = file.read().split()
        counter = 0
        while counter < index:
            for indx in word_file:
                word_to_print = indx
                counter += 1
                if (index - 1) < counter:
                    break
    print("The secret word has been chosen!\n")
    return word_to_print


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function check if the guessed letter is valid,
    and appends it to the list and return True.
    else, if it is not valid, prints out 'X',
    the list of the guessed letters so far and returns false
    :param letter_guessed: the letter the user guessed
    :param old_letters_guessed: a list of the guessed letters so far
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        old_letters_guessed.sort()
        print("X")
        print(" -> ".join(old_letters_guessed))
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """
        This function is doing QA for the guessed letters,
        is the letter valid?
        and if the letter has been already used?
        :param letter_guessed: input letter from user
        :param old_letters_guessed: list of guessed letters
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: boolean
        """
    if not (not (
            len(letter_guessed) > 1) and letter_guessed.isalpha() and not (
            letter_guessed.lower() in old_letters_guessed)):

        return False

    elif len(letter_guessed) == 1 and letter_guessed.isalpha():

        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    prints the secret word with guessed letter or  _ _
    :param secret_word: str
    :param old_letters_guessed: list
    :return: list as secret word with guessed letter or  _ _
    """
    progress_word = ' '.join(
        [letter if letter in old_letters_guessed else '_' for letter in
         secret_word])
    print(progress_word)
    return progress_word


def check_win(secret_word, old_letters_guessed):
    """
    checks if the user guessed the word with his letters
    :param secret_word: list
    :param old_letters_guessed: list
    :return True if the word is guessed fully, else False
    :rtype boolean
    """
    diff = set(secret_word) - set(old_letters_guessed)
    if diff:
        return False
    else:
        return True


def print_hangman(num_of_tries):
    """
    function prints out the hangman sketch according to the number of tries of
    the user
    :param num_of_tries: get the number of tries of the user
    :type num_of_tries : int
    :return: prints out the hangman sketch according to the number of tries of
            the user
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def game(word, list_of_guessed_letters):
    """
    this function runs the process of the game. gets the chosen secret word
    and the list of guessed letters so far.
    :param word: the secret word chosen
    :param list_of_guessed_letters: list of guessed letters so far
    :type word: str
    :type list_of_guessed_letters: list
    :return: prints a massage when the user lost or won the game
    """
    number_of_tries = 1
    show_hidden_word(word, list_of_guessed_letters)
    while not check_win(word, list_of_guessed_letters):
        letter = input("\nGuess a letter: ")
        if try_update_letter_guessed(letter, list_of_guessed_letters):
            if (number_of_tries < MAX_TRIES) and letter.lower() not in word:
                number_of_tries += 1
                print(":(")
                print_hangman(number_of_tries)
            if number_of_tries == MAX_TRIES:
                print("\nGAME OVER - YOU LOSE\n")
                return
        print("\nreminder of the secret word pattern:")
        show_hidden_word(word, list_of_guessed_letters)
    print("\nGAME OVER - YOU ARE A WINNER!\n")


def get_valid_file():
    """
    function is asking for a file path and checking if the file exists,
    and if not returns a comment to try again
    :return file path
    :rtype str
    """
    file_path = input("Please insert your file path here: ")
    exists = os.path.isfile(file_path)
    while not exists:
        print("File does not exists, please check file path")
        return get_valid_file()
    return file_path


def get_valid_index():
    """
    function is asking to input an index and checks
    if the input is valid (a number)
    :return inx
    :rtype inx: int
    """
    inx = input("please choose the word index: ")
    if not inx.isdigit():
        print("You must enter a number")
        return get_valid_index()
    else:
        return int(inx)


def main():
    start_game()

    end_the_game = False

    if os.path.isfile(DEFAULT_FILE_PATH):
        input_file_path = DEFAULT_FILE_PATH
    else:
        input_file_path = get_valid_file()

    while not end_the_game:
        input_index = get_valid_index()
        chosen_secret_word = choose_word(input_index, input_file_path)
        print("Since you are on your first guess, your man is not yet hanged"
              " but the hanger is here waiting for you: ")

        # print first level
        print_hangman(1)
        
        main_list_of_guessed_letters = []
        game(chosen_secret_word, main_list_of_guessed_letters)

        # ask the user if we wants to keep playing
        keep_playing = input("\nTo try again press 'Y'  "
                             "\nTo exit press 'N' \n")

        if keep_playing == "N" or keep_playing == "n":
            end_the_game = True


if __name__ == "__main__":
    main()
