CATEGORIES = {
    'КОНДИЦИОНЕРЫ': 'katalog/kondicionery/',
    'СМАРТФОНЫ': 'katalog/telefony/',
    'ХОЛОДИЛЬНИКИ': 'katalog/holodilniki/',
    'НОУТБУКИ': 'katalog/noutbuki/'
}


def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v