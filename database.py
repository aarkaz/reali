import requests
import csv

listing_table = {}
temp_file_name = 'temp_csv.csv'

def initialize():
    download = requests.get("https://server-assignment.s3.amazonaws.com/listing-details.csv")

    with open(temp_file_name, 'w') as temp_file:
        temp_file.writelines(download.text)

    with open(temp_file_name, 'rU') as temp_file:
        csv_reader = csv.DictReader(temp_file)
        for line in csv_reader:
            listing_table[line['id']] = line

def query(min_price=None,max_price=None,min_bed=None,max_bed=None,min_bath=None,max_bath=None):
    result_set = []
    for id in listing_table:
        record = listing_table[id]
        if min_price and int(record["price"]) < int(min_price):
            continue
        if max_price and int(record["price"]) > int(max_price):
            continue
        if min_bed and int(record["bedrooms"]) < int(min_bed):
            continue
        if max_bed and int(record["bedrooms"]) > int(max_bed):
            continue
        if min_bath and int(record["bathrooms"]) < int(min_bath):
            continue
        if max_bath and int(record["bathrooms"]) > int(max_bath):
            continue
        result_set.append(record)
    return result_set