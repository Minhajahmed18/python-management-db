use python_db
go


select * from student1
select COUNT(*) from student1 
delete from student1 where std_id=100
select * from courses1
delete from courses1 where course_name='Accounting' and std_id=1
insert into courses1 values(1,'ABC',4000,4,2,2000)



ALTER TABLE courses1
ADD CONSTRAINT fk_name
    FOREIGN KEY (std_id)
    REFERENCES student1 (std_id)
    ON DELETE CASCADE;


select * from student1


select * from courses1


delete from student1 where std_id=7