def get_level(xp: int) -> int:
    if xp < 300:
        level = 1
    elif xp < 900:
        level = 2
    elif xp < 2700:
        level = 3
    elif xp < 6500:
        level = 4
    elif xp < 14000:
        level = 5
    elif xp < 23000:
        level = 6
    elif xp < 34000:
        level = 7
    elif xp < 48000:
        level = 8
    elif xp < 64000:
        level = 9
    elif xp < 85000:
        level = 10
    elif xp < 100000:
        level = 11
    elif xp < 120000:
        level = 12
    elif xp < 140000:
        level = 13
    elif xp < 165000:
        level = 14
    elif xp < 195000:
        level = 15
    elif xp < 225000:
        level = 16
    elif xp < 265000:
        level = 17
    elif xp < 305000:
        level = 18
    elif xp < 355000:
        level = 19
    else:
        level = 20

    return level


def get_prof_bon(level: int) -> int:
    from math import ceil
    return ceil(1 + (level / 4))


def calculate_max_capacity(strength: int, size: str = 'normal'):
    WEIGHT: int = 15

    num = WEIGHT * strength

    if size == 'tiny':
        num *= 0.5
    elif size == 'large':
        num *= 2
    elif size == 'huge':
        num *= 4
    elif size == 'gargantuan':
        num *= 8

    return num


def determine_HP():
    return "WiP"


class HitDie:
    def __init__(self, die: int, num: int = 1):
        self.num = num
        self.dice = die

    def __str__(self):
        return "{}d{}".format(self.num, self.dice)

WIP = "aadhya u dumbass"

class Character:
    def __init__(self,
                 player_name: str, chara_name: str, class_lvl: dict, race: str, background: str, alignment: str, xp: int,
                 ability_scores: dict, ability_mods: dict, saving_throws: dict, skills: dict,
                 armor: str, speed: str, temp_hp: str, hit_dice: int, attacks_spellcasting: str,
                 traits: list, ideals: list, bonds: list, flaws: list,
                 features_traits: list, proficiencies: list, languages: list, equipment: list,
                 size: str, age: int, insp: bool):

        self.chara_name = chara_name

        self.class_lvl = class_lvl
        self.background = background
        self.player_name = player_name
        self.race = race
        self.alignment = alignment
        self.xp = xp
        self.total_level = get_level(xp)

        self.ability_scores = ability_scores
        self.ability_mods = ability_mods

        self.saving_throws = saving_throws
        self.skills = skills
        self.prof_bon = get_prof_bon(self.total_level)
        self.insp = insp

        self.armor_class = armor + ability_mods["DEX"]
        self.initiative = ability_mods["DEX"]
        self.speed = speed

        self.max_hp = determine_HP()
        self.curr_hp = self.max_hp
        self.temp_hp = temp_hp

        self.hit_dice = HitDie(hit_dice, self.total_level)
        self.death_saves = {"successes": 0, "failures": 0}

        self.attacks_spellcasting = attacks_spellcasting

        self.traits = traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws

        self.features_traits = features_traits

        self.proficiencies = proficiencies
        self.languages = languages

        self.equipment = equipment
        self.max_capacity = calculate_max_capacity(ability_scores["STR"], size)

        self.age = age
        self.height = WIP
        self.weight = WIP
        self.eyes = WIP
        self.skin = WIP
        self.hair = WIP
        self.backstory = WIP

        if self.class_lvl




# def generate_character(player_name, character_name, dnd_class, dnd_race, )
