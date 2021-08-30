# mcq-application
This is an online assessment platform i.e. web application made using ```Python-Flask``` microframework along with ```MySQL```(SQLITE3) database in backend and in frontend ```Jinja``` templating along with ```Html,css``` and a bit of ```javascript``` is used.

This application is created by me(Satyam Mourya) and Amiy tiwari as a Project of Walkover University Program
https://drive.google.com/file/d/15cQjLJeqQ_zQJQt4W3NZcA9CUB8c5dsO/view?usp=drivesdk


# Required functionality

1.Assessment shall be MCQ pattern.:heavy_check_mark:

2.There must be a question pool for the assessment:heavy_check_mark:```we have created question pool of 10 questions in database and select randomly 5 sample in shuffled manner```

3.The questions displayed in the assessment shall be only from that pool:heavy_check_mark:```We have queried question only from that question pool(database).```

4.Number of questions in the pool shall be more than questions displayed:heavy_check_mark:```we have pool of 10 questions and 5 asked```

5.Set a time limit for the assessment (individual timer for a question/optional):heavy_check_mark:```Individual timer for each question.```

6.Question order shall be shuffled for each candidate appearing:heavy_check_mark:```Questions appering in test are random sample decided once user log in so its different and shuffled for each user```

7.Assessment score shall be generated at the time of submission:heavy_check_mark:```Score of candidate is showed at the result page and saved in database with name,email,marks and time```


# Functionality (Extra)

1.```Login page``` - To take user's data.

2.```user table``` - To store the data and scores of the user and the time of test submission.


# Getting Started ```project setup```

Clone the source code in your local machine and install the requirements by running

```bash
pip install -r requirements.txt 
```

Finally, run the application using
```bash
python main.py
```
on your python interpreter

If everything executed well and in order then server with port 5000 must be given in terminal copy and paste in browser. Our site must be loaded on local server```.
