
# Task-003
task title: Train japster model for persian language with CommonVoice dataset using nemo toolkit</br>
this task develop on google colab and use pakeges related to it, so for running this task use google colab.

## Work Step
1. load dataset
CommonVoice is used for this task that is available in [link](https://commonvoice.mozilla.org/en/datasets). I used one of [nemo script](https://github.com/NVIDIA/NeMo/blob/main/scripts/dataset_processing/get_commonvoice_data.py) to load dataset. this scrpit download the dataset based on language and vesion of dataset, extract and convert to nemo valid format. unfortunately this script doesn't support the lastest version of dataset so i used cv-corpus-6.1-2020-12-11 version.</br>
<i>the main dataset has about 8G data but because of google colab limitations, only 30 percent of it is used.</i>
2. preprocess the dataset
in this task 3 preprocess language task is applied:
- normalized persian texts for handling half space in persian language
- replace some character that you can see the detail in image below
<img width="71" alt="image" src="https://user-images.githubusercontent.com/44172962/190924024-0486b9d8-3813-4073-b297-8123e45649dc.png">

- delete some character like !@#$%^&* and so on
<p>some character is used in dataset that isn't used in persian language. this character are not deleted because they have different sound like hamze or made some vowels obviouse in text like /ae/ in persian language</p>
3. fine-tuning Jasper model
there are multi pretrained model that use can see some of them in below. in this task we should use Jasper model so stt_en_jasper10x5dr model is used.

<img width="690" alt="image" src="https://user-images.githubusercontent.com/44172962/190924496-22f4d3af-5a34-45ee-8a21-f1c3e45ff75c.png">

some configs like vocabulary, dataset dirs, batch_size, optimizer 's config and ... is applied on model and train it with persian dataset.</br>
<i>also resume pretrained model from file is considered but it look likes there is a bug in pytorch lightning package that model is trained from scratch (has higher loss than last epoch that is trained) and has low training performance (decreasing the loss is so slow). this issue is mentioned [here](https://github.com/Lightning-AI/lightning/issues/4045) too.</i>

## Result
model shows better performance after some epochs trainning.</br>
before:
<img width="126" alt="image" src="https://user-images.githubusercontent.com/44172962/190925462-8ecb0e27-e4d1-4d2b-a8e0-9c4fb24bf664.png">

after 5 epochs:
<img width="135" alt="image" src="https://user-images.githubusercontent.com/44172962/190925497-34db3a7d-2fd9-4512-a08d-0c8731ee8ba5.png">

<i>Unfortunately, because of the limitation of Google colab, the process of training the model has not been completed, and the results will be shared here after the full trainning.</i>

