---
layout: default
title: Publications
permalink: /publications/
---

<h2>Journal Articles</h2>
{% assign journal_pubs = site.publications | where: "type", "Journal" %}
{% for pub in journal_pubs %}
  <p>
    <b>{{ pub.title }}</b><br>
    {{ pub.authors }}<br>
    <i>{{ pub.venue }}</i>, {{ pub.date | date: "%Y" }}<br>
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">[PDF]</a>
    {% endif %}
  </p>
{% endfor %}

<h2>Conference Papers</h2>
{% assign conf_pubs = site.publications | where: "type", "Conference" %}
{% for pub in conf_pubs %}
  <p>
    <b>{{ pub.title }}</b><br>
    {{ pub.authors }}<br>
    <i>{{ pub.venue }}</i>, {{ pub.date | date: "%Y" }}<br>
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">[PDF]</a>
    {% endif %}
  </p>
{% endfor %}

<h2>Datasets</h2>
{% assign dataset_pubs = site.publications | where: "type", "Dataset" %}
{% for pub in dataset_pubs %}
  <p>
    <b>{{ pub.title }}</b><br>
    {{ pub.authors }}<br>
    <i>{{ pub.venue }}</i>, {{ pub.date | date: "%Y" }}<br>
    {% if pub.paperurl %}
      <a href="{{ pub.paperurl }}">[Link]</a>
    {% endif %}
  </p>
{% endfor %}
