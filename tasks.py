from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent, query, keywords):
        return Task(
            description=f'Fetch most factually based and well reasoned articles on the idea that {query} {keywords}', 
            agent=agent,
            async_execution=True,
            expected_output="""A list of content descriptions, URLs, and a brief summary of the piece, and a list of
            relevant evidence. 
                Example Output: 
                [
                    {  'title': 'Description of content, 
                    'url': 'https://example.com/story1', 
                    'summary': 'Overall summary of content...',
                    [description of the most relevant piece of evidence, description of the next most relevant piece of evidence ...]
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context, query, keywords):
        return Task(
            description="""Analyze each piece of content ranking the most well reasoned and fact based pieces for inclusion in the newsletter.
            Analyze at least 50 different articles. Ensure there are at least 10 well-formatted pieces ranked on the strength of their reasoning and evidence""",
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each piece of content, including an overall summary, its ranking based on the strength of 
                its reasoning and evidence, and detailed bullet points of the evidence presented in each piece of content. There should be summaries for at least 
                10 pieces of content, each following the proper format.
                Example Output: 
                '## The below data provide support for the idea that inflation hurts Middle class Americans\n\n
                **Summary:
                ** This article discusses the relationthip between real wages and inflation for middle class Americans. It explains that... \n\n
                **The evidence:**\n\n
                - A survey of middle class Americans shows ...\n\n
                - A statistical analysis of the relationship of real wages and inflation revealed ...\n\n
                
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout. Include an overall summary, a summary for each
                piece of content, and a bullet point list of the evidence. Include the five highest ranking pieces of content.
                Example Output: 
                '# Overall Summary:\\n\\n
                After exhaustive research, the below articles provide support for the idea that inflation hurts the middle class. The evidence suggests
                that inflation hurts the middle class by depressing real wages, requires them to work longer hours which results in negative outcomes like
                higher suicide rates ...

                ## 1. [Why the middle class benefits from inflation](https://cepr.org/voxeu/columns/why-middle-class-benefits-inflation) - Article Publisher
                ## Summary: This article discusses the relationship between real wages and psychological outcomes for middle class Americans.\\n\\n
                \\n\\n
                **The evidence:**\n\n
                    - A survey of middle class Americans shows ...\n\n
                    - A statistical analysis of the relationship of real wages and inflation revealed ...\n\n
                ##2. ## 2. [Inflation has made the 1%�and the middle class�richer](https://fortune.com/2023/10/18/inflation-tax-made-1-middle-class-richer-nber-working-paper/) - Article Publisher
                ## Summary: This study explains the correlation between technological change and middle class real wages\n\\n
                **The evidence:**\n\n
                    - A statiscal analysis of technological change and real wages reveals ...\n\n
                    - A case study of the introduction of factory robots on workers...\n\n

            """,
            callback=callback_function
        )
