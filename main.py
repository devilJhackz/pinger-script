import csv
import os

file = open('input.csv','r')
reader=csv.reader(file)

for lines in reader:
    for i in range(len(lines)):
        with open('output.csv','a') as output:
            writter=csv.writer(output)
            if i==0:
                writter.writerow(('IP','STATUS','DOMAIN','TTL VALUE'))
            # response = os.system('ping -n 1 -a ' +lines[i])
            response =os.popen("ping -a -n 1 " +lines[i]).read()
            # print(response)

            if response.find('Reply') != -1 and response.find('Destination host unreachable.') == -1:
                status = "Up";
                domain = response.split('Pinging')[1].split()[0]
                ttl = response.split('TTL=')[1].split('\n')[0]
                output_list=(lines[i],status,domain,ttl)
                writter.writerow(output_list)
            else:
                status = "Down"
                output_list=(lines[i],status,'-','-')
                writter.writerow(output_list)
