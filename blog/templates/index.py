<h1>
    Hello
    {% if current_user.is_authenticated %}
        {{ current_user.username }}
    {% else %}
        anon
    {% endif %}
</h1>