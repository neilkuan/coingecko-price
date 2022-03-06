from typing import Dict
from pycoingecko import CoinGeckoAPI

def pair(cost, sell):
    if cost > sell:
        return f'賠{cost - sell} TWD'
    elif cost < sell:
        return f'賺{sell - cost} TWD'

def now_price(token: Dict):
    for k in token.keys():
       key_name = k
    return f'{str(key_name).upper()} now price is: {token.get(key_name)}'
def run():
    cg = CoinGeckoAPI()
    gst = cg.get_price(ids='gst', vs_currencies=['usd','twd'])
    solana = cg.get_price(ids='solana', vs_currencies=['usd','twd'])

    print(f'''
    {now_price(gst)}
    {now_price(solana)}
    兩雙 mint 0 灰鞋👟 成本{200*float(gst.get('gst').get('twd'))}
    mint 到 Runner 可以賣 10.3 sol {10.3 * float(solana.get('solana').get('twd'))}
    {pair(200*int(gst.get('gst').get('twd')), 10.3 * float(solana.get('solana').get('twd')))}
    ''')


if __name__ == '__main__':
    run()