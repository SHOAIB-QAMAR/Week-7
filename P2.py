# 1. Copying Files — cp

#    The cp (copy) command is used to copy files or directories.
#    i. copies file1.txt to file2.txt: 
#               cp [options] source destination
#    ii. Copy a file to another directory: 
#               cp file1.txt /home/user/Documents/
#    iii. Copy a directory (with contents):
#               cp -r dir1/ dir2/

# 2. Moving or Renaming Files — mv

# The mv (move) command is used to move files or rename them.
#     mv [options] source destination

#    i. Rename a file:
#           mv oldname.txt newname.txt
#    ii. Move a file to another directory:
#           mv file1.txt /home/user/Documents/
#    iii. Move a directory:
#           mv dir1/ /home/user/Documents/


#  3. Removing Files — rm

# The rm (remove) command deletes files or directories.
#       rm [options] file

#  i. Remove a file:
#           rm file1.txt
#  ii. Remove multiple files:
#           rm file1.txt file2.txt file3.txt
#  iii. Remove a directory (with contents):
#           rm -r dir1/
#  iv. Force removal without confirmation (-f = force, be careful with this option!):
#           rm -rf dir1/