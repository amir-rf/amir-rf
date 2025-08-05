from scholarly import scholarly
from slugify import slugify
import os

# === CONFIGURATION ===
SCHOLAR_ID = "aSdNHA8AAAAJ"  # Replace with your actual ID
OUTPUT_DIR = "_publications"  # Folder in academicpages
os.makedirs(OUTPUT_DIR, exist_ok=True)

def classify_publication(venue: str) -> str:
    venue_lower = venue.lower()
    if any(k in venue_lower for k in ["conference", "proceedings", "symposium", "workshop"]):
        return "Conference"
    elif any(k in venue_lower for k in ["dataset", "data", "repository"]):
        return "Dataset"
    else:
        return "Journal"

def save_publication(pub):
    title = pub.get('bib', {}).get('title', 'Untitled')
    authors = pub.get('bib', {}).get('author', 'Unknown')
    year = pub.get('bib', {}).get('pub_year', '9999')
    venue = pub.get('bib', {}).get('venue', 'Unknown Venue')
    url = pub.get('pub_url', '')

    pub_type = classify_publication(venue)
    filename = slugify(title) + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        print(f"Skipping existing: {title}")
        return

    md_content = f"""---
title: "{title}"
collection: publications
type: "{pub_type}"
permalink: /publication/{slugify(title)}
authors: {authors}
date: {year}-01-01
venue: "{venue}"
paperurl: {url}
citation: "{authors}, {venue}, {year}"
---
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Saved: {title} ({pub_type})")

def main():
    print(f"Fetching publications for Scholar ID: {SCHOLAR_ID}")
    author = scholarly.search_author_id(SCHOLAR_ID)
    if not author:
        print("Author not found.")
        return
    author_filled = scholarly.fill(author)
    pubs = author_filled.get('publications', [])

    for pub in pubs:
        filled_pub = scholarly.fill(pub)
        save_publication(filled_pub)

if __name__ == "__main__":
    main()
