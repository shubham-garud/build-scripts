from distutils.log import ERROR, INFO, WARN
from logging import WARNING

import os
import json
import requests
import subprocess
from subprocess import call
import glob
import stat
import docker
import shutil
import sys
from datetime import date

path_separator = os.path.sep
#package_name
ROOT = os.getcwd()
#dir_name = f"{ROOT}{path_separator}{package_name[0]}{path_separator}{package_name}"
'''
char_= {$1}
print("char:",char_)
'''
#dir_char=sys.argv[1]
dir_name = f"{ROOT}/"
print("dir_name:",dir_name)

def get_files_list(dirname:str, recursive:bool=True):
    file_list = []
    for file in os.listdir(dirname):
        current_file = os.path.join(dirname, file)
        if recursive and os.path.isdir(current_file):
            file_list = file_list + get_files_list(current_file, recursive)
        else:
            file_list.append(current_file)
    return file_list

file_list = get_files_list(dir_name)

#print(file_list)

count = 0
package_dockerfile_count={}
#package_dockerfile_count.setdefault(' ',0)
for file in file_list:
    if file.endswith("Dockerfile"):
        count=count+1
        #print(file)
        package_name=file.split('/')[6]
        #package_dockerfile_count[package_name]='true'
        if package_name in package_dockerfile_count.keys():
            package_dockerfile_count[package_name]+=1
        else:
            package_dockerfile_count[package_name]=1
        #print(file)
        
    #if "Dockerfiles" in file and "README" not in file and (not (file.endswith(".sh") or file.endswith(".py"))) :
        # Read the available build-scripts and load the data.
        #print(file)
        #count=count+1
    
print("========================")
        
print("length of dictionary:",len(package_dockerfile_count))
print("Total dockerfiles in repo:",count)
print("========================")

#summa=0
single_dockerfiles=0
multiple_dockerfiles=0
list_single_df=[]
list_muliple_df=[]
for key  in package_dockerfile_count.keys():
    if package_dockerfile_count[key]>1:
        multiple_dockerfiles+=1
        list_muliple_df.append(key)
        #summa+=package_dockerfile_count[key]
    elif package_dockerfile_count[key]==1:
        single_dockerfiles+=1
        list_single_df.append(key)
'''
print("========================")
print("single df:",single_dockerfiles)
print("multiple df:",multiple_dockerfiles)

print("========================")
'''
print("========================")
print("Total packages with dockerfiles:",multiple_dockerfiles+single_dockerfiles)
print("Total packages with multiple dockerfiles:",multiple_dockerfiles)
print("========================")
'''
new_count=0
for key in package_dockerfile_count.keys():
    new_count+=package_dockerfile_count[key]
print("total count of values from dictionary",new_count)
print("=============================================================")
for key ,value in package_dockerfile_count.items():
    print(f"{key}:{value}")
#print(package_dockerfile_count)
'''

print("single packages list")
print(len(list_single_df))
print("multiple packages list")
print(len(list_muliple_df))

# total count of dm
multiple_count_dfs=0
for m_df in list_muliple_df:
    if m_df in package_dockerfile_count.keys():
        multiple_count_dfs+=package_dockerfile_count[m_df]

print("multiple_count_dfs:",multiple_count_dfs)

