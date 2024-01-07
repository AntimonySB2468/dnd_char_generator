import dice


def get_ability_scores(order: list) -> dict:
    my_scores = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

    temp_lst = []

    for i in range(6):
        temp_lst.append(dice.roll_stats())

    temp_lst.sort()

    for ability in order:
        score = temp_lst.pop()
        my_scores[ability] = score

    return my_scores


def get_mod(score: int) -> int: return (score - 10) // 2


def get_ability_mods(ability_scores: dict) -> dict:
    my_mods = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

    for key in ability_scores.keys():
        my_mods[key] = get_mod(ability_scores[key])

    return my_mods


def get_saving_throws(mods: dict, bonus: int, proficiencies: list) -> dict:
    """Return a dictionary with the saving throw modifiers of the character."""

    saving_throws = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

    for save in saving_throws.keys():
        saving_throws[save] = mods[save]

    for proficiency in proficiencies:
        saving_throws[proficiency] += bonus

    return saving_throws


def get_skills(mods: dict, bonus: int, proficiencies: list) -> dict:
    skills = {
        "Acrobatics": 0,
        "Animal Handling": 0,
        "Arcana": 0,
        "Athletics": 0,
        "Deception": 0,
        "History": 0,
        "Insight": 0,
        "Intimidation": 0,
        "Investigation": 0,
        "Medicine": 0,
        "Nature": 0,
        "Perception": 0,
        "Performance": 0,
        "Persuasion": 0,
        "Religion": 0,
        "Sleight of Hand": 0,
        "Stealth": 0,
        "Survival": 0
    }

    strength_skills = ['Athletics']
    dexterity_skills = ['Acrobatics', 'Sleight of Hand', 'Stealth']
    intelligence_skills = ['Arcana', 'History', 'Investigation', 'Nature', 'Religion']
    wisdom_skills = ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival']
    charisma_skills = ['Deception', 'Intimidation', 'Performance', 'Persuasion']

    for skill in strength_skills:
        skills[skill] = mods['Strength']
    for skill in dexterity_skills:
        skills[skill] = mods['Dexterity']
    for skill in intelligence_skills:
        skills[skill] = mods['Intelligence']
    for skill in wisdom_skills:
        skills[skill] = mods['Wisdom']
    for skill in charisma_skills:
        skills[skill] = mods['Charisma']

    for skill in proficiencies:
        skills[skill] += bonus

    return skills