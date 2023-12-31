def unix_to_windows(path):
    if(path[0:2]=="C:"):
        value = "ERROR: already a windows path"
    else:
        x = path.split("/")
        x.remove(x[0])
        x.insert(0,"C:")
        x = "/".join(x)
        value = x
    return value

def windows_to_unix(path):
    if(path[0:2]!="C:"):
        value = "ERROR: already a unix path"
    else:
        x = path.split("/")
        x.remove(x[0])
        x.insert(0, "")
        x = "/".join(x)
        value = x
    return value



print(unix_to_windows("C:/desktop/cool"))
print(unix_to_windows("/desktop/cool"))
print()
print(windows_to_unix("/desktop/cool"))
print(windows_to_unix("C:/desktop/cool"))