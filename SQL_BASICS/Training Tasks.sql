use [22TD0651];

-- task-1
Create table Students (Name Varchar(20), CS Integer, Maths Integer, English Integer);
Insert into Students values ('Sam', 100, 95, 91), ('Ram', 95, 100, 90), ('Tom', 55, 70, 75); 
select * from Students;

-- task-2
select * from Students where CS >90 order by Name ASC;
delete from Students where Name = ('Sam' );
delete from Students where Name = ('Ram' );
delete from Students where Name = ('Tom' );

-- task-3
Insert into Students values ('Anu',92,85,88),('Ravi',88,92,90),('Priya',90,88,92),('Arun',85,90,88),('Neha',92,88,90),('Hari',88,90,92),('Sita',90,92,88),('Mohan',88,90,92),('Tina',92,88,90),('Asha',90,92,88),('Raj',88,90,92),('Meena',92,88,90),('Jai',90,92,88),('Lata',88,90,92),('Sunil',92,88,90),('Mala',90,92,88),('Kiran',88,90,92),('Nisha',92,88,90),('Anand',90,92,88);

-- task-4
alter table Students add Department Varchar(20);
delete from Students;
INSERT INTO Students (Name, CS, Maths, English, Department) VALUES ('Anu', 92, 85, 88, 'MECH'),('Ravi', 88, 92, 90, 'ECE'),('Priya', 90, 88, 92, 'BME'),('Arun', 85, 90, 88, 'EEE'),('Neha', 92, 88, 90, 'CSE'),('Hari', 88, 90, 92, 'MECH'),('Sita', 90, 92, 88, 'ECE'),('Mohan', 88, 90, 92, 'BME'),('Tina', 92, 88, 90, 'EEE'),('Asha', 90, 92, 88, 'CSE'),('Raj', 88, 90, 92, 'MECH'),('Meena', 92, 88, 90, 'ECE'),('Jai', 90, 92, 88, 'BME'),('Lata', 88, 90, 92, 'EEE'),('Sunil', 92, 88, 90, 'CSE'),('Mala', 90, 92, 88, 'MECH'),('Kiran', 88, 90, 92, 'ECE'),('Nisha', 92, 88, 90, 'BME'),('Anand', 90, 92, 88, 'EEE'),('Sam', 100, 95, 91, 'BME'),('Ram', 95, 100, 90, 'CSE'),('Tom', 55, 70, 75, 'ECE');

-- task-5
SELECT MAX(CS) AS 'Highest CS', MAX(Maths) AS 'Highest Maths', MAX(English) AS 'Highest English' FROM Students;
SELECT MIN(CS) AS 'Lowest CS', MIN(Maths) AS 'Lowest Maths', MIN(English) AS 'Lowest English' FROM Students;
SELECT Department, COUNT(*) AS 'Number of Students' FROM Students GROUP BY Department;

