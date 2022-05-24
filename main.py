from src.file_loader import FileLoader

if __name__ == '__main__':
    print('Beginning the ETL process...')
    try:
        fl = FileLoader()
        fl.load_files("./data/source/SOURCECOLUMNS.txt","./data/source/SOURCEDATA.txt")
    except:
        print("there was a problem loading the source data")

