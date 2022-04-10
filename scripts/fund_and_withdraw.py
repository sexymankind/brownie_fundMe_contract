from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    # if we already have a FundMe deployed in whatever other network we are on, we need the last one
        #used by the current NETWROK THATS WE ARE ON THE LAST FundMe THAT WAS DEPLOYED
        #  ITS IMPORTANT CAUSE ITS THE LAST CONTRACT FundMe 
        #THAT WAS USED [-1]
    fund_contract = FundMe[-1]
    account = get_account()
    entrance_fee = fund_contract.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    fund_contract.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_contract = FundMe[-1]
    account= get_account()
    fund_contract.withdraw({"from": account})
    

def main():
    fund()
    withdraw()