
# SELECT all female bears (name + age)
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

# SELECT all bear names alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name
    FROM bears
    ORDER BY name ASC;
"""

# SELECT alive bears (name + age) sorted youngest → oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age
    FROM bears
    WHERE alive = 1
    ORDER BY age ASC;
"""

# SELECT oldest bear
select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# SELECT youngest bear
select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""