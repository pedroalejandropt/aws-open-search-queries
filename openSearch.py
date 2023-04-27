from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import argparse
import boto3
import json

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-p", "--port", help = "Set Port")
parser.add_argument("-d", "--domain", help = "Set Domain")
parser.add_argument("-r", "--region", help = "Set Region")
parser.add_argument("-i", "--index", help = "Set Index")
parser.add_argument("-f", "--file", help = "JSON File with Query")
parser.add_argument("-l", "--log", help = "Set Log Filename & Return it")
 
# Read arguments from command line
args = parser.parse_args()
print(args)

if args.domain == None:
    print('You should provided a domain.\n')
    exit()
if args.port == None:
    print('You should provided a port.\n')
    exit()
if args.index == None:
    print('You should provided a index name.\n')
    exit()
if args.file == None:
    print('You should provided a json file.\n')
    exit()
if args.region == None:
    print('Using Default Region (us-west-1).\n')

json_file_name = args.file
# Cluster Endpoint, Example: my-test-domain.us-east-1.es.amazonaws.com
host = args.domain
# Port, Example: 443, 9443, ...
port = args.port
# Region, Example: us-west-1, us-west-2, eu-west-1, eu-west-2, ...
region = args.region if args.region else 'eu-west-2'
log_file_name = args.log

credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)
index_name = args.index if args.index else  'example-index'

client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

# Opening JSON file
json_file = open(json_file_name)
query = json.load(json_file)

response = client.search(
    body = query,
    index = index_name
)

json_result = json.dumps(response, sort_keys=True, indent=4)

print('Results:\n')
print(json_result)

if args.log == None:
    f = open(log_file_name + '.txt', "w")
    f.write("{0}\n".format(json_result))
    f.close()