# P2P chat and file sharing client

The project involved builsing a peer to peer architecture which could communicate with each other in a chat room and request for files. We made use of multiple technologies such as the bittorrent protocol which takes care of the finding peers, discovery of local files, periodic refreshing etc. We made use of tkinter for the GUI. The project consists of two major parts, the chat room, and the file sharing client.
In the chat room, we make use of tcp so that the messages are never lost since that is sensitive data. There is realtime updation of error/confirmation messages which are displayed on the GUI screen. Multiple clients can connect and make use of the chat room and they all can connect and share files. Each client acts like he is the server and is connected to other clients based on their ip address and port number.
The p2p file sharing client is activated once we click the start button. This opens a new tkinter window which prompts you to enter your ip address and port number separated by a colon. When you hit enter, the file sharing window is now opened.
This new window consists of multiple modules, like adding a peer to the peer list, adding your local files which you would like to share and refreshing for peer disccovery in your network, and searching for files available for transfer, and also downloading files from the list of available files.

There are certain precautions that need to be taken for the file sharing to work,
- the port number used for file sharing shouldn't be the same as the one set in the chat room
- the files when being fetched in the file sharing client need to be clicked on and selected properly.
- to make sure it doesnt hang, kindly avoid using port 7894 for the chat room and use only port number 7894 in the file sharing client.


![MainUI](/UI1.PNG)

This is the main screen that will enable users to chat with each other.

![Start](/gui2.png)

This will enable users to connect on a fixed port to enable file transfer.

![Transferfiles](/guifiletransfer.png)

The files can be uploaded and fetched by the other users who are connected
