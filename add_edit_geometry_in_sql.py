class AddGeometry:
    def __init__(self, epsg_num, input_filename, output_filename):
        self.epsg_num = int(epsg_num)
        self.sql_text = self.__open_text_file(input_filename)
        self.edited_sql_list = list()
        self.table_name = list()
        self.table_name_type = list()
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
        2- get the name of each table and type of features (point, line, ...).
            these are the input of AddGeometryColumn query
        3- delete ',' of the end of each table query
        update self.edited_sql_list and self.table_name
        """
        for line in self.sql_text:
            if 'CREATE TABLE' in line:
                self.table_name.append(line.split(' ')[-1][1:-2])
                self.edited_sql_list.append(line)
            elif 'Geometry' in line:
                self.table_name_type.append(line.split(' ')[1].lower())
                continue
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
        geometry_dic = {'point': "'POINT'", 'line': "'LINESTRING'", 'polyline': "'LINESTRING'",
                        'linestring': "'LINESTRING'", 'polygon': "'POLYGON'",
                        'multipoint': "'MULTIPOINT'", 'multiline': "'LINESTRING'", 'multipolyline': "'LINESTRING'",
                        'multilinestring': "'MULTILINESTRING'", 'multipolygon': "'MULTIPOLYGON'"}

        # geometry_type = [(f"'{self.table_name[i]}'", self.table_name_type[i]) for i in range(len(self.table_name))]
        for i in range(len(self.table_name)):
            self.edited_sql_list.append(
                f"SELECT AddGeometryColumn({self.table_name[i]}, 'geometry', {self.epsg_num}, {geometry_dic[self.table_name_type[i]]});"
            )

    def __write_new_sql_file(self, output_filename):
        """
        rewrite edited queries in new sql file
        :param output_filename:
        """
        with open(output_filename, 'w') as f:
            for line in self.edited_sql_list:
                f.write(f'{line}\n')
