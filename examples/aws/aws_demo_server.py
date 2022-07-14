from fastapi import FastAPI, Query, HTTPException, Request
from typing import Union
import json
import boto3
import re

app = FastAPI()

# Opening JSON file
with open('aws_credentials.json') as json_file:
    new_client_session_credentials = json.load(json_file)

ec2_client = boto3.client('ec2', aws_access_key_id = new_client_session_credentials["AccessKeyId"],
                                 aws_secret_access_key = new_client_session_credentials["SecretAccessKey"],
                                 aws_session_token = new_client_session_credentials["SessionToken"])

regions_response = ec2_client.describe_regions(AllRegions=True)
regions_list = [item['RegionName'] for item in regions_response["Regions"]]
shortest_region_name = min(regions_list, key=len)
longest_region_name = max(regions_list, key=len)
continents = list(set([item[:2] for item in regions_list]))

print(f"List of Continents: {continents}")
print(f"List of Region Names: {regions_list}")
print(f"Shortest Region Name: {shortest_region_name} || Length:{len(shortest_region_name)} \
      \nLongest Region Name: {longest_region_name} || Length: {len(longest_region_name)}")

def pattern_match_check(str_input):
    if (m := re.search("(af|us|ap|ca|cn|eu|sa|me)-(central|(north|south)?(east|west)?)-\d", str_input)) is None:
        return False       
    else:
        return True
        
@app.get("/get_s3_buckets_list")
def list_s3_buckets(reg_name : Union[str,None]  = Query(description="Region Name of the selected AWS Resource",default = "ap-south-1",
                                                        # regex="(af|us|ap|ca|cn|eu|sa|me)-(central|(north|south)?(east|west)?)-\d",
                                            		    min_length= len(shortest_region_name), max_length = len(longest_region_name))) -> dict:
    """Lists all the names of the S3 buckets"""
    # Retrieve the list of existing buckets using the new credentials
    if len(reg_name) == 0 or reg_name == None:
        print(f"Region name cannot be empty")
        raise HTTPException(status_code=400, detail = "Region name cannot be empty")
    if type(reg_name) != str:
        print ("Region name Type is not of type String")
        raise HTTPException(status_code=400, detail = "Region name Type is not of type String")
    if pattern_match_check(reg_name) == False:
        print("Region Name Pattern is not valid")
        raise HTTPException(status_code=400, detail = "Region name Pattern is not Valid")
    if reg_name not in regions_list:
        print(f"Region Name Input: {reg_name} is not valid")
        raise HTTPException(status_code=400, detail="Not a valid AWS Region")
        
    s3_client = boto3.client('s3', region_name = reg_name, aws_access_key_id = new_client_session_credentials["AccessKeyId"],
                                   aws_secret_access_key = new_client_session_credentials["SecretAccessKey"],
                                   aws_session_token = new_client_session_credentials["SessionToken"])
                                   		
    buckets_list_of_dicts = s3_client.list_buckets()['Buckets']
    buckets_list = [ bucket["Name"] for bucket in buckets_list_of_dicts ]
    return buckets_list

