import csv

def main():
        state = ''
        while state != '2':
            state = render_menu()

def render_menu():

    print('--- MUSIC DATABASE ---')
    print('Press 1- View most listened artists')
    print('Press 2- Exit')

    user_input = input()

    return handle_action(user_input)

def handle_action(user_input):

    match user_input:
        case '1':
            output_sorted_list()
            return '1'
        case '2':
            return '2'
        case _:
            print('Invalid input')

def output_sorted_list():
    db_size = 0
    with open('music_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        artist_list = {}

        for row in reader:
            db_size += 1
            if ' - ' in row['Track name'] and row['Track name'].count(' - ') == 1:
                artist, song = row['Track name'].split(' - ')

                if artist in artist_list:
                    artist_list[artist] += 1

                else:
                    artist_list[artist] = 1
   
    lst = artist_list.items()
    artist_list = sorted(lst, key = lambda x : x[1], reverse=True)

    for current_artist in artist_list:
        percentage = (current_artist[1] / db_size) * 100
        percentage = round(percentage,1)
        print(current_artist[0], f'{percentage}%')


main()
