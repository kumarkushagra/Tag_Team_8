# If "False is returned, duplicacy is found"
# If "True is returned, duplicacy is not found"


import pandas as pd

def check():
    try: 
        # Attempt to read the CSV file
        df = pd.read_csv('Database/mapping.csv')
        
        # Check for duplicate entries in 'uhid' column
        duplicate_uhids = df[df.duplicated('uhid', keep=False)]
        
        # Check for duplicate entries in 'name_of_StudyID' column
        duplicate_study_ids = df[df.duplicated('name_of_StudyID', keep=False)]
        
        # If duplicates found in either column, return False
        if not duplicate_uhids.empty or not duplicate_study_ids.empty:
            return True
        
        # If no duplicates found in both columns, return True
        return False
        
    except FileNotFoundError:
        print("File does not exist")
        return False  # Return True if file does not exist

if __name__ == "__main__":
    result = check()
    print(result)

