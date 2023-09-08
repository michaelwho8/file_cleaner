import os
import datetime

directories = ["C:\\Users\\micha\\OneDrive\\Pictures\\Screenshots", "C:\\Users\\micha\\OneDrive\\Pictures\\Feedback"]
window = 30

def clean_folders(directories, window):
    """
    :param directories: a set of absolute file paths of directories in strings
    :param window: number of days before deletion
    :return: <todo>
    """
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=window)

    for dir_path in directories:
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if datetime.datetime.fromtimestamp(os.path.getctime(file_path)) < cutoff_date:
                os.remove(file_path)

clean_folders(directories, window)