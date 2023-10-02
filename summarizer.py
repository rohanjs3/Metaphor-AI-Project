from metaphor_python import Metaphor

API_KEY = "5fa48571-8631-4edf-af1f-20b19b907d33"  # Your Metaphor API key
metaphor = Metaphor(API_KEY)

def fetch_and_aggregate_articles(query, num_results=5):
    # Step 1: Search for articles based on the given query
    response = metaphor.search(query, num_results=num_results)
    
    # Extract the IDs of the articles
    article_ids = [result.id for result in response.results]
    
    # Step 2: Fetch the contents of these articles
    contents_response = metaphor.get_contents(article_ids)
    
    # Aggregate the fetched contents
    print(contents_response)
    #aggregated_content = "\n\n".join([content for content in contents_response.contents])
    
    return contents_response.contents