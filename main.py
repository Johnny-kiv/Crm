import os
import xml.etree.ElementTree as ET
from flask import Flask, render_template

app = Flask(__name__)
def xml(tag,file):
    root_node = ET.parse(file).getroot()
    for elem in root_node.iter():
        if elem.tag == tag:
            return elem.text

@app.route('/')
def main():
    files = os.listdir("client/0001/tasks")
    res_list = []
    for f in files:
        path = "client/0001/tasks/"+f
        href = "window.location.href = '"+"http://192.168.1.11:5000/"+f.split("task_")[1].split(".xml")[0]+"';"
        number = f.split("task_")[1]
        name = xml("title",path)
        d = xml("description",path)
        descr=''
        for i in range(60):
            descr+=d[i]
        root_node = ET.parse(path).getroot()
        for elem in root_node.iter():
            if elem.tag == "data":
                executor = elem.attrib['executor']
                data = elem.attrib['expiration']
                status = elem.attrib['status_payment']
        d1 = {"href":href, "name":name, "descr":descr,"author":executor,"data":data,"status":status}
        res_list.append(d1)
    return render_template('panel.html',res_list=res_list)
@app.route("/<number>")
def one(number):
    path = f"client/0001/tasks/task_1.xml"
    name = xml("title",path)
    descr = xml("description",path)
    root_node = ET.parse(path).getroot()
    for elem in root_node.iter():
        if elem.tag == "data":
            executor = elem.attrib['executor']
            data = elem.attrib['expiration']
            status = elem.attrib['status_payment']
    return render_template('tasks-descriptions/'+number+'.html',name=name, descr=descr,author=executor,data=data,status=status)


if __name__ == '__main__':
    app.run("0.0.0.0")