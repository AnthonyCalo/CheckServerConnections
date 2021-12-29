# CheckServerConnections
<h1>Overview</h1>
This is a gui created with tkinter for managing a program that checks connections to a list of servers or workstations.
Input a list of servers you would like to keep track of. The gui will insert them into a sqllite database for persistent storage
Run the Gui.py file and it will bring you to the first page(image below). 
</br>
</br>
After this click on the second page to add a file location(bottom image). Write any file location. By default the file will appear in same folder as 
the program.
<br/>
<br/>
At this point press Run Scan and the application will scan the list of servers and write the results to the file locations listed.
Example of the format below and in history.txt/ newlogs file in repo.
</br>
![scanres](https://user-images.githubusercontent.com/63485111/147626883-63a4a258-bfd6-41ce-9437-2fd38335fa0b.PNG)

<br/>
<br/>
<h2>Optional Gmail configuration</h2>
There is an optional feature that if a during a scan a high priority server is down the program will automatically email you with a message containing details.
<p>In the Gmail.py on lines 12 & 13 enter gmail user and password. For this to work you will need to change a setting in gmail that allows less secure apps</p>
<p>This is completely optional and the application works fully without the additional email configuration</p>
</br>
<h2>Additional use information</h2>
Once you configure the output locations and server list with the gui. You can schedule cronjob for python to run CheckServer.py.
The scans will be automated to run at custom time. If you configure email update you won't even need to check logs because you'll get emailed if a server is down




<br/>
<br/>
<br/>




![server_conn_gui1](https://user-images.githubusercontent.com/63485111/147626095-28c3de3d-e20f-40cd-850d-b6629d9a2ce6.PNG)


![server_conn_gui2](https://user-images.githubusercontent.com/63485111/147626132-db17ac2c-37d7-4719-b7d4-981052a5e52b.PNG)
