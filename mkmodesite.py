import imp
import os
import traceback


def get_immediate_subdirectories(dir):
    if os.path.isdir(dir):
        return [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name)) and name != ".git"]  
    else :
        return []

mode_folders = sorted(get_immediate_subdirectories("ETC_Modes"), key=lambda s: s.lower() )

out = "<table>"

for mode_folder in mode_folders :
    out += "<tr>"
    mode_info_path = "ETC_Modes/" + mode_folder + '/info.py'
    try :
        info = imp.load_source('info', mode_info_path)
        
        out += "<td>" + str(mode_folder) + "</td>"
        out += "<td>" + str(info.description) + "</td>"
        out += "<td>" + str(info.knob1) + "</td>"
        out += "<td>" + str(info.knob2) + "</td>"
        out += "<td>" + str(info.knob3) + "</td>"
        out += "<td>" + str(info.knob4) + "</td>"
        out += "<td><img src=\"ETC_Modes/" + mode_folder + "/preview.jpg\" style=\"width:128px;height:72px;\"></td>"
    except Exception, e:
        print traceback.format_exc()
    out += "</tr>\n"

out += "</table>"
print out    

