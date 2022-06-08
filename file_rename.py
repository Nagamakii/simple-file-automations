import os

def rename():
    for count, files in enumerate(os.listdir("\Code Projects\simple-file-automations")):
        os.rename(f"\Code Projects\simple-file-automations\{files}_{count}")

if __name__ == "__main__":
    rename()