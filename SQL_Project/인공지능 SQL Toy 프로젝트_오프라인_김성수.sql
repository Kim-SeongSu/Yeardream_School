# 5월 2일 [Year-Dream SQL PJT] 오프라인_김성수

USE University;

#a.  Computer Science 학부 과목을 한 과목이라도 수강하고 있는 모든 학생의 ID와 이름을 출력하세요.  
-- (단, 중복을 제거하여 출력해주세요)
SELECT student.ID, student.name
FROM student
INNER JOIN takes
ON student.ID = takes.ID
WHERE (takes.course_id)

IN (SELECT takes.course_id
    FROM takes 
    INNER JOIN course
    ON takes.course_id = course.course_id
    INNER JOIN section
    ON takes.course_id = section.course_id
    WHERE course.dept_name = 'Comp. Sci.' AND section.year = '2010');

/* 
2010년도에 Comp. Sci.의 학부과목을 수강하고 있는은 학생은 없다. 하지만 2007년 기준으로는 있다.
*/
SELECT student.ID, student.name
FROM student
INNER JOIN takes
ON student.ID = takes.ID
WHERE (takes.course_id)

IN (SELECT takes.course_id
    FROM takes 
    INNER JOIN course
    ON takes.course_id = course.course_id
    INNER JOIN section
    ON takes.course_id = section.course_id
    WHERE course.dept_name = 'Comp. Sci.' AND section.year = '2007');


#b.  “CS-001”를 id로 가지고, “Weekly Seminar”가 title인 1학점짜리 과목을 새로 신설해보세요.
INSERT INTO course (course_id, title, dept_name ,credits)
VALUES ('cs-001', 'Weekly Seminar','Comp. Sci.', 1);

SELECT *
FROM course;


#c.  Computer Science 학부생 전원을 sec_id가 1인 2007년도 가을학기 세션에 등록시켜주세요. 
-- (HINT. University ERD도 참고해보세요)
insert into takes(ID,course_id, sec_id, semester, year, grade)
Values((SELECT ID
        FROM student
		WHERE dept_name = 'Comp. Sci.'),
       (select course_id
        from section
		where sec_id = '1' and semester = 'Fall' and year = '2007'),
		1,'Fall',2007,null);


#d.  각 학부별로 가장 많은 연봉을 가진 instructor중에서 가장 연봉이 낮은 instructor의 name과 dept_name을 찾아주세요.
select name, dept_name
from instructor
where (dept_name, salary)
in (select dept_name, max(salary)
    from instructor
    group by dept_name)
order by salary
limit 1;


#e.  2008년도 가을학기에 수업을 진행하는 모든 instructor를 찾아주세요.
SELECT instructor.name
FROM instructor
INNER JOIN teaches
ON instructor.ID = teaches.ID
WHERE teaches.year= 2008 and teaches.semester = 'Fall';


#f.  2007년도 기준 물리학부에 재학중인 모든 학생을 찾아주세요.
SELECT distinct name
FROM student
INNER JOIN takes
ON student.ID = takes.ID
WHERE takes.year= 2007 and student.dept_name = 'Physics';


#g.  컴퓨터공학 강사 Lee가 담당하고 있는 학생들 중 다른 학부 학생을 모두 찾아주세요.
SELECT student.name
FROM student
where student.name
IN (SELECT student.name
    FROM advisor 
    INNER JOIN instructor
    ON advisor.i_ID = instructor.ID
    INNER JOIN student
    ON advisor.s_ID = student.ID
    WHERE instructor.name= 'Lee') and student.dept_name != 'Comp. Sci';


#h.  이 때까지 한번도 과목을 수강한 적이 없는 모든 학생의 ID와 name을 출력해주세요.
select ID, name
from student
where tot_cred < 3;