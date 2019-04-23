import boto3, requests, json, sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

clientops = boto3.client(
        'opsworks',
        region_name='sa-east-1',
        aws_access_key_id='AKIAJ56G3BAGOLBQW3SQ',
        aws_secret_access_key='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'
)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# OpenAM authenticate integration
try:
   OamUrl = "https://extranethml2.unimedbh.com.br/openam/json/"
   headers = {"X-OpenAM-Username": "uni13477", "X-OpenAM-Password": "T3hil1m128", "Content-Type": "application/json"}
   response = requests.post(OamUrl + 'authenticate', headers=headers, verify=False)
   tokenid = json.loads(response.text)['tokenId']
except:
   print("credentials, ERROR.: \n")
   print(response.text)
   sys.exit(2)
