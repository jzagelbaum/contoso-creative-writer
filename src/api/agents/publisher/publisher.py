import os
import json
from pathlib import Path
import prompty
from prompty.tracer import trace

# Define style guide as a constant
STYLE_GUIDE = """# Contoso Style Guide
- Use H2 for main headings and H3 for subheadings
- All product names should be in bold
- All links should use the format [text](url)
- Add the Contoso logo at the top of the article
- Include a "Share this article" section at the bottom
- Use the Contoso color scheme: #0078D4 for headings, #333333 for body text"""

@trace
def publish(article, feedback="No Feedback"):
    try:
        stream_result = prompty.execute(
            "publisher.prompty",
            parameters={"stream": True},
            inputs={
                "article": article,
                "styleGuide": STYLE_GUIDE,
                "feedback": feedback,
            },
        )
        
        # Collect the stream content into a string
        result = ""
        for chunk in stream_result:
            result += str(chunk)

        # Write to file if output_file is provided
        file_path = None
        output_file = "publisher_output.md"
        if output_file:
            try:
                output_path = Path(output_file)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result)
                file_path = str(output_path.absolute())
            except Exception as e:
                feedback += f"\nError writing to file: {str(e)}"

    except Exception as e:
        result = f"An exception occured: {str(e)}"
    
    return result

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    
    # Simple test article
    sample_article = """
    # Winter Camping Trends
    
    Camping has become increasingly popular in winter months. Many outdoor enthusiasts are discovering the beauty of snow-covered landscapes.
    
    Our Contoso Extreme Weather Tent and Contoso Alpine Backpack are perfect companions for winter adventures.
    """
    
    # Test publishing functionality
    result = publish(sample_article)
    
    # Still print to console for reference
    print(result)
