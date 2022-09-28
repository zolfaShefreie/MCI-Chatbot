# Task 005
task title: add asr service to telegram bot that was created in task-004 using persian_jasper that was trained in task-003</br>
this task develop on google colab and use pakeges related to it, so for running this task use google colab. if you want run this you should have api token of your telegram bot.</br>
## Work Step
1. install the requirements for nemo model and telegrambotapi
2. load model</br>
the asr model is loaded from checkpoint that for accessing to functions of nemo asr model, an object of based model should be load before loading form checkpoints.
3. add some handler functions for manage the asr process</br>
add "/asr" command for asr process send a voice and bot download it, convert to wav file (orginal format is oga) and use <b>transcribe</b> function to converting to text by the provided model.
## Result
<img width="464" alt="image" src="https://user-images.githubusercontent.com/44172962/192763162-2a7c78fd-9891-40b2-acf2-2e294f5e2739.png">
