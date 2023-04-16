class StringFormatter():
    def __init__(self, str):
        self.__string = str
        self.__separator = " "

    def __str__(self):
        return self.__string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, value):
        self.__separator = value

    def delete(self, n):
        words = []
        word = ""
        counter = 0
        lenght = len(self.__string)
        for symbol in self.__string:
            if symbol != self.__separator:
                word += symbol
                counter += 1
            lenght -= 1
            if symbol == self.__separator or lenght == 0:
                if counter >= n:
                    words.append(word)
                word, counter = "", 0
        for w in words:
            word = word + w + self.separator
        self.__string = word[:-1]

    def replace(self):
        new_str = ""
        for symbol in self.__string:
            new_str += "*" if symbol.isdigit() else symbol
        self.__string = new_str

    def insertEnter(self):
        new_str = ""
        for symbol in self.__string:
            new_str += symbol + " "
        self.__string = new_str[:-1]

    def sortByLenght(self):
        words = []
        word = ""
        counter = 0
        lenght = len(self.__string)
        for symbol in self.__string:
            if symbol != self.__separator:
                word += symbol
                counter += 1
            lenght -= 1
            if symbol == self.__separator or lenght == 0:
                words.append([word, counter])
                word, counter = "", 0
        for i in range(len(words)-1):
            for j in range(len(words)-i-1):
                if words[j][1] > words[j+1][1]:
                    words[j], words[j+1] = words[j+1], words[j]
        for i in words:
            word += i[0] + self.__separator
        self.__string = word[:-1]

    def sortByLexical(self):
        words = []
        word = ""
        counter = 0
        lenght = len(self.__string)
        for symbol in self.__string:
            if symbol != self.__separator:
                word += symbol
                counter += 1
            lenght -= 1
            if symbol == self.__separator or lenght == 0:
                words.append(word)
                word, counter = "", 0
        for i in range(len(words)-1):
            for j in range(len(words)-i-1):
                k = 0
                while k != len(words[j]) and k != len(words[j+1]):
                    if ord(words[j][k].lower()) > ord(words[j+1][k].lower()):
                        words[j], words[j+1] = words[j+1], words[j]
                        break
                    elif ord(words[j][k].lower()) < ord(words[j+1][k].lower()):
                        break
                    k += 1
        for i in words:
            word += i + self.__separator
        self.__string = word[:-1]


if __name__ == "__main__":
    st = StringFormatter("Great morning in the Donbass")
    st.delete(5)
    st.replace()
    st.sortByLenght()
    st.sortByLexical()
    st.insertEnter()
    print(st)

