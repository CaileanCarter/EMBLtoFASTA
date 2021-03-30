[![Total alerts](https://img.shields.io/lgtm/alerts/g/CaileanCarter/EMBLtoFASTA.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CaileanCarter/EMBLtoFASTA/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/CaileanCarter/EMBLtoFASTA.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/CaileanCarter/EMBLtoFASTA/context:python)

# EMBLtoFASTA

The EMBLtoFASTA Python script allows the conversion of EMBL file formats to bare FASTA formats. It is a simplistic and bare bones script for the file conversion and has some limitations. 

The script asks the user for the EMBL file path so it can be read. The script will also ask the user to give the file a name and will check the user's file library to ensure no file of the same name is overwritten - if a file already exists then the user will be asked to provide a different name. 

The disadvantages to the script is it is rather slow, particularly in dealing with larger file sizes. This may be due to how it is handling the file contents and parsing of the EMBL file through the main function. As it deals with each letter individually, this may be causing slow downs in larger files. This could be something to improve in future versions.

The reason for writing the script was a lack of a publicly available tool suitable for the conversion. Initially, the script was going to separate the sequence according to the annotations provided by the EMBL, but this proved challenging, time consuming and resource intensive for larger EMBL files (such as whole genome sequences). Therefore, before moving onto other projects and to prevent this script being lost and forgotten, I have simplified and condensed the script so it has functionality to extract the sequence information and write into a FASTA format for any future use. 
