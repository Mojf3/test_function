
def change_path(path):
    if path[0]=='/':
        path=path[5].upper()+':'+path[6:]
        for i in range(len(path)):
            if path[i]=='/':
                path=path[:i]+'\\'+path[i+1:]
    else:
        path='/mnt/'+path[0].lower()+path[2:]
        for i in range(len(path)):
            if path[i]=='\\':
                path=path[:i]+'/'+path[i+1:]
    return path


