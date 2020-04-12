import csv
import math

rows = {}

with open('avocado_state.csv', 'r') as rfile:
    reader = csv.reader(rfile)
    for row in reader:
        if rows.get(row[-1]) :
            rows[row[-1]].append(row)
        else:
            # rows["New York"] = []
            rows[row[-1]] = []

            # rows["New York"].append(row)
            rows[row[-1]].append(row)

    agg_rows = []
    # [Average Price,Counter, 4046,4225,4770, Small Bags,Large Bags,XLarge Bags, State]
    for key, value in rows.items():
        counter = 0
        d = [0,0, 0,0,0, 0,0,0, key]
        for row in value:
            d[0] += float(row[2])
            
            counter += 1

            d[2] += float(row[4])
            d[3] += float(row[5])
            d[4] += float(row[6])

            d[5] += float(row[8])
            d[6] += float(row[9])
            d[7] += float(row[10])
            # print(row[2], row[4],row[5],row[6], row[8],row[9],row[10], row[-1])
        d[0] = math.ceil(d[0] / counter)
        d[1] = counter

        d[2] = math.floor(d[2])
        d[3] = math.floor(d[3])
        d[4] = math.floor(d[4])

        d[5] = math.floor(d[5])
        d[6] = math.floor(d[6])
        d[7] = math.floor(d[7])
        agg_rows.append(d)

        # print("{{'name':'{}', 'sum':{}}},".format(d[8], d[2]+d[3]+d[4]))


# # bags
# for row in agg_rows:
#     total = row[5] + row[6] + row[7]
#     to_add = 100 - (math.floor(row[5]/total * 100) + math.floor(row[6]/total * 100))
#     print("'{}':[{{'label':'{}', 'value':{}}},".format(row[-1], 'Small Bags', math.floor(row[5]/total * 100)))
#     print("{{'label':'{}', 'value':{}}},".format('Large Bags', math.floor(row[6]/total * 100)))
#     print("{{'label':'{}', 'value':{}}}],".format('XLarge Bags', to_add))

# PLUs
for row in agg_rows:
    total = row[2] + row[3] + row[4]
    to_add = 100 - (math.floor(row[2]/total * 100) + math.floor(row[3]/total * 100))
    print("'{}':[{{'label':'{}', 'value':{}}},".format(row[-1], '4046', math.floor(row[2]/total * 100)))
    print("{{'label':'{}', 'value':{}}},".format('4225', math.floor(row[3]/total * 100)))
    print("{{'label':'{}', 'value':{}}}],".format('4770', to_add))

# open('avocado_state.csv', 'w', newline='') as wfile:
#     reader = csv.reader(rfile)
#     writer = csv.writer(wfile)

#     for row in reader:
#         state = city_to_state_dict.get(' '.join(re.findall('[A-Z][^A-Z]*', row[-1])))
#         if (state):
#             row.append(state)
#             writer.writerow(row)