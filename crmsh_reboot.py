#!/usr/bin/env python3
import subprocess
import os
import xml.etree.ElementTree as ET

def main():
    root = ET.ElementTree(ET.fromstring(get_crm_xml_status())).getroot()
    nodes_configured = int(root.find('*/nodes_configured').attrib['number'])
    nodes_count = 0
    for tag in root.findall('nodes'):
        for subtag in tag:
            if  subtag.attrib['online'] == 'true' and \
                subtag.attrib['standby'] == 'false' and \
                subtag.attrib['maintenance'] == 'false'and \
                subtag.attrib['pending'] == 'false'and \
                subtag.attrib['unclean'] == 'false'and \
                subtag.attrib['shutdown'] == 'false':
                nodes_count += 1

    if nodes_count == nodes_configured:
        os.system('reboot')
        exit()

def get_crm_xml_status():
    a = subprocess.run(["/usr/sbin/crm_mon", "--as-xml"], encoding='utf-8', stdout=subprocess.PIPE)
    return a.stdout

if __name__ == "__main__":
    main()
