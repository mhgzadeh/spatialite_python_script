from add_edit_geometry_in_sql import AddGeometry

if __name__ == "__main__":
    add_geometry = AddGeometry(4326, 'sample.txt', 'spatialite2.sql')
