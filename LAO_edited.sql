/* ---------------------------------------------------- */

/*  Generated by Enterprise Architect Version 13.5 		*/

/*  Created On : 02-Nov-2021 12:41:10 PM 				*/

/*  DBMS       : SQLite 								*/

/* ---------------------------------------------------- */



/* Drop Tables */



DROP TABLE IF EXISTS 'Building'

;



DROP TABLE IF EXISTS 'Landparcel'

;



DROP TABLE IF EXISTS 'Owner'

;



DROP TABLE IF EXISTS 'owns'

;



DROP TABLE IF EXISTS 'StreetLookUp'

;



DROP TABLE IF EXISTS 'Telephone'

;



/* Create Tables with Primary and Foreign Keys, Check and Unique Constraints */



CREATE TABLE 'Building'

(

	'UrbanDistrict' Integer NULL,

	'HouseNo' Text NULL,

	'SeqNo' Integer NULL,

	'Type' Text NULL,

	'ID' Integer NULL,

	'StreetCode' Integer NULL,

	CONSTRAINT 'FK_isLocatedOn_Landparcel' FOREIGN KEY ('ID') REFERENCES 'Landparcel' ('ID') ON DELETE No Action ON UPDATE No Action,

	CONSTRAINT 'FK_hasStreetCode_StreetLookUp' FOREIGN KEY ('StreetCode') REFERENCES 'StreetLookUp' ('StreetCode') ON DELETE No Action ON UPDATE No Action

)

;



CREATE TABLE 'Landparcel'

(

	'ID' Integer NOT NULL PRIMARY KEY,

	'assetSize' Real NULL

)

;



CREATE TABLE 'Owner'

(

	'PID' Integer NOT NULL PRIMARY KEY,

	'Title' Text NULL,

	'FirstName' Text NULL,

	'LastName' Text NULL,

	'City' Text NULL

)

;



CREATE TABLE 'owns'

(

	'share' NULL,

	'ID' Integer NOT NULL,

	'PID' Integer NOT NULL,

	CONSTRAINT 'PK_owns' PRIMARY KEY ('ID','PID'),

	CONSTRAINT 'FK_Landparcel_owns' FOREIGN KEY ('ID') REFERENCES 'Landparcel' ('ID') ON DELETE No Action ON UPDATE No Action,

	CONSTRAINT 'FK_Owner_owns' FOREIGN KEY ('PID') REFERENCES 'Owner' ('PID') ON DELETE No Action ON UPDATE No Action

)

;



CREATE TABLE 'StreetLookUp'

(

	'StreetCode' Integer NOT NULL PRIMARY KEY,

	'StreetName' Text NULL

)

;



CREATE TABLE 'Telephone'

(

	'Telephone' Integer NOT NULL PRIMARY KEY,

	'PID' Integer NULL,

	CONSTRAINT 'FK_Owner_Telephone' FOREIGN KEY ('PID') REFERENCES 'Owner' ('PID') ON DELETE No Action ON UPDATE No Action

)

;

SELECT AddGeometryColumn('Building', 'geometry', 25832, 'POLYGON');
SELECT AddGeometryColumn('Landparcel', 'geometry', 25832, 'POLYGON');
