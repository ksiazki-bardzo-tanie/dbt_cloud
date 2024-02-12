select * 
from {{  ref('contracts_low_price') }}
where id > 6