-- Create a table for storing books in your booklist. The table should be able to contain
-- the book's title, the author, and the date of publication as a string.

CREATE TABLE books (title TEXT, author TEXT, publication_DATE TEXT);

-- Create a table for storing information about a person that writes book reviews. For each
-- person, store their name, their location as a string, and how many book reviews they have
-- written.

CREATE TABLE book_reviewers (name TEXT, location TEXT, review_count INTEGER);

-- Create a table for storing temperature readings for a thermometer inside a greenhouse.
-- Each reading should contain the temperature as well as the date and time of the reading
-- as a string.

CREATE TABLE temperature_readings (temperature REAL, date_time TEXT);
