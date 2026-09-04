select
    order_date,
    count(*) as paid_orders,
    sum(amount) as revenue
from {{ ref('stg_orders') }}
where status = 'paid'
group by order_date
