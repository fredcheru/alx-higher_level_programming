-- mySQL script to display # of records with id=89
-- cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT COUNT(*) FROM first_table WHERE id = 89;
