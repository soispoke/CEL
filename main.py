#! /usr/bin/env python3
import readline
import dotenv
import os
import json
import sys

from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import Query

lines = sys.stdin.readlines()
data = json.loads(lines[0])

blockchain = data[0]
address = data[1]
start_date = data[2]
end_date = data[3]

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
results_nodes = dune.parse(dune.refresh(query_nodes),'nodes')
results_links = dune.parse(dune.refresh(query_links),'links')
parsed = results_nodes.copy()
parsed.update(results_links)
dune.save(parsed)