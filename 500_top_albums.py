import csv
import requests
import time

api_key = 'xbU9tfRFmPsXV41cb72rsvFhJc8BFfZ3nHGJDv5J00dKzEGZtAZa7S8Jtv0jrHLw'

with open('./500-Greatest-Albums-master/500-Greatest-Albums-master/albumlist.csv', newline='') as csvFile:
    total_calls = 0
    total_found = 0
    songs = csv.reader(csvFile, delimiter=',')
    t0 = time.time()
    for row in songs:
        print(f'{row[2]}, {row[3]}')
        try:
            url = f'https://orion.apiseeds.com/api/music/lyric/{row[3]}/{row[2]}?apikey={api_key}'
            result = requests.get(url).json()
            total_calls += 1
            t1 = time.time()
            time_passed = t1 - t0
            # Limit on how many times I could call the API a minute so
            # had to add this
            if time_passed < 60 and total_calls >= 100:
                time.sleep(60)
                t0 = time.time()
                total_calls = 0
            if 'error' in result:
                continue
            else:
                total_found += 1
                print(result['result']['track']['text'])
        except:
            print(f'Exception happened for {row[2]}, {row[3]}')
    print(total_found)