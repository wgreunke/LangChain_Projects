#This file test the LangChain Wikipedia Connector
print("")
print("********************")


#Connect to Wikipedia
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

#print(wiki_tool.run({"query": "Volkswagon Bus"}))

#Connect to Yahoo Finance


