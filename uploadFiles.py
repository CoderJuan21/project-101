import dropbox
import os

class TransferData :
     def __init__ (self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)


def main():
     access_token = "wAzQsvH04U4AAAAAAAAAAZfuCPknXrggIf6tEPZnu_E8mMwhTkSEj5oXrL0Quek2"
    transferData = TransferData(access_token)
    file_from = "C:/Users/AwesomeGamer/Downloads/Python/C-101/Sample.txt"
    file_to = "C:/Users/AwesomeGamer/Dropbox/Test/Sample.txt"
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()
