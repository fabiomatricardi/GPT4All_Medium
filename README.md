# GPT4All_Medium
Repo of the code from the Medium article


---
 ## Update and bug fixes - 2023.05.30
- [x] llama.cpp: loading model from ./models/ggml-model-q4_0.bin 'std::runtime_error' what(): unexpectedly reached end of file

Buğra Çakır reported an issue, running the code on Python 3.11.3 (main, May 24 2023, 00:00:00) [GCC 13.1.1 20230511 (Red Hat 13.1.1-2)] on linux<br>
He solved the issue installing a different llama-cpp-python version with
```
pip install llama-cpp-python==0.1.48
```



 ## Update and bug fixes - 2023.05.25
- [x] Cannot install llama-cpp-python

This happens usually only on Windows users. Running the installation of llama-cpp-python, required by <br>
LangChain with the llamaEmbeddings, on windows CMake C complier is not installed by default, so you cannot build from source. <br>
On Mac Users with Xtools and on Linux, usually the C complier is already available on the OS. <br>
To avoid the issue you MUST use pre complied wheel. <br>
Go here [https://github.com/abetlen/llama-cpp-python/releases](https://github.com/abetlen/llama-cpp-python/releases)  <br> 
and look for the complied wheel for your architecture and python version - **you MUST take Weels Version 0.1.49**  <br>
because higher versions are not compatible. <br>

<img src="https://i.ibb.co/8j50gXw/issue-llama-cpp-Built-In-compiled-Wheels.jpg">

In  my case I have Windows 10, 64 bit, python 3.10 <br>
so my file is llama_cpp_python-0.1.49-cp310-cp310-win_amd64.whl <br>


## Troubleshooting Section
**Update and bug fixes - 2023.05.23**<br>
- [x] Some readers faces an issue with `langchain.callbacks` <br>
```
ImportError: cannot import name 'CallbackManager' from 'langchain.callbacks.base' 
on the line importing CallbackManager in my_langchain.py.
```
- [x] Michal Founě solved it follwing the issue as described in https://github.com/hwchase17/chat-langchain/issues/70 with
`pip install langchain==0.0.142` <br>
<br><br>
- [x] On the GitHub repo there is already an issue solved related to `GPT4All' object has no attribute '_ctx'`. Fixed specifying the versions during pip install like this:

```
pip install pygpt4all==1.0.1 
pip install pygptj==1.0.10 
pip install pyllamacpp==1.0.6
```

- [x] Another quite common issue is related to readers using **Mac with M1 chip**. The arm64 architecture is a little reluctant to work. As suggested to Emile Pretorius and to Yosef Agung Wicaksono you can try to fix it with the guidelines in this document https://docs.google.com/document/d/1JDMBTOjbRtJo49z1SKEnvfG1a4JQMjWFT7hvfZZU4vQ/edit . <br>
it seems to have worked with them.<br><br>
- [x] Bruce Wen suggested to avoid all the problems mentioned above giving already all the versions in the code: all the pip instructions are now updated.<br><br>
- [x] BEpshtein suggested to update the article and the Github repo: keep reporting the issues and I will try to reply including the smart troubleshooting of the readers.<br><br>
- [x] geert van kempen got the following issue:
```
File "/Users/XXXX/GPT4ALL_gvk/.venv/lib/python3.10/site-packages/pyllamacpp/model.py", line 402, in __del__
if self._ctx:
AttributeError: 'GPT4All' object has no attribute '_ctx'
```
He was using pygpt4all version 1.1.0, and pygptj 2.0.3 (and he was using version 1.0.6 of pyllamaccp) and he solved it with the GitHub solved Issue (see above).<br><br>
- [x] Norman Procope and Kon16ov got problems loading the pdfs from my GitHub repo. It was solved downloading again the pdf or checking if UTF-8 format was used or not: fixed with decoding `text = text.decode()` <br><br>
- [x] Alain Uro and other users got an error on the `pygtp4all callbacks`. As greatly explained and solved by **Rajneesh Aggarwal** this happens because the pygpt4all PyPI package will no longer by actively maintained and the bindings may diverge from the GPT4All model backends. He solved it installing instead of pygtp4all `pip install gpt4all` <br>
The code must be changed as well as follows:
```
import gpt4all
model_path = '.\models'
model = gpt4all.GPT4All(model_name='gpt4all-converted.bin', model_path=model_path, model_type='llama', allow_download=True)
model.generate("Once upon a time, ", streaming=True)
```
- [x] Shamik Dhar also had an issue with the new_text_callback.
```
def new_text_callback(text):
print(text, end="")
model = GPT4All('./models/gpt4all-converted.bin')
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
I am getting an error here that there is no argument in 
the generate module of name new_text_callback
```
It was solved by Oscar Jeong changing the code generate() to `cpp_generate()` as follows:
```
# Just change generate() to cpp_generate() then it works.
def new_text_callback(text):
print(text, end="")
model = GPT4All('./models/gpt4all-converted.bin')
model.cpp_generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
```


If this story provided value and you wish to show a little support, you
