from urllib.parse import urlparse


class MeiliSearchHelper:
    def __init__(self, meilisearch_url, meilisearch_api_key, index_uid):
        parsed_url = urlparse(meilisearch_url)
        if not parsed_url.scheme:
            raise ValueError(f"Invalid URL '{meilisearch_url}': No scheme supplied. Please provide a valid URL with a scheme.")
        
        self.meilisearch_client = meilisearch.Client(meilisearch_url, meilisearch_api_key)
        self.meilisearch_index = self.meilisearch_client.get_index(index_uid)
        self.delete_index()
        self.meilisearch_index = self.meilisearch_client.create_index(index_uid)
