from langchain.document_loaders.image import UnstructuredImageLoader
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import ( ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate )
from langchain.schema import ( AIMessage, HumanMessage, SystemMessage )
import os

os.environ["OPENAI_API_KEY"] = "<enter your key here, or set it as an environment variable>"

chat = ChatOpenAI(temperature=0)

loader = UnstructuredImageLoader("test_fr.jpeg")
data = loader.load()

raw_data = data[0].page_content

data = chat([HumanMessage(content=f'Format this text: {raw_data}')])



with open("output.txt", "w") as f:
    f.write(data[0].content)
