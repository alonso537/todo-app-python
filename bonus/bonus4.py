filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]


for filename in filenames:
    filename_new = filename.replace(".", "-", 1)
    print(filename_new)