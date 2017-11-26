import os

#Each website you crawl is a separate project/folder

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory " + directory)
        os.makedirs(directory)

# create queue and crawled files

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled= project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)  #file path,data going in the file
    if not os.path.isfile(crawled):
        write_file(crawled, '') #empty file

#create a new file
def write_file(path, data):
    f =open(path, 'w')
    f.write(data)
    f.close()

#add data to an existing file

def append_to_file(path, data): #what file to append to and what data to add
    with open(path, 'a'): #a means append, with ????
        file.write(data + '\n')

# Delete contents of a file

def delete_file_contents(path):
    with  open(path, 'w'):
        pass
