# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

ENDPOINTS

GET /categories
•	Fetches a dictionary of all categories
•	Request parameters: None.
{
  "categories": {
    "1": "Science",       
    "2": "Art",
    "3": "Geography",     
    "4": "History",       
    "5": "Entertainment", 
    "6": "Sports"
  },
  "success": true
}
GET /questions?page=<page_number>
•	Fetches: a dictionary of paginated questions across all categories
•	Request arguments: page integer

example
{
  "all_questions": 19,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
  ],
  "success": true
}
DELETE /questions/:question_id/
•	Delete question using a question_id
•	Request arguments:int: question_id
 {
 "deleted": 2,
  "success": true,
  "total_books": 18
}
POST /questions
•	Creates a new question.
•	Request arguments: question (string, answer(string), difficulty(int), category(string).
{
  "success": true,
  "created": 1,
  "question": 1,
  "total_questions": 21,
}
POST /questions - 
•	Looks through all question and matches it to search term.
•	Request arguments: SearchTerm(string)
{
  "current_category": null,
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    }
  ],
  "success": true,
  "total_questions": 2
}
GET /categories/<int:category_id>/questions
•	Gets questions from a specific category
•	Request arguments: category_id(int)
{"current_category":3,
"questions":[{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,
"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"},{"answer":"Agra","category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is located in which Indian city?"}],
"success":true,"total_question":3}


POST /quizzes
•	Sends a post request to get next question
•	Request arguments: quiz_category(dict), previous_ids(list)
{
  "question": null,
  "success": true
}


## Testing


```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
