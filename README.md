# library
A library in python with MSQL database.

To get started, make sure you have python as well as MySQL server installed on your system.

First of all, Create a database named "library" and create 3 tables in it named, book, user, issuedBooks.

a) To create table 'book', use below SQL query-
CREATE TABLE `book` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `subject` varchar(30) NOT NULL,
  `code` varchar(30) NOT NULL,
  `count` int unsigned NOT NULL,
  PRIMARY KEY (`id`)
)

b) Create table user with following SQL query-
 CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `identityNumber` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
)

c) Similarly create the table 'issuedBooks' using below query-
CREATE TABLE `issuedbooks` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userID` varchar(30) NOT NULL,
  `issueDate` date DEFAULT NULL,
  `submitDate` date DEFAULT NULL,
  `bookCode` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`userID`)
)

Now our database is setup. Congratulations.

Let's do the final step and run main.py file in a python virtual environment and enjoy using this awesome and simple library.
