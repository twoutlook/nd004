import os
import random

def encrypt_files():
    file_list=os.listdir(r"D:\000-udacity\nd004\mini2")
    cwd=os.getcwd()
    # print(cwd)
    os.chdir(r"D:\000-udacity\nd004\mini2")
    # print(file_list)
    for file_name in file_list:
        temp_file_name=file_name.translate(None, "0123456789")
                
        # print(file_name)
        num= random.randint(123, 999)
        # print(num)
        # need to convert number to string before +
        new_file_name=str(num)+temp_file_name

        # print(new_file_name)
        os.rename(file_name, new_file_name)
        
    print("encrypt_files, done!");

def decrypt_files():
    file_list=os.listdir(r"D:\000-udacity\nd004\mini2")
    cwd=os.getcwd()
    # print(cwd)
    os.chdir(r"D:\000-udacity\nd004\mini2")
    # print(file_list)
    for file_name in file_list:
        temp_file_name=file_name.translate(None, "0123456789")
                
        # print(file_name)
        # num= random.randint(123, 999)
        # print(num)
        # need to convert number to string before +
        # new_file_name=str(num)+temp_file_name

        # print(new_file_name)
        os.rename(file_name, temp_file_name)
        
    print("decrypt_files, done!");

# comment and uncomment to determine which function to run    
encrypt_files()                         

# decrypt_files()                         

