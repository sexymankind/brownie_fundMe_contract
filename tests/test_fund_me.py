from brownie import network, accounts, exceptions
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundMe
import pytest
#Basic running test of a simple entrance and exit of a bit of eth
def test_can_FundAndWithdraw():
    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     pytest.skip("only for local testing")
    account = get_account()
    account2 = accounts[1]
    fund_me = deploy_fundMe()
    entrance_fee = fund_me.getEntranceFee()*10
    
    tx= fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmntFounded(account.address) == entrance_fee
    tx2= fund_me.fund({"from": account2, "value": entrance_fee})
    tx2.wait(1)
    assert fund_me.addressToAmntFounded(account2.address) == entrance_fee
   
    tx3= fund_me.withdraw({"from": account})
    tx3.wait(1)
    assert fund_me.addressToAmntFounded(account.address) == 0

def test_balance_equal_to_total_sum():
    account = get_account()
    account2 = accounts[1]
    fund_me = deploy_fundMe()
    balance = (fund_me.addressToAmntFounded(account.address)
     + fund_me.addressToAmntFounded(account2.address))
    tx_bl= fund_me.balance()
    assert tx_bl == balance

def test_only_owner_casher():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    bad_boy = accounts[1]
    fund_me = deploy_fundMe()
    # fund_me.withdraw({"from": bad_boy})
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_boy})

