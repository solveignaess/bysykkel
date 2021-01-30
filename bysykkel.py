import requests
import pandas

# user input caller ID
caller_id = str(input('Insert Client Identifier (e.g. company-application): '))
my_headers = {'Client-Identifier' : caller_id}

try:
    # get station information and status
    information = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json',
                               headers=my_headers)
    information.raise_for_status()

    status = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json',
                          headers=my_headers)
    status.raise_for_status()

    # make station information and status lists
    information_list = information.json()['data']['stations']
    status_list = status.json()['data']['stations']

    # make lookup dictionary {caller ID: station name}
    dict = {}
    for elem in information_list:
        id = elem['station_id']
        dict[id] = elem['name']

    # make dictionary to show {station name: [num bikes, num locks]}
    dict_to_show = {}
    for elem in status_list:
        jd = elem['station_id']
        if jd in dict.keys():
            dict_to_show[dict[jd]] = [elem['num_bikes_available'], elem['num_docks_available']]

    # sort dict alphabetically
    dict_to_show = {key:dict_to_show[key] for key in sorted(dict_to_show)}

    # get current maximum number of rows displayed with pandas DataFrame
    max_rows = pandas.get_option('display.max_rows')
    # set correct number of rows
    num_rows_table = len(status_list) +  1
    pandas.set_option('display.max_rows', num_rows_table)

    # display data
    table = pandas.DataFrame.from_dict(dict_to_show,
                                       orient='index',
                                       columns=['# bikes', '# docks'])
    print(table)

    # reset maximum number of rows
    pandas.set_option('display.max_rows', max_rows)

# check for errors
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
