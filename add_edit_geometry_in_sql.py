class AddGeometry:
    def __init__(self, epsg_num, input_filename, output_filename):
        self.epsg_num = epsg_num
        self.sql_text = self.__open_text_file(input_filename)
        self.edited_sql_list = list()
        self.table_name = list()
        self.__edit_sql_file()
        self.__add_geometry_to_edited_sql_file()
        self.__write_new_sql_file(output_filename)

    @classmethod
    def __open_text_file(cls, input_file):
        """
        Read sql docs which are generated in Enterprise Architect
        :param input_file: text file of sql queries
        :return: a list which each value is equal to each line of text file
        """
        with open(input_file) as f:
            return f.readlines()

    def __edit_sql_file(self):
        """
        restoring edited queries in self.edited_sql_list
        1- delete lines containing Geometry word.
        2- get the name of each table. these are the input of AddGeometryColumn query
        3- delete ',' of the end of each table query
        update self.edited_sql_list and self.table_name
        """
        for line in self.sql_text:
            if 'Geometry' in line:
                continue
            elif 'CREATE TABLE' in line:
                self.table_name.append(line.split(' ')[-1][1:-2])
                self.edited_sql_list.append(line)
            elif ')\n' in line:
                if self.edited_sql_list[-1][-2] == ',':
                    self.edited_sql_list[-1] = self.edited_sql_list[-1].replace(',', '')
                    self.edited_sql_list.append(line)
                else:
                    self.edited_sql_list.append(line)
            else:
                self.edited_sql_list.append(line)

    def __add_geometry_to_edited_sql_file(self):
        """
        add AddGeometryColumn query to self.edited_sql_list
        """
        geometry_dic = {1: "'POINT'", 2: "'LINESTRING'", 3: "'POLYGON'",
                        4: "'MULTIPOINT'", 5: "'MULTILINESTRING'", 6: "'MULTIPOLYGON'"}
        geometry_type_text_show = '==> Point: 1\tPolyline: 2\t Polygon: 3 :\tMULTIPOINT: 4\t' \
                                  'MULTIPOLYLINE: 5\t MULTIPOLYGON: 6 :\t'
        geometry_type = [(f"'{item}'", geometry_dic[int(input(f'{item} {geometry_type_text_show}'))])
                         for item in self.table_name]
        for item in geometry_type:
            self.edited_sql_list.append(f"SELECT AddGeometryColumn({item[0]}, 'geometry', {self.epsg_num}, {item[1]});")

    def __write_new_sql_file(self, output_filename):
        """
        rewrite edited queries in new sql file
        :param output_filename:
        """
        with open(output_filename, 'w') as f:
            for line in self.edited_sql_list:
                f.write(f'{line}\n')
