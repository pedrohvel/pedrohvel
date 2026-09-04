with source as (
    select * from {{ ref('orders') }}
),
normalized as (
    select
        cast(order_id as {{ dbt.type_string() }}) as order_id,
        cast(customer_id as {{ dbt.type_string() }}) as customer_id,
        lower(trim(cast(status as {{ dbt.type_string() }}))) as status,
        cast(amount as numeric(18, 2)) as amount,
        cast(order_date as date) as order_date,
        cast(updated_at as {{ dbt.type_string() }}) as updated_at
    from source
)
select * from normalized
