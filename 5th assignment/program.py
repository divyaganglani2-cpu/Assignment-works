import re
import csv
import os

# Weekly Topics applied here:
# 1. Regex: Pattern matching for extraction
# 2. Generators: Memory-efficient file reading
# 3. Sorting/Comprehensions: Data filtering and ordering
# 4. CSV Module: Writing the final structured report

def raw_data_generator(file_path):
    """
    Generator function to read the file line by line.
    Should yield lines one at a time.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line
    else:
        print("Error: raw_data.txt not found!")
#takes a phrase and returns dictionary of found data after extracting through re
def extract_user_data(phrase):
    email=re.search(r"[\w\.-]+@[\w\.\-]+\.\w+",phrase)
    phone=re.search(r"\b\d{10}\b",phrase)
    name=re.search(r"\b(?!(?:User|System|Entry|Yes|Status|Random|Log|Noise|Registration|Final|Dummy|Garbage|End|Date|ID|Dept|Remarks|Location|Role|Batch|City|Verified|Mobile|Ph|Contact|Priority)\b)[A-Z][a-z]+\b(?:\s[A-Z][a-z]+)*",phrase)

    if email and phone and name:
        return{
            "Name":name.group(),
            "Email":email.group(),
            "Phone":phone.group()
        }
    return None


def process_assignment():
    # Step 1: Use the generator to fetch lines
    data=[]
    g=raw_data_generator("raw_data.txt")
    for i in g:
        # Step 2: Extract data using re.search() or re.findall()
        dict_of_data=extract_user_data(i)
        if dict_of_data:
            data.append(dict_of_data)
    print(data)
    # Step 3: Filter Gmail users using List Comprehension
    gmail_users=[i for i in data if re.search(r"@gmail\.com$",i["Email"])]
    
    # Step 4: Sort the data by Name
    sorted_data=sorted(data,key=lambda x:x["Name"])
    # Step 5: Save to cleaned_users.csv using csv.DictWriter
    fields=["Name","Email","Phone"]
    with open ("student.csv","w",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(sorted_data)
    print("program complete")
    

if __name__ == "__main__":
    process_assignment()