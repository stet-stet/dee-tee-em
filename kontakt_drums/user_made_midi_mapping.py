import os
import sys
import shutil

def do_folder(folder):
    filelist = os.listdir(folder)

    # back up
    folder_basename = os.path.basename(folder)
    shutil.copytree(folder, os.path.join("backup", filelist[0].split("_")[0]), dirs_exist_ok=False)

    data_suffix = "_mapping_data.nka"
    names_suffix = "_mapping_names.nka"

    data_fn = [e for e in filelist if e.endswith(data_suffix)][0]
    names_fn = [e for e in filelist if e.endswith(names_suffix)][0]

    print(data_fn)
    print(names_fn)

    # modify name of custom mapping to "Keyboard Warrior".
    with open(os.path.join(folder, names_fn)) as names_file:
        lines = names_file.readlines()
        suffix = lines[0].replace(f"!{names_fn.replace('.nka','')}", "") # \n or \r\n?
        lines[1] = "Keyboard Warrior" + suffix
    
    with open(os.path.join(folder, names_fn), 'w') as names_file:
        for line in lines:
            names_file.write(line)
        
    # C-2 to G8 is 128 notes
    # look at 2nd to 129th lines, determine max, and then print
    # arange(max)

    with open(os.path.join(folder, data_fn)) as data_file:
        lines = data_file.readlines()
        all_there_exists = set([int(e) for e in lines[1:128+1]])
        all_there_exists = sorted(list(all_there_exists))
        for i, ind in enumerate(all_there_exists):
            lines[1+i] = str(ind) + suffix

    with open(os.path.join(folder, data_fn), 'w') as data_file:
        for line in lines:
            data_file.write(line)

if __name__=="__main__":
    do_folder(sys.argv[1])