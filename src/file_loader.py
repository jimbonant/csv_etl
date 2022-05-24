from src.some_storage_library import SomeStorageLibrary

class FileLoader:
    def __init__(self):
        self.lines = list()

    def __get_columns(self, file):
        try:
            f = open(file, "r")
            self.lines = f.readlines()
            # sort the columns
            self.lines.sort(key=lambda a: int(a.split("|")[0]))
            # format the columns
            for idx, a in enumerate(self.lines):
                self.lines[idx] = str(a).split("|")[1].rstrip()
            #put the pipe in one more time for simplicity
            for idx,a in enumerate(self.lines):
                if idx != len(self.lines) -1:
                   self.lines[idx] = a + "|"
            self.lines.append("\n")
            f.close()
        except:
            print("there was an issue processing the column headers")

    #open the data file and merge the columns to the front of it, with a little formatting
    def __merge_header(self,file):
        try:
            f = open(file, "r")
            #put the lines in a list to prepre for prepending headers
            ls = f.readlines()
            #prepend headers
            ls.insert(0,''.join(self.lines))
            #change pipes to commas probably should be pulled out to sperate function but I got to get to work here
            for idx,a in enumerate(ls):
                ls[idx] = a.replace("|",",")
            outfile = open("outfile.csv", "w")
            #write the list lines to file
            for a in ls:
                outfile.write(a)
            outfile.close()
        except:
            print("There was a problem merging the columns with the the data")

    def __validate(self,dfile):
       try:
        f = open(dfile,"r")
        ls = f.readlines()
        line = ls[0]
        #see if we have the same amount of headers and columns
        if(len(str(line).split("|")) != (len(str(self.lines).split("|")))):
            print( "Error files are the wrong shape, found %i columns in header and %i, columns in the data" % ((len(str(line).split("|"))), len(str(self.lines).split("|"))))
            return False
        else:
            return True
       except:
           print("problem validting inputs")

    def load_files(self, cfile,dfile):
        print("Processing headers")
        self.__get_columns(cfile)
        print("Validating files")
        if self.__validate(dfile) != True:
            return
        print("Mergeing headers and data")
        self.__merge_header(dfile)
        print("Moveing files to destination")
        try:
            ssl = SomeStorageLibrary()
            ssl.load_csv("outfile.csv")
        except:
            print("There was a problem moving the completed csvfile")