# AWS OpenSearch Queries

This is a Python project allow request queries to AWS OpenSearch. The queries have to follow the AWS OpenSearch Queries structure and have to be in a external file (e.g. query.json). 

## Dependencies

You can install the package using pip:

```bash
pip install opensearchpy
pip install boto3
```

## Environment Preparation
- Create the enviroment
  ```
  py -m venv <name_of_virtualenv>
  ```
- Activate the enviroment
  ```
  .\<name_of_virtualenv>\Scripts\activate
  ```
- Install libraries
  ```
  (<name_of_virtualenv>) py -m pip install -r requirements.txt
  ```
- Deactivate the enviroment (when the application finish)
  ```
  deactivate
  ```

## Usage

To use the script, you have to provide some arguments:

- `--region`: Set the AWS Region.
- `--domain`: Set the Open Search Domain.
- `--port`: Set th Open Search port.
- `--index`: Set the index name into the opensearch domain.
- `--file`: File path and name (query).
- `--log`: Set log file name to save the result in top a log file.

```bash
py ./openSearch.py -r us-west-1 -d my-domain-com -p 443 -i index-name -f query.json -l logger 
```

## Query Examples

Here is a query example:

```json
{
    "_source": [
        "property-name"
    ],
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "first-name": "Pedro"
                    }
                }
            ],
            "filter": [
                {
                    "range": {
                        "age": {
                            "gte": 18
                        }
                    }
                }
            ]
        }
    }
}
```

## Directory Hierarchy
```
|—— openSearch.py
|—— requirements.txt
|—— README.md
|—— .gitignore
```

## Code Details
### Tested Platform
- Software
  ```
  Python: 3.11.1
  ```

## References
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- [opensearchpy](https://pypi.org/project/opensearch-py/)