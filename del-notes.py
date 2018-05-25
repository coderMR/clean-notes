
# -*- coding:utf-8 -*- 

#####################################
######### 剔除'#'开头的注释 #########
#####################################

import re

def main():
    if __name__ == "__main__":

        #################
        # Get file path #
        #################
        file_p = input("Please enter file path:")
        
        #######################
        # Get the point index #
        #######################
        i = file_p.index('.')
        
        ##################################
        # Get the file reader and writer #
        ##################################
        reader = open(file_p, "r")
        writer = open(file_p[:i] + '[no-notes]' + file_p[i:], "w")
        
        #########################
        # Delete the letter '#' # 
        #########################
        while True:
            line = reader.readline()
            if not len(line):
                reader.close()
                writer.close()
                break
            line = re.sub(r"^\s*#.*\n$", lambda match_obj:None, line)
            writer.write(line)

main()


