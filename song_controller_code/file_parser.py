class FileParser:
    def __init__(self):
        self.port = ""
        self.songs = {}

    # get data from config.txt
    def ParseAndGetConfig(self):
        self.config = open("config.txt", "r")
        property_names = ["port:", "path_to_firefox:", "path_to_geckodriver:"]

        index = 0
        for name in property_names:

            line = self.config.readline()[:-1]

            if line[0:len(name)] != name:
                print("Wrong config format")
                exit(1)

            if index == 0:
                self.port = line[len(name):].strip()
            elif index == 1:
                self.firefox_path = line[len(name):].strip()
            else:
                self.geckodriver_path = line[len(name):].strip()
            index = index + 1

        self.config.close()
        return self.port, self.firefox_path, self.geckodriver_path

    # get data from links.txt as a dictionary {name : url}
    def ParseAndGetSongs(self):
        self.links = open("links.txt", "r")
        for line in self.links:
            index = line.find("-")
            self.songs[line[0 : index].strip()] = line[index + 1: -1].strip()

        self.links.close()
        return self.songs
