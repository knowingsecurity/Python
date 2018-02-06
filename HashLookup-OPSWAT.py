import requests
import csv
import json


hashes = [line.rstrip('\n') for line in open('filenameforhashes.txt')]
r=["Hash", "FileName", "Positivies"]
f=open('Hashwithfilenames.csv', 'wb')
w=csv.writer(f)
w.writerow(r)



for i in hashes:
    url = "https://api.metadefender.com/v2/hash/"+i
    headers = {'apikey': "Your Key"    }
    response = requests.request("GET", url, headers=headers)
    data=response.json()
    try:
        print "for Hash: " + i
        print(data["file_info"]["display_name"])
        print(data["scan_results"]["total_detected_avs"])
        r=[];
        r.append(i)
        r.append(data["file_info"]["display_name"])
        r.append(data["scan_results"]["total_detected_avs"])
        w.writerow(r)
    except:
        try:
            data[i]="Not Found"
            print "Not Found"
            r=[];
            r.append(i)
            r.append(data[i])
            w.writerow(r)
        except:
            print "Not Available"
            r=[];
            r.append(i)
            r.append("Not Available")
            w.writerow(r)         
f.close()
