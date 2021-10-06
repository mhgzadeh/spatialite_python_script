# with open('sample.txt') as f:
#     file_text = f.readlines()

# table_name = list()
# edited_list = list()
# for line in file_text:
#     if 'Geometry' in line:
#         continue
#     elif 'CREATE TABLE' in line:
#         table_name.append(line.split(' ')[-1][1:-2])
#         edited_list.append(line)
#     elif ')\n' in line:
#         print(edited_list[-1])
#         if edited_list[-1][-2] == ',':
#             edited_list[-1] = edited_list[-1].replace(',', '')
#             edited_list.append(line)
#         else:
#             edited_list.append(line)
#     else:
#         edited_list.append(line)

# geometry_dic = {1: "'POINT'", 2: "'POLYLINE'", 3: "'POLYGON'"}
#
# geometry_type = [(f"'{item}'", geometry_dic[int(input(f'{item} ==> Point: 1\tPolyline: 2\t Polygon: 3 :\t'))])
#                  for item in table_name]
#
# for item in geometry_type:
#     edited_list.append(f"SELECT AddGeometryColumn({item[0]}, 'geometry', 4326, {item[1]});")
#
# with open('spatialite2.sql', 'w') as f:
#     for line in edited_list:
#         f.write(f'{line}\n')

if __name__ == '__main__':
    for line_num, line in enumerate(edited_list):
        print(f"{line_num}:\t {line}\n len of line: {len(line)}\n")
    print(table_name)
    print(geometry_type)
    print(file_text)
