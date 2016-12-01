import dryscrape
import pandas
import re
import requests
import time

url = 'http://www.piliakalniai.lt/piliakalnis.php?piliakalnis_id='
total_hillforst = 901
hillforts = []
data = {}

session = dryscrape.Session()

# will be using this to pause requests
counter = 0

for h_fort in range(801, total_hillforst):
    session.reset()
    # time.sleep(10)
    if counter == 50:
        time.sleep(30)
        counter = 0
    counter += 1
    print('working on id: {0}'.format(h_fort))

    # sometimes server got too busy and request returns error
    try:
        session.visit(url + str(h_fort))
        table = session.at_xpath('//*[@id="pil_table_div"]')
    except:
        print('=======================================================')
        print('Url with id: {0} timed out.'.format(h_fort))
        print('Waiting for 40 seconds and trying again.')
        time.sleep(40)
        session.visit(url + str(h_fort))
        table = session.at_xpath('//*[@id="pil_table_div"]')
        print('=======================================================')
        continue

    # some id's are not legit on this website and returns error
    try:
        wgs = table.children()[0].text().splitlines()[6]
    except:
        print('=============================================')
        print('Hillfort by id: {0} does not exist.'.format(h_fort))
        print('Skipping to the next iteration.')
        print('=============================================')
        continue

    wgs = re.findall('\d+\.\d+|\d+', wgs)
    wgs = [float(numeric_string) for numeric_string in wgs]

    # custom logic for special case of hillfort with id: 807
    if h_fort == 807:
        wgs.append(wgs[4])
        number = str(wgs[3])
        wgs[3] = int(number[:2])
        wgs[4] = float(number[-3:])

    # Decimal Degrees = Degrees + minutes/60 + seconds/3600
    latitude = wgs[0] + wgs[1]/60 + wgs[2]/3600
    longitude = wgs[3] + wgs[4]/60 + wgs[5]/3600

    data['Name'] = table.children()[0].text().splitlines()[0].replace('Pavadinimas:	', '')
    data['Region'] = table.children()[0].text().splitlines()[3].replace('Rajonas:	', '')
    data['latitude'] = latitude
    data['longitude'] = longitude
    hillforts.append(data)
    data = {}

data_frame = pandas.DataFrame(hillforts)

'''
if you are extracting data all in once.
'''
# data_frame.to_csv('new_hillforts.csv')

'''
if decision was made to extract data in parts
and using same csv file to append new data.
'''
with open('new_hillforts.csv', 'a') as f:
    data_frame.to_csv(f, header=False)
print('done')
