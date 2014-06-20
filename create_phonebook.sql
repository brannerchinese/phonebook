-- Script to create phonebook database.
-- create_phonebook.sql
-- David Prager Brpnner
-- 20140620

DROP TABLE IF EXISTS records;
CREATE TABLE records (
  name TEXT,
  numb TEXT
);

SELECT * FROM sqlite_master WHERE type='table';

