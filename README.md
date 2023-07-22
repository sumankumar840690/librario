# Librario

The Python Flask Librario is a web application designed to streamline the operations of a library. This feature-rich Flask app offers an intuitive user interface for managing books, book copies, and borrower records efficiently. It includes functionalities for both general users and administrators, providing an enhanced user experience and seamless administration.

## Key Features:

### Book Management:

- Adding new books to the library with essential details such as title, author, ISBN, genre, and publication year.
- Removing books that are no longer part of the library's collection.
- Creating copies of books with unique identification numbers to keep track of individual copies.

### Borrowing and Returning Books:

- Allowing library members to borrow book copies for a specific duration.
- Managing due dates and generating reminders for overdue books.
- Facilitating the return process, updating book availability status accordingly.

### User Roles:

- The application offers two distinct user roles: general users and admin users.
- General users can search for books, view availability, and borrow/return books.
- Admin users have access to an exclusive admin tab and dashboard for advanced management capabilities.

### Admin Dashboard:

- The admin dashboard provides an overview of library statistics, including the total number of books, available copies, borrowed copies, etc.
- Admin users can add or remove books from the collection, manage borrower records, and track book copies' status.

### User Authentication:

- Secure user authentication and authorization mechanisms to ensure data privacy and prevent unauthorized access.
- Admin users need specific credentials to access the admin dashboard.

### User-friendly Interface:

- A well-designed, responsive, and intuitive user interface for easy navigation and a pleasant user experience.

### Database Management:

- The application uses a robust database to store book records, user data, and transaction details.
- Efficient database management ensures data integrity and optimal system performance.


## Start

- Clone the repository.

```sh
$ git clone https://github.com/sumankumar840690/librario
$ cd librario
```

- Create Virtual Environment.

    In Linux Systems:
    ```sh
    $ virtualenv venv
    $ source venv/bin/activate
    ```

    In Windows:
    ```sh
    $ virtualenv venv
    $ ./venv/Scripts/Activate.ps1
    ```

- Install dependencies.

```sh
$ pip install -r requirements.txt
```

- Run the application.

```bash
$ python wsgi.py
```
