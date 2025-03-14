import requests

url = 'https://adventofcode.com/2024/day/1/input'

def CalculateSimilarity(array1, array2) :
    maxTimes = 0
    for item1 in array1:
        maxTimes += (item1 * array2.count(item1))
    
    print('max Similarity is ', maxTimes)
    return maxTimes


def CalculateNumberDifference(array1, array2) :
    array1 = sorted(array1)
    array2 = sorted(array2)

    maxDiff = 0
    for item1, item2 in zip(array1, array2):
        #print(item1, item2, ' diff is ', abs(item1 - item2))
        maxDiff += abs(item1 - item2)

    print('max Diff is ', maxDiff)
    return maxDiff



def ConnectInputUrl(url): 
    # Set the Referer header and the required policy
    headers = {
        'Referer': 'https://adventofcode.com/2024/day/1',  # Origin URL
        'Origin': 'https://adventofcode.com',  # Origin header (important for CORS)
    }

    cookies = {
        'session': '53616c7465645f5f39198981a8aaf368913c7434881b44c98ba7562dc56ae7a13471583fdfeeb7ed22083a7528befe5e48011ce33f89ec8ae30181d58399dfc6'  # my hardcoded session
    }

    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        content = response.text
        lines = content.splitlines()
        
        column1 = []
        column2 = []

        for line in lines:
            values = line.split()
            if len(values) >= 2:
                column1.append(int(values[0]))
                column2.append(int(values[1]))

        CalculateNumberDifference(column1, column2)
        CalculateSimilarity(column1, column2)

    else:
        print ('reading URL ERROR.')


if __name__ == '__main__':
    # Column1 = [3, 4, 2, 1, 3, 3]
    # Column2 = [4, 3, 5, 3, 9, 3]

    ConnectInputUrl(url)

