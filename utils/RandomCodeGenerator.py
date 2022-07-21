from random import randint, shuffle


class RandomCodeGenerator:
    code_length = 5

    def generate_random_string(self):
        letters = "abcdefghijklmnprstuvyzqw123456789".upper()

        list_letters = [char for char in letters]
        shuffle(list_letters)

        generated = ""
        for i in range(0, self.code_length):
            generated += list_letters[randint(0, len(letters) - 1)]
        return generated


generator = RandomCodeGenerator()
