---
layout: page
title: Genres
permalink: /genres/
---

{% for genres in site.tags %}
{% assign genre = genres | first %}
<div class="container featured " id="{{genre}}"><h3>{{genre | capitalize}}</h3>
   {% for post in site.tags[genre] %}
        <article class="post" itemscope itemtype="http://schema.org/BlogPosting" role="article">
      <a href="{{ post.url }}" itemprop="url" style="text-decoration: none">
          <div class="article-item">
            <header class="post-header" style="color:#66a3ff">
              <h2 class="post-title" itemprop="name" style="color:#000">{{ post.title }}</h2>
            </header>
            <i>{{post.author}}</i>
            <section class="post-excerpt" itemprop="description">
              <p>{{ post.content | strip_html | truncatewords: 30 }}</p>
            </section>
            <div class="post-meta">
              <time datetime="{{ post.date | date_to_long_string }}">{{ post.date | date_to_long_string }}</time>
            </div>
          </div>
          </a>
        </article>
      {% endfor %}
    </div>
{% endfor %}