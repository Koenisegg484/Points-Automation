# Points-Automation
This is a selenium script to automate earning Microsoft rewards points automatically without the need to do anything manually. The account's email and password is saved into a csv file. The program logs in with the account and earns the points.

Do not change any file name present in the repo.
Using this program you can run multiple microsoft ids at once to earn more rewards.
Donload this repository into your local system, then follow the below steps : 

1. The pwds002.csv file has three columns, one for email, second for password, third for Country.
2. Enter the email ids and their passwords in the respective columns, In the Country column, enter "france" or "usa" to use the vpn of that country, and if don't want to use vpn enter the name of your country
    I recommend not using vpns.
3. Make sure you have python installed in your computer.
4. Make sure you have the following libraries installed in your computer, if not run the following command
      pip install csv os threading plyer seleniium 
5. Once you have installed them completely, you are ready to go.
6. Go to the folder which has the downloaded files, open the folder in terminal, write the following code

    python ./PointsAutomate.py
    hit enter,
    
7. The program has now started, Enter 1 to run all the ids, or enter 2 to run specific ids.
8. The program may crash sometimes in case the internet speed gets slow or some ram issues, but don't mind it, once the program has completed, you can run the ids that crashed once again by choosing the "Run specific ids" option
9. Once the program has completed, it creates a "DailyReports.txt" file which includes which ids were signed in and did they successfully get completed or not.
10. That's all Thankyou.....
