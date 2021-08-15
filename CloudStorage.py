import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = '2OVTDREB6xoAAAAAAAAAAQUzLZ3UrgNcPoOTEJoL7-1pWr6js5KKus1q-2YpLyhC'
    transferData = TransferData(access_token)

    file_from = input("Enter the Path Of The Folder To Be Transfered=> ")
    file_to = input("Enter The Full Path To Upload To Dropbox=> ")

    transferData.upload_file(file_from, file_to)
    print("File is Transfered")
main()