# create table
use alooma;
# DROP TABLE engagements;
CREATE TABLE if not exists engagements (
  id int(11),
  portalI int(11) DEFAULT NULL,
  createdAt bigint(20) DEFAULT NULL,
  lastUpdated bigint(20) DEFAULT NULL,
  `type` text,
  primary key(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
;
# Load Data to cloud mart
LOAD DATA LOCAL INFILE 'C:\\Users\\jparsons\\PycharmProjects\\jwp-alooma\\engagements.csv' INTO TABLE engagements
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

# create view for queries and convert unix ts to dates
use alooma;
# DROP VIEW vw_engagement;
CREATE VIEW vw_engagement AS 
select 
id 
,date(from_unixtime(createdAt / 1000)) as createdAt
,date(from_unixtime(lastUpdated / 1000)) as lastUpdated
,type
,'1' as ecount
from engagements;

# Write a SQL Query that pulls the Engagements per Day broken down by type.  You should expose both the counts per day and a rolling 2 week avg for each day
select 
createdAt
,type 
,sum(ecount) as ecount
from vw_engagement
group by createdAt, type
;

select
a.createdAt
,a.type
,sum(a.ecount) as cnt
,round((select sum(b.ecount) / b.ecount
           from vw_engagement as b
           where datediff(a.createdAt, b.createdAt) between 0 and 13
         ),2) as '14dayMovingAvg'
from vw_engagement as a
group by a.createdAt, a.type
order by a.createdAt
;