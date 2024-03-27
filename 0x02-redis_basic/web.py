#!/usr/bin/env python3
"""
Fonction pour obtenir le contenu HTML d'une URL avec mise en cache et suivi d'accès
"""
import requests
import redis

redis_client = redis.Redis()

def get_page(url: str) -> str:
    count_key = f"count:{url}"
    page_content = redis_client.get(url)
    if not page_content:
        response = requests.get(url)
        page_content = response.text
        redis_client.setex(url, 10, page_content)
        redis_client.incr(count_key)
    return page_content
