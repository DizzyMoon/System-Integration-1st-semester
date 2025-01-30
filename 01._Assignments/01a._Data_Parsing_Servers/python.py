import pandas as pd
import yaml
from pprint import pprint
import xml.etree.ElementTree as ET


df_json = pd.read_json("01._Assignments/01a._Data_Parsing_Servers/data/me.json")
df_csv = pd.read_csv("01._Assignments/01a._Data_Parsing_Servers/data/me.csv")
xml_tree = ET.parse("01._Assignments/01a._Data_Parsing_Servers/data/me.xml")
xml_root = xml_tree.getroot()


with open("01._Assignments/01a._Data_Parsing_Servers/data/me.yaml", "r") as f:
    df_yaml = yaml.safe_load(f)  # YAML


# Extract data for XML example:
name = xml_root.find("name").text
age = xml_root.find("age").text
hobbies = [hobby.text for hobby in xml_root.findall(".//hobby")]

df_xml = pd.DataFrame({"name": [name] * len(hobbies), "age": [age] * len(hobbies), "hobby": hobbies})
    

# Pretty print YAML
yml_name = df_yaml["name"]
yml_age = df_yaml["age"]
yml_hobbies = df_yaml["hobbies"]

# Convert into a DataFrame
df_yaml = pd.DataFrame({"name": [yml_name] * len(yml_hobbies), "age": [yml_age] * len(yml_hobbies), "hobbies": yml_hobbies})

if __name__ == "__main__":
    print("------- JSON --------------------\n" + df_json.to_string())
    print("------- CSV ---------------------\n" + df_csv.to_string())
    print("------- XML ---------------------\n" + df_xml.to_string(index=False))
    print("------- YAML ---------------------")
    pprint(df_yaml)

