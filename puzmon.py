import random

ELEMENT_SYMBOLS = {
    '火': '$', '水': '~', '風': '@', '土': '#', '命': '&', '無': ' '
}
ELEMENT_COLORS = {
    '火': 1, '水': 6, '風': 2, '土': 3, '命': 5, '無': 7
}

def main():
    friends = [
        {'name': '青龍', 'hp': 150, 'max_hp': 150, 'element': '風', 'ap': 15, 'dp': 10},
        {'name': '朱雀', 'hp': 150, 'max_hp': 150, 'element': '火', 'ap': 25, 'dp': 10},
        {'name': '白虎', 'hp': 150, 'max_hp': 150, 'element': '土', 'ap': 20, 'dp': 5},
        {'name': '玄武', 'hp': 150, 'max_hp': 150, 'element': '水', 'ap': 20, 'dp': 15}
    ]
    monster_list = [
        {'name': 'スライム', 'hp': 100, 'max_hp': 100, 'element': '水', 'ap': 10, 'dp': 1},
        {'name': 'ゴブリン', 'hp': 200, 'max_hp': 200, 'element': '土', 'ap': 20, 'dp': 5}
    ]
    player_name = input('プレイヤー名を入力してください>> ')
    print('*** Puzzle & Monsters ***')
    party = organize_party(player_name, friends)
    kills = go_dungeon(party, monster_list)
    print(f'倒したモンスター数={kills}')

def organize_party(player_name, friends):
    total_hp = sum(friend['hp'] for friend in friends)
    total_dp = sum(friend['dp'] for friend in friends) / len(friends)
    return {'name': player_name, 'friends': friends, 'hp': total_hp, 'max_hp': total_hp, 'dp': total_dp}

def go_dungeon(party, monster_list):
    kills = 0
    print(f'{party["name"]}のパーティ(HP={party["hp"]})はダンジョンに到着した')
    show_party(party)
    for monster in monster_list:
        show_battlefield(party, monster)
        kills += do_battle(party, monster)
        if party['hp'] <= 0:
            print(f'{party["name"]}はダンジョンから逃げ出した')
            break
        print(f'{party["name"]}はさらに奥に進んだ')
    return kills

def do_battle(party, monster):
    print(f'【{party["name"]}のターン(HP={party["hp"]})】')
    show_battlefield(party, monster)
    
    command = input('コマンド?>> ')
    if command:
        damage = sum(friend['ap'] for friend in party['friends']) - monster['dp']
        monster['hp'] = max(monster['hp'] - damage, 0)
        print(f'{monster["name"]}に{damage}のダメージを与えた')
    
    if monster['hp'] > 0:
        print(f'【{monster["name"]}のターン(HP={monster["hp"]})】')
        enemy_damage = max(monster['ap'] - party['dp'], 1)
        party['hp'] = max(party['hp'] - enemy_damage, 0)
        print(f'敵の攻撃！ {enemy_damage}のダメージを受けた')
        if party['hp'] <= 0:
            print(f'{party["name"]}は倒れた...')
            return 0
    else:
        print(f'{monster["name"]}を倒した！')
        return 1

def show_battlefield(party, monster):
    print(f'バトルフィールド')
    print(f'{monster["name"]} HP = {monster["hp"]} / {monster["max_hp"]}')
    show_party(party)
    print('----------------------------')
    show_puzzle_board()

def show_party(party):
    print(f'【{party["name"]}のパーティ】 HP = {party["hp"]} / {party["max_hp"]}')
    for friend in party['friends']:
        print(f'{friend["name"]} (HP={friend["hp"]}, 攻撃={friend["ap"]}, 防御={friend["dp"]})')

def show_puzzle_board():
    elements = ['火', '水', '風', '土']
    board = [[random.choice(elements) for _ in range(6)] for _ in range(5)]
    print('  A B C D E F')
    for row in board:
        print(' '.join(ELEMENT_SYMBOLS[e] for e in row))

if __name__ == '__main__':
    main()
