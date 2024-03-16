from crewai import Agent
from tools.search_tools import SearchTools


class AINewsLetterAgents():
    def editor_agent(self, query):
        return Agent(
            role='Editor',
            goal="""Oversee the creation of a newsletter about {query}  studying philosophy. 
            You ensure that the newsletter contains compelling description and urls for 5 articles.""",
            backstory="""With a keen eye for logic and a passion for facts, you ensure that the newsletter
            not only informs but also presents compelling fact based evidence to supporting or refuting the theme. """,
            allow_delegation=True,
            verbose=True,
            max_iter=1
        )

    def news_fetcher_agent(self, query):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top articles examining {query}  relationship to philosophy',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful news and essays
            on {query} studying philosophy, ensuring that our readers are always in the know.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def news_analyzer_agent(self, query):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of {query} relationship with philosophy, making them accessible and engaging for our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow
            newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
        )
