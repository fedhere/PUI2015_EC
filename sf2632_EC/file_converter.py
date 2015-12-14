__author__ = 'Shi Fan'
import csv

txt_file = r"nbhds.txt"
csv_file = r"nbhds.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)