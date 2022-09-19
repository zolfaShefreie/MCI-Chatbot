# Task-004
task title: Implemente a simple Telegram bot that get a text from user and return same text as result

## Work Step:
1. make new bot using BotFather 
"/newbot" command is used for create new bot. then the name and Id of bot must be specified to complete the process of creation. When the bot is successfully created, a token is provided for bot owner to control the bot.
<img width="249" alt="Screenshot 2022-09-19 101415" src="https://user-images.githubusercontent.com/44172962/191019044-17bb890b-6fd3-4198-8cc0-8f22294294cc.png">

<img width="482" alt="Screenshot 2022-09-19 101751" src="https://user-images.githubusercontent.com/44172962/191019891-de17abe8-eb60-4576-96ab-551b8966ca6c.png">

2. some code for control bot using pyTelegramBotAPI
for controling the bot some functions have been implemented that each of them work as handler. user send message and besaed on some messages bot show specific reaction. in this code "/start" and "/help" commands used for showing the other commands. "/start_echo" and "/stop_echo" used for control echo process. after entering "/start_echo" command, the same messages that user sent, will return as reply until the "/stop_echo" command is send.
## Result
<img width="493" alt="image" src="https://user-images.githubusercontent.com/44172962/191020141-d4b0920e-faca-49f8-821a-52d78e2a5216.png">
