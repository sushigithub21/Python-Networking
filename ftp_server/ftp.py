import ftplib

#Define credentials
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

#Connect to FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

#Get welcome message
print(ftp.getwelcome())

def get_cwd():
    #Get current directory path
    print(ftp.pwd())

def ls_dir():
    #Produce a directory listing
    ftp.dir()

def ls_files():
    #Produce a list of files in the directory
    print(ftp.nlst())

def create_folder():
    #Create a new folder in the directory
    folder = input("Enter name of the folder to be created: ")
    ftp.mkd(folder)

def set_cwd():
    #Set the new folder as the current directory
    folder = input("Enter name of the folder to change directory: ")
    ftp.cwd(folder)
    #Get current directory path
    print(ftp.pwd())

def upload_files():
    #Upload file to FTP server
    file = ("Provide the local file path with file name to be uploaded: ")
    with open(file, 'rb') as f:
       ftp.storbinary('STOR ' + file, f)
    #Produce a list of files in the directory
    print(ftp.nlst())

def download_files():
    #Download file from FTP server
    file = ("Provide the local file path with file name to be downloaded: ")
    with open(file, 'wb') as f:
        ftp.retrbinary('RETR ' + file, f.write)

def delete_file():
    #Delete file from FTP server
    file = ("Provide the name of file to be deleted: ")
    ftp.delete(file)
    #Produce a list of files in the directory
    print(ftp.nlst())

def rename_file():
    #Rename file in FTP server
    file1 = ("Provide the name of file to be named: ")
    file2 = ("Provide the new name for the file: ")
    ftp.rename(file1, file2)
    #Produce a list of files in the directory
    print(ftp.nlst())

if __name__ == "__main__":
    exit = True

    while(exit):
        print("Choose from the below operation for FTP server")
        print("1)   Get current working directory")
        print("2)   List all the directories")
        print("3)   Get the list of files present")
        print("4)   Change to current working directory")
        print("5)   Create a new folder in current working directory")
        print("6)   Upload file to current working directory")
        print("7)   Download file from current working directory")
        print("8)   Rename a file in current working directory")
        print("9)   Delete a file in current working directory")
        print("10)  Exit FTP server")
        choice = int(input("Enter the Choice:"))
        match choice:
            case 1:
                get_cwd()
            case 2:
                ls_dir()
            case 3:
                ls_files()
            case 4:
                set_cwd()
            case 5:
                create_folder()
            case 6:
                upload_files()
            case 7:
                download_files()
            case 8:
                rename_file()
            case 9:
                delete_file()
            case 10:
                exit = False
                break
