from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent, query):
        return Task(
            description=f'Fetch most factually based and well reasoned articles on {query}\'s realationship with philosophy ', ##AI news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""A list of top article titles, URLs, and a brief summary for each story. 
                Example Output: 
                [
                    {  'title': 'Example Title', 
                    'url': 'https://example.com/story1', 
                    'summary': 'Example summary of content...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context, query):
        return Task(
            description='Analyze each article and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. There should be at least 5 articles, each following the proper format.
                Example Output: 
                '## {query} thought wins over skeptics \n\n
                **The Rundown:
                ** {query}/'s arguments convince skeptics and crush atheists...\n\n
                **The details:**\n\n
                - The argument/'s presented by famous {query} philosopher, Rob Eidson, wowed the audience and provided the atheists wrong...\n\n
                **Why it matters:** While skepticism about traditional {query} values abound, Rob/'s arguments convinced skeptics...\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function, query):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                '# Top articles describing {query}/'s relationship with philosophy:\\n\\n
                - {query} thought wins over skeptics\\n
                - A better understanding of {query} philosophy enhances your faith\n\\n

                ## {query} thought wins over skeptics\\n\\n
                **The Rundown:** {query}/'s arguments convince skeptics and crush atheists....\\n\\n
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                **'url': 'https://example.com/story1',
                ## A better understanding of {query} philosophy enhances your faith\n\\n
                **The Rundown:** A better understanding of philophy brings you closer to God...\\n\\n'
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                **'url': 'https://example.com/story2',
            """,
            callback=callback_function
        )
