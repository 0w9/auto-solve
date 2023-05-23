from langchain.document_loaders.image import UnstructuredImageLoader

loader = UnstructuredImageLoader("test_fr.jpeg")
data = loader.load()
print(data[0])