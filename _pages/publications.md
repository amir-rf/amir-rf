---
layout: default
title: Publications
permalink: /publications/
---

## Journal Articles

{% assign journal_pubs = site.publications | where: "type", "Journal" %}
{% for pub in journal_pubs %}
- **{{ pub.title }}**  
  {{ pub.authors }}  
  _{{ pub.venue }}_, {{ pub.date | date: "%Y" }}
  {% if pub.paperurl %}[PDF]({{ pub.paperurl }}){% endif %}
{% endfor %}

---

## Conference Papers

{% assign conf_pubs = site.publications | where: "type", "Conference" %}
{% for pub in conf_pubs %}
- **{{ pub.title }}**  
  {{ pub.authors }}  
  _{{ pub.venue }}_, {{ pub.date | date: "%Y" }}
  {% if pub.paperurl %}[PDF]({{ pub.paperurl }}){% endif %}
{% endfor %}

---

## Datasets

{% assign dataset_pubs = site.publications | where: "type", "Dataset" %}
{% for pub in dataset_pubs %}
- **{{ pub.title }}**  
  {{ pub.authors }}  
  _{{ pub.venue }}_, {{ pub.date | date: "%Y" }}
  {% if pub.paperurl %}[Link]({{ pub.paperurl }}){% endif %}
{% endfor %}
