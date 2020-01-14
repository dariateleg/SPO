import web3
from web3 import Web3
import numpy as np
import matplotlib.pyplot as plt

def transactionsFeeAndContracts(block, web3):
    feesSum = 0
    contracts = 0
    for transaction in block.transactions:
        tr = web3.eth.getTransaction(transaction)
        feesSum += web3.eth.getTransactionReceipt(transaction).gasUsed * tr.gasPrice * 1e-18
        if tr.input != '0x':
            contracts+=1
    return feesSum, contracts

def plot(x, y, name, Color, Ylabel):
    Fig = plt.figure(figsize=(30, 10))
    ax = Fig.add_subplot()
    ax.set(title=name, xlabel="Block's count", ylabel=Ylabel)
    ax.tick_params(axis='x', labelrotation=90, pad=10)
    ax.plot(x, y, color=Color, linewidth=0.8)
    ax.scatter(x, y, color=Color, s=6)
    Fig.savefig(name + '.png')


def main():
    fb, lb = 8960400, 8960500
    #8961400 - 1000 * (2 - 1)  # first block, last block
    commissionPercentage = []
    commission_block = []  # commission for each block
    reward_block = []  # reward for each block
    contracts_block = [] # contracts for each block
    web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/c2709fa8cb054278bd6aa385ee1bc381"))  # Connection via Infura
    numberOfBlock = []
    for blockNumber in range(fb, lb):
        block = web3.eth.getBlock(blockNumber)  # Current block
        fee, contracts = transactionsFeeAndContracts(block, web3)
        contracts_block.append(contracts)
        numberOfBlock.append(blockNumber)
        reward_block.append(2 + fee + 2 * len(block.uncles) / 32)
        commission_block.append(fee)
        print(commission_block[len(commission_block)-1], " ", reward_block[len(reward_block) - 1], " ", blockNumber)
        commissionPercentage.append(commission_block[len(commission_block) - 1] / reward_block[len(reward_block) - 1] * 100)

    MX = np.mean(commission_block)  # мат ожидание
    DX = np.var(commission_block)  # дисперсия
    Me = np.median(commission_block)  # медиана
    Range = np.ptp(commission_block)  # размах
    Sigma = np.sqrt(DX)  # среднеквадрат. отклонение

    plot(numberOfBlock, commissionPercentage, 'Relative_commission_for_each_block', 'green', 'Fee, %')
    plot(numberOfBlock, commission_block, 'Abcolute_Commission_for_each_block', 'orange', 'Fee, ETH')
    plot(numberOfBlock, reward_block, 'Reward_for_each_block', 'blue', 'Reward, ETH')
    plot(numberOfBlock, contracts_block, 'Smart_contracts_count_for_each_block', 'red', 'Smart contracts')

    print('MX= ', MX, '\nDX= ', DX, '\nMe= ', Me, '\nРазмах= ', Range, '\nδ= ', Sigma)

main()
