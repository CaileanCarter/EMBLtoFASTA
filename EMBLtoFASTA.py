import os.path as FindFile

def FileInterpreter():
    UserFileName = input("Name your fasta file:  ")
    FileName = UserFileName + ".fasta"

    if not FindFile.exists(FileName): #ensures file doesn't already exist
        return(FileName)
        
    else:
        print("Error: this file already exists")
        FileInterpreter()

if __name__ == "__main__":
    #ask user for file path
    EMBLfile = open(input("Please enter the EMBL file path:  "), 'rt')

    file = open(FileInterpreter(), "a+")   
    
    [[file.write(''.join([Nucleobase for Nucleobase in row if not Nucleobase.isdigit()]).upper().replace(" ", ""))] for row in EMBLfile if row[:2] == "  "]
    file.close()