from eth_account import Account

def generate_and_check() -> None:
    Account.enable_unaudited_hdwallet_features()
    acct, mnemonic = Account.create_with_mnemonic()

    print(f'Address: {acct.address}\n'
          f'Private Key: {acct.key.hex()}\n'
          f'Mnemonic: {mnemonic}')

    with open(file='evm_wallets.txt', mode='a', encoding='utf-8-sig') as file:
        file.write(f'{acct.address}:{acct.key.hex()}:{mnemonic}\n')


if __name__ == '__main__':
    count: int = input('How many wallets: ')

    print('Generating addresses...\n')

    for i in range(0, int(count)):
        generate_and_check()
