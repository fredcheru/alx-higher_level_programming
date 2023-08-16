-- MySQL script to calculate average of score
-- cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT AVG(score) as `average` FROM second_table;
