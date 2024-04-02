# LangChain is an open source library that lets you build connectors to different resources and then combine those resources when producing a response.

1. Agents - Control the flow of prompts - https://python.langchain.com/docs/modules/agents/agent_types/
1. Tools - Connect to resources such as Wikipedia, Reddit or Google Search - https://python.langchain.com/docs/integrations/tools 
1. Chains - Allows you to connect outputs from one agent to input of another agent.


# agent_chain.run(Prompt)
Asks the LLM to query a tool and then give a resonse.  
## Flow or information
* Action: yahoo_finance_news
* Action Input: MSFT
*Observation: Forget Inflation, Buy These 5 Stocks on the Ongoing Tech Rally
Stocks like NVIDIA Corporation, Amazon.com, Inc. (AMZN), Meta Platforms, Inc. (META), Logitech International (LOGI) and Microsoft Corporation (MSFT) are ongoing leading the tech rally.
* Thought:I now know the final answer
* Final Answer: The financial news for
