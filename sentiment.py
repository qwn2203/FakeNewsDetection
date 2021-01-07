# Import
import paralleldots
import csv
# Setting your API key
paralleldots.set_api_key("API KEY")
# Viewing your API key
paralleldots.get_api_key()

with open('Training Document', mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\nID: {row["ID"]} \n\t with text: {row["Text"]} \n')

        lines = {row["Text"]} 
        print('\nThe emotion analysis results for' +'\033[1m'+ ' ID: ' +  f'{row["ID"]}' +'\033[0m' + ' in the file:') 
        print("---------------------------------------------------------\n") 
        response=paralleldots.emotion(lines)
        print(response)

    line_count += 1
    #print(f'Processed {line_count} lines.')