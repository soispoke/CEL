import dotenv
import os
import json

from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import Query

blockchain = "bnb"
address = "0x0d8ce2a99bb6e3b7db580ed848240e4a0f9ae153"
start_date = "2021-06-01 00:00:00"
end_date = "2021-06-25 21:08:00"

query_nodes = Query(
    name="Query Nodes",
    query_id=1302730,
    params=[
            QueryParameter.enum_type(name="Blockchain", value=blockchain),
            QueryParameter.text_type(name="Address", value=address),
            QueryParameter.date_type(name="Start Date", value=start_date),
            QueryParameter.date_type(name="End Date", value=end_date)
    ]
)

query_links = Query(
    name="Query Links",
    query_id=1304311,
    params=[
            QueryParameter.enum_type(name="Blockchain", value=blockchain),
            QueryParameter.text_type(name="Address", value=address),
            QueryParameter.date_type(name="Start Date", value=start_date),
            QueryParameter.date_type(name="End Date", value=end_date)
    ]
)

print("Results available at", query_nodes.url(), query_links.url())

dotenv.load_dotenv()
dune = DuneClient(os.environ["DUNE_API_KEY"])
results_nodes = {"nodes": dune.refresh(query_nodes).result.rows} 
results_links =  {"links": dune.refresh(query_links).result.rows} 

parsed = {**results_nodes, **results_links}
with open('example/datasets/blockchain_data.json', 'w') as f:
    json.dump(parsed, f)