from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import(
    get_account, 
    get_MockV3Aggregator, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
    )

def deploy_fundMe():
    account = get_account()
    #PriceFeed address to our contract
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        prc_feed_add= config["networks"][network.show_active()]["eth_usd_"]
    else:
        
         # if we already have a M3Agg deployed in whatever other network we are on, we need the last one
        #used by current NETWROK THATS WHY WE USE THE LAST M3Agg THAT WAS DEPLOYED
        #  ITS IMPORTANT CAUSE ITS THE LAST CONTRACT M3Agg 
        #THAT WAS USED
        get_MockV3Aggregator()
        prc_feed_add = MockV3Aggregator[-1].address
        
        #Este es el contrato donde ya es implementado con todas las funciones que contiene dentro
        #donde le pasamos como atributo el pricefeed actual del ETHSUSD PORQUE POR DEFAULT ESTABA
        #EL QUE SE USA CON UNA TESTNET THE RINKBY SI LO QUEREMOS CAMBIAR DEPENDIENDO DE LA RED
        # ES POR ESO QUE NECESITAMOS #AGREGAR EL PRECIO CORRECTO DEPENDIENDO 
        # DE LA RED EN LA QUE SE ENCUENTRE
    contract_fundMe= FundMe.deploy(
        prc_feed_add, 
        {"from": account}, 
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    return contract_fundMe
    #agregar una f en print es que vas a declarar una funcion dentro
    
    

def main():
    deploy_fundMe()