from pathlib import Path

# to get absolute path of the file
curr_Dir = Path(__file__).resolve()
print (curr_Dir)

# to get the file name
file4name = curr_Dir.stem+".h5"
#file4name = str(file4name1+".h5")
print (file4name)


file_dir = (Path(__file__).resolve().parent)
print (file_dir)

print (file_dir.joinpath(file4name))
#print (str(file_dir)+ file4name)
