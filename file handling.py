
sample = open("bulade.txt", "a") # open file with file name and mode in a string format
sample.write("\nOkeng is so sexy") # we can the use the .write to write information
sample.close()  # for every file we open ,it has to be closed


sample = open("bulade.txt", "r")
print(sample.read())
sample.close()