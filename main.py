from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown

from dotenv import load_dotenv
load_dotenv()

# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

# Initialize the OpenAI GPT-4 language model
OpenAIGPT4 = ChatOpenAI(
    model= "gpt-3.5-turbo" ## "gpt-4"
)

query = 'Should I invest in residential real estate in Savannah Georgia?'
kw = ['job trends', 'population trends', 'quality of life trends', 'things to do trends']
keywords = f', focusing on {kw}'

# Instantiate the agents
editor = agents.editor_agent(query, keywords)
news_fetcher = agents.news_fetcher_agent(query, keywords)
news_analyzer = agents.news_analyzer_agent(query, keywords)
newsletter_compiler = agents.newsletter_compiler_agent()

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher, query, keywords)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task], query, keywords)
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
    verbose=2
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)


