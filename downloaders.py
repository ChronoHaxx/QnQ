import requests 
from urls import links # extract links that contains pdf downloads urls
from pathlib import Path
p = Path("mathematics").resolve() # find windows path to current dir

for link in links :

    r = requests.get(link, stream = True)    
    file_name: str = link.split("/")[-2] + '_' + link.split("/")[-1]
    with open(str(p) + '/' + file_name,"wb") as pdf: 
        for chunk in r.iter_content(chunk_size=1024): 
        
             # writing one chunk at a time to pdf file 
             if chunk: 
                 pdf.write(chunk) 
    
    print('File ' + file_name + ' downloaded successfully.')

print('All files downloaded successfully. :D')