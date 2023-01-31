DuneGraf
=======================

* [Uniswap ERC20 transfers graph on Ethereum](https://soispoke.github.io/DuneGraf/example/large-graph/) ([source](https://github.com/soispoke/DuneGraf/blob/main/example/large-graph/index.html)) A web component to represent a graph data structure in a 3-dimensional space for Uniswap transfers on Ethereum last week, collected via the Dune API.

* Once you click on a page, navigate in the 3D graph, zoom in/out, drag nodes and explore!

Each edge represents an ERC20 transfer, and you can click on Nodes to get redirected to the [Etherscan](https://etherscan.io/) page of their corresponding 
address.

Notice how nodes are colored based their label category (MEV, Exchange, Contract, etc...)

* To choose another blockchain, token address, or a different time period to analyse, modify the following parameters in the ([main.py script](https://github.com/soispoke/DuneGraf/blob/main/main.py)):   `blockchain`, `address`, `start_date`, `end_date`


