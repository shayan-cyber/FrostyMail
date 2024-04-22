
# FrostyMail

The project aims to automate the process of sending cold emails to recruiters listed in a Google Sheet and updating the status of each email on the same sheet. The script will run automatically every day at 8 PM, eliminating the need for manual intervention. 

Key features of the project include:

1. **Google Sheet Integration**: The script interacts with a Google Sheet containing a list of recruiters' email addresses and other relevant information.

2. **Cold Email Sending**: Using the data from the Google Sheet, the script sends personalized cold emails to recruiters.

3. **Status Update**: After sending each email, the script updates the status of the email (e.g., "Sent", "Pending", "Follow-up Required") on the Google Sheet.

4. **Automation**: The script is scheduled to run automatically at a specified time (8 PM every day), ensuring that cold emails are sent consistently without manual effort.

5. **Ease of Use**: Users only need to add the email content and recipient details to the Google Sheet, and the script takes care of the rest.

Overall, the project streamlines the process of reaching out to recruiters via cold emails, improves efficiency, and reduces manual workload.


## Set-Up

Clone the repo

```bash
 git clone https://github.com/shayan-cyber/FrostyMail.git
```
Navigate
```bash
  cd FrostyMail
```
Install
```bash
  pip install -r requirements.txt
```


#### 1. go to main.py file

#### 2. Add your email credentials

#### 3. change the key.json file with google credentials (https://www.youtube.com/watch?v=1QFLfvvjmkQ)

#### 4. Add the google console service account to the sheet from which you are gonna take the emails (the should have column names as Mail ID, Status, Company Name as shown below) (https://www.youtube.com/watch?v=7qU_f__95Qc)

#### 5. Change Sheet Name in the main.py file

#### 6. Change the email template according to your need
#### 7. Push the Code to your own repository and Have fun



![Image](https://i.imgur.com/2nMyg7g.png)


## Authors

- [@shayan-cyber](https://github.com/shayan-cyber)
- [debroyshayan@gmail.com]()

