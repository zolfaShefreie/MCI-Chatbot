
# Task-001
task title: develop speech recognition for persian language using vosk toolkit.<br/>
<i>this task develop on google colab and use pakeges related to it, so for running this task use google colab.</i>
## work steps:
1. install vosk and ffmpeg-python packages using pip
2. download perian vosk models</br>
the defualt model is vosk-model-small-fa-0.4 that isn't good enough. so <b>vosk-model-fa-0.5</b> is used in this task. with linux commands (wget, unzip) can download model file (you can access model file urls from [vosk websit](https://alphacephei.com/vosk/models)) and unzip it.
3. load model</br>
useing Model and KaldiRecognizer from vosk package for load model.
4. audio file preparation</br>
you can't recode sounds in colab in normal way. so there is two way to prepare the audio file
* upload file to colab from <b>files section</b>
<img width="203" alt="image" src="https://user-images.githubusercontent.com/44172962/189521977-e65ca9b3-784d-4058-8704-038f7a2fbad9.png">

* Run <b>Record Sound and save it to wav file</b> part on code to record sound.</br>
js script used to record sound by user device. you can show elements like button and get the output of script with IPython.display.HTML and google.colab.output.eval_js modules. this scipt record sound using MediaRecorder package from user's microphone. the source code is available at [colab file](https://colab.research.google.com/gist/ricardodeazambuja/03ac98c31e87caf284f7b06286ebf7fd/microphone-to-numpy-array-from-your-browser-in-colab.ipynb#scrollTo=XZlWKbI4A1Rp) that has made small changes to save the recorded audio.
5. convert audio file to text using model
get path of audio file from user the defual is same the recording part's file path. open it and make loop tho convert every frame of audio to text and get final result.
## Result of a example
below file was recorded by <b>Record Sound and save it to wav file</b> part on ipynb file.</br>

https://user-images.githubusercontent.com/44172962/189517810-2c5e1f1f-e9ec-49dd-b902-32d7cae56598.mp4

reuslt of file is like:</br>

<img width="193" alt="image" src="https://user-images.githubusercontent.com/44172962/189518051-817fb843-4dfa-49af-b792-3443f2dfc9ff.png">

<i>the partioal parts have been repeated several times in the real result</i>
