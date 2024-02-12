{{ config(materialized='ephemeral') }}

with contracts as (
    select * from {{ source('snowflake', 'contracts') }}
)

select 
    c.id,
    c.location,
    c.object,
    {{ lower_price('price', 100) }} as lowered_price,
    c.price as original_price
from contracts c
