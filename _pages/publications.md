---
layout: default
title: Publications
permalink: /publications/
---

## Journal Articles

{% assign journal_pubs = site.publications | where: "type", "Journal" %}
{% if journal_pubs.size > 0 %}
<ul>
  {% for pub in journal_pubs %}
    <li>
      <strong>{{ pub.title }}</strong><br>
      {{ pub.authors }}<br>
      <em>{{ pub.venue }}</em>, {{ pub.date | date: "%Y" }}
      {% if pub.paperurl %}
        <a href="{{ pub.paperurl }}" target="_blank">[PDF]</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<p>No journal articles listed yet.</p>
{% endif %}

---

## Conference Papers

{% assign conf_pubs = site.publications | where: "type", "Conference" %}
{% if conf_pubs.size > 0 %}
<ul>
  {% for pub in conf_pubs %}
    <li>
      <strong>{{ pub.title }}</strong><br>
      {{ pub.authors }}<br>
      <em>{{ pub.venue }}</em>, {{ pub.date | date: "%Y" }}
      {% if pub.paperurl %}
        <a href="{{ pub.paperurl }}" target="_blank">[PDF]</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<p>No conference papers listed yet.</p>
{% endif %}

---

## Datasets

{% assign dataset_pubs = site.publications | where: "type", "Dataset" %}
{% if dataset_pubs.size > 0 %}
<ul>
  {% for pub in dataset_pubs %}
    <li>
      <strong>{{ pub.title }}</strong><br>
      {{ pub.authors }}<br>
      <em>{{ pub.venue }}</em>, {{ pub.date | date: "%Y" }}
      {% if pub.paperurl %}
        <a href="{{ pub.paperurl }}" target="_blank">[Link]</a>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
<p>No datasets listed yet.</p>
{% endif %}
