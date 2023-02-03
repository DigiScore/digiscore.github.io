---
layout: page
title: Case Studies
---

<div id="full-tags-list">
    {%- for tag in tags_list -%}
    <div class="post-list">
        {%- for post in site.tags.case_studies -%}
        <article class="post-preview">
            {%- capture thumbnail -%}
                {% if post.thumbnail-img %}
                    {{ post.thumbnail-img }}
            {% elsif post.cover-img %}
                {% if post.cover-img.first %}
                    {{ post.cover-img[0].first.first }}
            {% else %}
                {{ post.cover-img }}
          {% endif %}
        {% else %}
        {% endif %}
      {% endcapture %}
      {% assign thumbnail=thumbnail | strip %}
        </article>
        {%- endfor -%}
    </div>
    {%- endfor -%}
</div>