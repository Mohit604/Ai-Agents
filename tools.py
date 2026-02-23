from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime
from tools import search_tool, wiki_tool,save_tool
from datetime import datetime

def save_to_file(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"\n---\nTimestamp: {timestamp}\nData:\n{data}\n---\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data saved to {filename}"
save_tool = tool(name="save_to_file", func=save_to_file, description="Save the research output to a file with a timestamp")
search = DuckDuckGoSearchRun()
search_tool = tool(name="search",func=search.run,description="Search the web for information")
api_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

 