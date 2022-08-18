import json 
import os



class filePaths:

    def __init__(self):

        self.workingDir = None
        self.inputPath = './'
        self.outputPath = './'
        self.filePrefix = None


    def set_working_directory(self, path, relative=True):
        if (relative):
            currentDir = os.getcwd()
            self.workingDir = os.path.join(currentDir , path)
        
        else:
            self.workingDir = path

    def set_input_directory(self, path):
        path

    def get_input_file_list(self):
        fileList = []
        if self.workingDir is None:
            raise OSError('Please set working directory Currently set as:', self.workingDir )

        

        

        








MZmetaPath = filePaths()

MZmetaPath.set_working_directory('../metadata')

print("working on files in: ",MZmetaPath.workingDir)






# For reference
'''
# import required modules
import os
import json
import shutil

# assign input / output directories
directory_in = 'hashlips_images'
directory_out = 'images'
json_directory_in = 'hashlips_json'
json_directory_out = 'json'

# globals
index = 1
metadata = []
 
# iterate over files in directory_in
for filename in os.listdir(directory_in):
    f = os.path.join(directory_in, filename)
    # checking if it is a file
    if os.path.isfile(f):
        filename_json_in = os.path.splitext(filename)[0] + ".json"
        filename_img_out = str(index) + ".png"
        filename_json_out = str(index) + ".json"
        print(filename)    # output to user that we're making progress, can be commented out

        # read json
        f = open(os.path.join(json_directory_in, filename_json_in))
        data_in = json.load(f)
        f.close()
        
        # create output json
        data_out = {}
        data_out['format'] = 'CHIP-XXXX'
        data_out['name'] = "Barnyard Babies #" + str(index)
        data_out['description'] = "Barnyard Babies"
        data_out['attributes'] = data_in['attributes']
        for attr in data_out['attributes']:
            attr['type'] = attr.pop('trait_type')
            attr['value'] = attr.pop('value')

        data_out['collection'] = {}
        data_out['collection']['name'] = "Barnyard Babies"
        data_out['collection']['id'] = "15c40dc8-f30b-4531-8935-c3fcd34147cb"
        data_out['collection']['attributes'] = [
            {'type':'description', 'value':"Barnyard Babies adventure in the solar system."},
            {'type':'icon', 'value':"http://jedjacobson.art/byb/img/icon.png"},
            {'type':'banner', 'value':"http://jedjacobson.art/byb/img/banner.png"},
            {'type':'twitter', 'value':"gobber_82"},
            {'type':'website', 'value':"http://jedjacobson.art/"}
        ]
        
        # write json for the image
        with open(os.path.join(json_directory_out, filename_json_out), 'w') as outfile:
            json.dump(data_out, outfile, indent=2)

        # add json to metadata.json file (contains all individual image json files combined)
        metadata.append(data_out)

        # copy img to final folder
        shutil.copyfile(os.path.join(directory_in, filename), os.path.join(directory_out, filename_img_out))        
        
        index = index + 1
  
# write metadata
with open(os.path.join(json_directory_out, 'metadata.json'), 'w') as outfile:
    json.dump(metadata, outfile, indent=2)
'''