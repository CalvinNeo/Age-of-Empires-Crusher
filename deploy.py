#coding: utf8

import shutil, os

def deploy():
    tar = "D:/Games/AOE_UserPatch/Ai/"
    shutil.copyfile('Crusher.ai', tar + "Crusher.ai")
    shutil.copyfile('Crusher.per', tar + "Crusher.per")
    if os.path.exists(tar + "Crusher"):
        shutil.rmtree(tar + "Crusher")
    shutil.copytree('Crusher/', tar + "Crusher")

namespace_configs = {
    "global": {"path" : "Crusher/glx.per", "startid" : 101, "contents" : []},
    "dark": {"path" :  "Crusher/glx.per", "startid" : 1, "contents" : []},
    "feudal": {"path" : "Crusher/glx.per", "startid" : 1, "contents" : []},
    "castle": {"path" : "Crusher/glx.per", "startid" : 1, "contents" : []},
    "imperial": {"path" : "Crusher/glx.per", "startid" : 1, "contents" : []},
}

unique_files = list(set([namespace_configs[k]["path"] for k in namespace_configs.keys()]))

def configure():
    current_namespace = "global"
    current_index = 1
    f = open("gl.txt", "r+")
    while True:
        line = f.readline() 
        if not line:
            break
        line = line.strip(" ").strip("\n")

        if line == "":
            pass
        elif line.startswith("#"):
            pass
        elif line.startswith(":"):
            current_namespace = line[1:]
            print "change folder to", current_namespace
        else:
            namespace_configs[current_namespace]["contents"].append(line)

    # clean files
    for x in unique_files:
        ff = open(x, "w")
        ff.close()

    for namespace in namespace_configs.keys():
        fout = open(namespace_configs[namespace]["path"], "a")
        for item in namespace_configs[namespace]["contents"]:
            fout.write("(defconst {} {})\n".format(item, namespace_configs[namespace]["startid"]))
            namespace_configs[namespace]["startid"] += 1
        fout.close()
if __name__ == '__main__':
    configure()
    deploy()