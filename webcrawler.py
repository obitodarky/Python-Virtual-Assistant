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

#Read a file and convert each line to set items

def file_to_set(file_name):
    results = set() #an empty set
    with open(file_name,'rt') as f: #read text files as f
        for line in f:
            results.add(line.replace('\n','')) #add each line to the set and replace the new lines with '' cuz we dont need new lines in a set
    return results #returning the value of results

#Iterate through a set ,each item will be a new line in the file

def set_to_file(links, file): #the links we wanna save to the particular file
    delete_file_contents(file)
    for link in sorted(links): #sort in alphabetical order
        append_to_file(file,link)


