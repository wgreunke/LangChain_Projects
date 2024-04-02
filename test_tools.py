#This file test the LangChain Wikipedia Connector
print("")
print("********************")
#LangChaing Reference
#https://python.langchain.com/docs/integrations/tools


#Connect to Wikipedia
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import os
from dotenv import load_dotenv

#Wikipedia ***********************************
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

#print(wiki_tool.run({"query": "Volkswagon Bus"}))


#Connect to Yahoo Finance
load_dotenv()
#print(os.getenv('chat_key'))
os.environ["OPEN_AI_KEY"]=os.getenv('chat_key')

from langchain.agents import AgentType, initialize_agent
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_openai import ChatOpenAI

