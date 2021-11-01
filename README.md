### Django multi database connection
This project is made to build a multi tenancy django application.

We make use of middleware. A middleware is built such that the database connection is intercepted and database connection is created for the request based on the request header.
There is only one simple table called alpha_userdata where user name will be stored and retrived

Curl for GET Request

    curl --location --request GET 'http://localhost:8000/user' --header 'database: uae'

Curl for POST Request

    curl --location --request POST 'http://localhost:8000/user' --header 'database: uae' --header 'Content-Type: application/json' -- data-raw '{
    "name": "UAE Use through postman" }'
