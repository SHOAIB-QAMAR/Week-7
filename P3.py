# 1. Creating Directories — mkdir
       
#    The mkdir (make directory) command is used to create new directories.
#    mkdir [options] directory_name
#
#    i. Create a single directory: (Creates a directory named myfolder in the current location)
#           mkdir myfolder
# 
#    ii. Create multiple directories at once:
#           mkdir dir1 dir2 dir3
# 
#   iii. Create a nested directory structure (with parent directories):
#        (The -p option creates parent directories if they don’t exist)
#           mkdir -p projects/code/java

#  2. Deleting Directories — rmdir

#   The rmdir (remove directory) command deletes empty directories.
#   rmdir [options] directory_name
# 
#   i. Remove an empty directory:
#           rmdir myfolder
#   ii. Remove multiple empty directories:
#           rmdir dir1 dir2 dir3
#   iii. Remove a nested directory structure:
#           rmdir -p projects/code/java
# 
#  ⚠️ Note: rmdir works only on empty directories.
#  To remove non-empty directories, use:
#       rm -r directory_name