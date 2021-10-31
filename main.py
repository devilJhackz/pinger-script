"""
*
*
*
*   File edited on 31st October 2021
*
*
*
"""
import csv
import os
input_file='input.csv'
output_file='output.csv'
file = open(input_file,'r')
reader=csv.reader(file)

for lines in reader:
    for i in range(len(lines)):
        with open(output_file,'a') as output:
            writter=csv.writer(output)
            if i==0:
                writter.writerow(('IP','STATUS','DOMAIN','TTL VALUE','OS TYPE'))
            response =os.popen("ping -a -n 1 " +lines[i]).read()
            if response.find('Reply') != -1 and response.find('Destination host unreachable.') == -1:
                status = "Up"
                os_type=""
                domain = response.split('Pinging')[1].split()[0]
                ttl = response.split('TTL=')[1].split('\n')[0]
                #getting OS type from ttl code
                if ttl==128 or ttl==32:
                    os_type="Windows"
                elif ttl==255 or ttl==64:
                    os_type="Linux"
                elif ttl==60:
                    os_type="MacOS 2.0.x"
                elif ttl==254:
                    os_type="Cisco"
                output_list=(lines[i],status,domain,ttl,os_type)
                writter.writerow(output_list)
            else:
                status = "Down"
                output_list=(lines[i],status,'-','-','-')
                writter.writerow(output_list)
