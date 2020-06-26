use python_db
go

select * from courses1

select * from student1

insert into courses1 values(4,'ABC',4000,4,7,3000)

insert into courses1 values(4,'ABC',4000,4,2,3000)

insert into courses1 values(4,'ABC',4000,4,12,3000)

select course_name from courses1
inner join student1
on courses1.std_id=student1.std_id