from brownie import accounts, network, config, MockV3Aggregator
MAINNETFORK_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS= 8
INIT_VALUE= 2000*10**8

def get_account():
    account_cli_ui = accounts[0]
    account_infura = accounts.add(config["wallets"]["from_key"])
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in MAINNETFORK_ENVIRONMENTS:
        return account_cli_ui
    else:
        return account_infura


 # if we already have a M3Agg deployed in whatever other network we are on, we need the last one
        #used by current NETWROK THATS WHY WE USE THE LAST M3Agg THAT WAS DEPLOYED
        #  ITS IMPORTANT CAUSE ITS THE LAST CONTRACT M3Agg 
        #THAT WAS USED
def get_MockV3Aggregator():
    account = get_account()
    #Im not really sure of what this does 100% exactly
    if len(MockV3Aggregator) <=0:
        print(f"The active network is: {network.show_active()}")
        print("Deploying Mock...")
        MockV3Aggregator.deploy(DECIMALS, INIT_VALUE, {"from": account})
        print("Mock Deployed!")
        
    