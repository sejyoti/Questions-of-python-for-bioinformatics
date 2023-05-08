import pandas as pd
from pandasql import sqldf

# Load and parse the csv file into a pandas dataframe
df = pd.read_csv('tasks_info.csv')

# Define the SQL query to extract the required task ids
sql_query = """
SELECT task_id
FROM df
WHERE task_group_id IN (
    SELECT task_group_id
    FROM df
    WHERE task_status = 'success'
    GROUP BY task_group_id
    HAVING COUNT(*) > 2
)
"""

# Execute the SQL query over the dataframe
result = sqldf(sql_query)

# Output the list of required task ids
task_ids = list(result['task_id'])
print(task_ids)

