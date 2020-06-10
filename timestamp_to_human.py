from datetime import datetime

if __name__ == '__main__':
    timestamp = input('Type the unix timestamp:\n')
    human_date = datetime.fromtimestamp(int(timestamp))

    print(human_date)
