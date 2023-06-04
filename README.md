# PythonWithPostgresCourse

This folder contains the source code and activities from Jose Salvatierra's course on Udemy.

## Programming Journal with Python and SQLite

The project is a programming journal that uses SQLite as a database. In this journal it is possible to add new entries or view existing entries to keep track of our programming learning. When users first use our app, they are going to see a prompt like the one below. A quick welcome at the top and three options that they have in the menu. One to add new entries, two to view entries or three to exit, and their selection at the bottom. 

```
Welcome to the programming diary!

Please select one of the following options:
1) Add new entry for today;
2) View entries;
3) Exit.

Your selection: 
```

### Adding new entries

* User presses 1;
* We ask them for date and contents for the entry;
* It is used two separate prompts.

```
What have you learned today?

Enter the date:
```

### Viewing entries

* User presses 2;
* For each entry, we show the date and content.

```
01-01-2023
Today I learned how to use Python and SQLite

02-01-2023
Continued with Python and SQLite, including filtering results and updating values.
```

## Movie Watchlist App

### Project Features

* Keep track of movies the user is interested in, and their release dates;
* Store which movies the user has already watched;
* Add new users to keep track of their watched movies separetly.

### User Interface

```sql
Welcome to the watchlist app!

Please select one of the following options:
1) Add new movie;
2) View upcoming movies;
3) View all movies;
4) Add watched movie;
5) View watched movies;
6) Add user to the app;
7) Exit.

Your selection:
```

