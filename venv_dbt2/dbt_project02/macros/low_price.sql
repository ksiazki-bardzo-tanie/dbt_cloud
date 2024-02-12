{% macro lower_price(column_name, factor) %}
    (
        {{ column_name }} / {{ factor }}
    )
{% endmacro %}