import xml.etree.ElementTree as ET
root_node = ET.parse('client/0001/tasks/task_1.xml').getroot()
for elem in root_node.iter():
    if elem.tag == "data":
        print(elem.attrib['executor'])

