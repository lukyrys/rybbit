import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

translations = {
    'cs.json': {
        'rd5F5r': 'Individuální plán',
        '5/hIKX': 'Limity plánu',
        'BdV5Om': 'Weby',
        'HCYBYT': 'Členové týmu',
    },
    'zh.json': {
        'rd5F5r': '自定义计划',
        '5/hIKX': '计划限制',
        'BdV5Om': '网站',
        'HCYBYT': '团队成员',
    },
    'ja.json': {
        'rd5F5r': 'カスタムプラン',
        '5/hIKX': 'プランの制限',
        'BdV5Om': 'ウェブサイト',
        'HCYBYT': 'チームメンバー',
        'u9xEkD': '© {year} Rybbit. 全著作権所有。',
    },
    'de.json': {
        'rd5F5r': 'Benutzerdefinierter Plan',
        '5/hIKX': 'Plan-Limits',
        'BdV5Om': 'Websites',
        'HCYBYT': 'Teammitglieder',
    },
    'pl.json': {
        'rd5F5r': 'Plan niestandardowy',
        '5/hIKX': 'Limity planu',
        'BdV5Om': 'Strony internetowe',
        'HCYBYT': 'Członkowie zespołu',
    },
    'pt.json': {
        'rd5F5r': 'Plano personalizado',
        '5/hIKX': 'Limites do plano',
        'BdV5Om': 'Sites',
        'HCYBYT': 'Membros da equipe',
    },
    'it.json': {
        'rd5F5r': 'Piano personalizzato',
        '5/hIKX': 'Limiti del piano',
        'BdV5Om': 'Siti web',
        'HCYBYT': 'Membri del team',
    },
    'fr.json': {
        'rd5F5r': 'Plan personnalisé',
        '5/hIKX': 'Limites du plan',
        'BdV5Om': 'Sites web',
        'HCYBYT': "Membres de l'équipe",
    },
    'ko.json': {
        'rd5F5r': '맞춤 플랜',
        '5/hIKX': '플랜 한도',
        'BdV5Om': '웹사이트',
        'HCYBYT': '팀 멤버',
        'u9xEkD': '© {year} Rybbit. 모든 권리 보유.',
    },
    'es.json': {
        'rd5F5r': 'Plan personalizado',
        '5/hIKX': 'Límites del plan',
        'BdV5Om': 'Sitios web',
        'HCYBYT': 'Miembros del equipo',
    },
}

with open(BASE_DIR / 'en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

en_key_order = list(en.keys())

for fname, updates in translations.items():
    file_path = BASE_DIR / fname
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, value in updates.items():
        if key in data:
            data[key] = value

    ordered = {}
    for key in en_key_order:
        if key in data:
            ordered[key] = data[key]
    for key in data:
        if key not in ordered:
            ordered[key] = data[key]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f'Updated {fname}')

print('Done!')
