# Task-007
task title: develop tts service</br>
this task has three subtask.
## Subtask-1
subtask title: train English tts model using nemo toolkits (tacotron2) </br>
### Work Steps
- install the requirements for nemo model
- download some scripts for train tacotron2</br>
some scripts for train model, config files and phonemes dictionary were downloaded
- transform dataset to nemo valid format and train the model</br>
[LJSpeech dataset](https://keithito.com/LJ-Speech-Dataset/) is used in this project. according the [nemo docs](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/tts/datasets.html), nemo has prepared a script for download dataset and trasform it to valid format. then use tacotron script to train nem model.</br>

the model save as tacotron2.nemo file. you can load model and use it. In [nootbook](https://github.com/zolfaShefreie/MCI-Chatbot/blob/main/task-007/English_tacotron_nemo.ipynb) has a sample that shows how to use model and convert text to speech.
## Subtask-2
subtask title: train Pertian tts model using nemo toolkits (tacotron2) </br>
### Work Steps
- download dataset and clean data
- create Phoneme dictionary file for Persian language
## Subtask-3
subtask title: connect model to telegram bot </br>
