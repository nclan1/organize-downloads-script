

#Declare the folder names
import os

from path import Path


#dictionary of string:set(uses {})
#find out the different file types and their extensions. 
folder_names = {
    "audio": {'aif', 'cda', 'mid', 'mp3', 'mpa', 'ogg', 'wav', 'wma'},
    "compressed-file": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip'},
    "code": {'js', 'jsp', 'html', 'ipynb', 'py', 'java', 'css'},
    "images": {'bmp', 'gif.ico', 'jpeg', 'jpg', 'png', 'jfif', 'svg', 'tif', 'tiff'},
    "docs": {'ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'doc', 'docx', 'txt', 'tex', 'epub'},
    "software": {'apk', 'bat', 'bin', 'exe', 'jar', 'msi', 'py'},
    "video": {'3gp', 'avi', 'flv', 'h264', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'wmv'},
    "other": {'NONE'}
}

#get downloads paths
download_paths = r"C:/Users/LAN/Downloads"

#creates a list (list comprehension method) to only put files (the path) from /Downloads in it
all_files = [os.path.join(download_paths, file)
             #os.path.join just joins original download path with 
             #the files using conditional if
        for file in os.listdir(download_paths)
            if os.path.isfile(os.path.join(download_paths, file))]

# #same thing but for folders 
# onlyfolders = [os.path.join(download_paths, file)
#         for file in os.listdir(download_paths)
#             if not os.path.isfile(os.path.join(download_paths, file))]


#creates a dictionary that pairs each extension to a filetype
extension_filetype_map = {extension: fileType
            #filetype goes first because in folder_name, thats the key
            #for every filetype, starting from beginning
        for fileType, extensions in folder_names.items()
            #run through all the extensions one by one
            for extension in extensions }


#creates a list of all the paths for the diff folder
#os.path.join combines the path of the download and then the folder name
folder_paths = [os.path.join(download_paths, folder_name)
                for folder_name in folder_names.keys()]


#takes the path of a file
def new_path(old_path):
    
    #grabs only the extension. 
    extension = str(old_path).split('.')[-1]
    
    #check if the extension falls under a filetype
    #if so, amp_folder store the name of the file_type
    if extension in extension_filetype_map.keys():
        amp_folder = extension_filetype_map[extension]
    else:
        amp_folder = 'other'

    #return a modified path of the file where it is located in 
    #.split(\\) just takes the filename+extension
    final_path = os.path.join(download_paths, amp_folder, str(old_path).split('\\')[-1])
    
    return final_path

#uses list comprehension to go through all files in the previously made list of all the files
#Path().rename() changes the directory of the file into the new location
[Path(eachfile).rename(new_path(eachfile)) for eachfile in all_files]