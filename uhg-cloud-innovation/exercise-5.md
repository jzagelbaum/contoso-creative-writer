# DIY Publisher Exercise

In this exercise, you'll create your own publisher component that formats articles according to a style guide. The publisher is responsible for taking raw content and applying consistent formatting before publishing.

## Style Guide Reference
Here's the Contoso style guide that your publisher will need to implement:

    # Contoso Style Guide
    - Use H2 for main headings and H3 for subheadings
    - All product names should be in bold
    - All links should use the format [text](url)
    - Add the Contoso logo at the top of the article
    - Include a "Share this article" section at the bottom
    - Use the Contoso color scheme: #0078D4 for headings, #333333 for body text

## Task 1: Create the Publisher Prompt

1. Create a file named `publisher.prompty` in the `src/api/agents/publisher` directory
2. Design a prompt that instructs an AI to format an article according to the style guide
3. Include the following components in your prompt:
   - System message explaining the publisher's role
   - Placeholders for the article content: `{{article}}`
   - Placeholders for the style guide: `{{styleGuide}}`
   - Placeholders for optional feedback: `{{feedback}}`
   - Instructions for formatting the response

## Task 2: Implement the Publisher Agent

1. Examine the `publisher.py` file in the `src/api/agents/publisher` directory
2. Implement the `publish()` function that:
   - Takes an article, style guide, and optional feedback as parameters
   - Uses prompty to execute your `publisher.prompty` file
   - Returns the formatted content
3. Implement the `process()` function that:
   - Parses the response from the AI
   - Separates the formatted article from any feedback
   - Returns a dictionary with the formatted article and feedback

## Task 3: Integrate the Publisher into the Orchestrator

1. Open the `orchestrator.py` file in the `src/api` directory
2. Find the section where the publisher is called
3. Ensure the publisher agent:
   - Receives the article from the writer
   - Receives the style guide
   - Returns the formatted article
4. Make sure the publisher response is properly returned to the frontend

## Task 4: Test Your Implementation

1. Run your application and create a new article
2. Check that the final published article follows all the style guide requirements
3. Verify that:
   - Headings use the correct format
   - Product names appear in bold
   - Links use the correct format
   - The Contoso logo appears at the top
   - A "Share this article" section appears at the bottom
   - Colors match the Contoso scheme

## Bonus Challenge

Add a feature to your publisher that validates the article against the style guide and provides feedback if any guidelines aren't followed.