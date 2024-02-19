import json
import pandas as pd

"""
LAB 3 JSON and Pandas

Objective: convert JSON to Pandas data frame and present results
Date: 2/18/2024
Name: Riley Fletcher
"""

with open('data.json', 'r') as file:
    json_string = file.read()
    data = json.loads(json_string)
    df = pd.DataFrame(data['teams'])

    """
    Step 3: Will print the first 100 rows of the data frame
    """
    print(df[1:101])
    
    """
    4A: How many teams? A: 320 different teams
    """
    unique_teams_count = df['tid'].nunique()
    print("\nNumber of unique teams:", unique_teams_count)

    """
    4B: How many teams in Virginia? A: 13 teams in Virginia
    """
    virginia_count = df['state'].value_counts().get('VA', 0)
    print("\nNumber of rows where state is Virginia:", virginia_count)

    """
    4C: Duplicate mascots grouped by number, 1 does not count
    """
    mascot_counts = df['name'].value_counts()
    mascot_counts_filtered = mascot_counts[mascot_counts > 1]
    mascot_counts_filtered = mascot_counts_filtered.items()
    print("\nCity counts as list of tuples:")
    for mascot in mascot_counts_filtered:
        print(mascot)
