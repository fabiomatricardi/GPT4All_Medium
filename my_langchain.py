from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

local_path = './models/gpt4all-converted.bin' 
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

template = """Question: {question}

Answer: Let's think step by step on it.

"""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = GPT4All(model=local_path, callback_manager=callback_manager, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Hardcoded question
question = "What Formula 1 pilot won the championship in the year Leonardo di Caprio was born?"

# User imput question...
#question = input("Enter your question: ")

llm_chain.run(question)