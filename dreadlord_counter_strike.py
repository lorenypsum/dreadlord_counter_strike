from datetime import datetime
from enum import Enum, auto
from random import randrange
from time import sleep
from typing import Optional, Tuple


class GameItem(Enum):
    DEATH = auto()
    WOODEN_SWORD = auto()
    SIMPLE_BOW = auto()
    VIOLIN = auto()
    ORDINARY_SWORD = auto()
    STRAHD_SLAYER_SWORD = auto()
    STRAHD_SLAYER_BOW = auto()


class GameStatus(Enum):
    ALIVE = auto()
    DEAD = auto()
    ARREGAO = auto()
    WINNER = auto()
    HAHA = auto()


def ask_if_yes(input_text: str) -> bool:
    """
    This function asks the player a question,
    and returns True if they typed yes,
    or False if they typed anything else.
    """
    return input(input_text).lower() in ["y", "yes", "s", "sim"]


def ask_if_wanna_continue(player_name: str) -> bool:
    """
    This function asks the player if they want to continue the game,
    and returns the answer.
    """
    print("You reached one possible end!!!")
    if ask_if_yes("Wanna change your fate? "):
        sleep(2)
        print("Very well then...")
        sleep(2)
        return True
    else:
        if ask_if_yes(f"{player_name} did you find the treasure I prepared for you? "):

            print("Congratulations, you may leave now!!!")
            sleep(1)
        else:
            print("What a shame! you broke my heart :'(")
            sleep(1)
        return False


def roll_for_item(player_name: str) -> Tuple[Optional[GameItem], GameStatus]:
    """
    This function rolls the dice for the player.
    It returns the item that the player gained (if any),
    and the status of the player after the roll.
    """
    roll = randrange(1, 20)
    if player_name.lower() == "lurin":
        print(f"You rolled {roll}!")
        sleep(2)
        if ask_if_yes("Since you are inspired... wanna roll again? "):
            sleep(2)
            roll = randrange(1, 20)
            print(f"Now your roll was {roll}")
    if roll == 1:
        print(f"HAHAHAHAHA, tragic! You got {roll}")
        sleep(2)
        if player_name.lower() != "lurin":
            print(
                f"Unfortunalety {player_name}, you are not Lurin, so you do not have another chance!!!"
            )
            sleep(4)
        else:
            print(
                f"Unfortunalety fake {player_name}, even inspired you got it? You are a joke!!!"
            )
            sleep(4)
            return None, GameStatus.DEAD
            
        if player_name.lower() == "snow":
            print(f"... you may have this *WONDERFUL DEATH* to help you kill STRAHD...")
            sleep(3)
            print("...the perfect item for you, huh?")
            sleep(2)
            print("...no, it is not a typo or some faulty logic!")
            sleep(2)
            print(
                "It is indeed the perfect item for you... you will play dead (you are used to it)... STRAHD flew away..."
            )
            sleep(4)
            return GameItem.DEATH, GameStatus.ALIVE
        else:
            print(
                f"Well {player_name}, you may have this *DEATH* to help you kill STRAHD..."
            )
            sleep(3)
            print("...since you are not SNOW....")
            sleep(2)
            print("...no, it is not a typo or some faulty logic!")
            sleep(2)
            print("...you are DEAD!")
            sleep(2)
            print("***Bad end!***")
            sleep(1)
            return None, GameStatus.DEAD
    elif roll <= 5:
        print(f"You got {roll}")
        if player_name.lower() != "kaede":
            print(
                f"Well {player_name}, you may have this *VIOLIN* to help you kill STRAHD..."
            )
            sleep(3)
            print("...since you are not KAEDE.... gooood luck!")
            sleep(2)

            return GameItem.VIOLIN, GameStatus.ALIVE
        else:
            print(f"Well {player_name}, you may have this ***WONDERFUL VIOLIN***")
            sleep(3)
            print("the perfect item for you, huh?")
            sleep(2)
            return GameItem.VIOLIN, GameStatus.ALIVE
    elif roll <= 10:
        print(f"You got {roll}")
        if player_name.lower() != "soren":
            print(
                f"Well {player_name}, you may have this *SIMPLE BOW* to help you kill STRAHD..."
            )
            sleep(3)
            print("...since you are not Soren... gooood luck!")
            sleep(2)
            return GameItem.SIMPLE_BOW, GameStatus.ALIVE
        else:
            print(f"Well {player_name}, you may have this ***WONDERFUl SIMPLE BOW***")
            sleep(3)
            print("the perfect item for you, huh?")
            sleep(2)
            print("just.. do not kill any cats with this, moron!!!")
            sleep(2)
            return GameItem.SIMPLE_BOW, GameStatus.ALIVE
    elif roll <= 15:
        print(f"You got {roll}")
        if player_name.lower() != "vis":
            print(
                f"Well {player_name}, you may have this *ORDINARY SWORD* to help you kill STRAHD..."
            )
            sleep(3)
            print("...since you are not Vis... gooood luck!")
            sleep(2)
            print("and pray it won't fly...")
            sleep(2)
            return GameItem.ORDINARY_SWORD, GameStatus.ALIVE
        else:
            print(
                f"Well {player_name}, you may have this ***FANTASTIC ORDINARY SWORD*** to help you kill STRAHD"
            )
            sleep(3)
            print("the perfect item for you, huh?")
            sleep(2)
            print("if it doesn't fly...")
            sleep(2)
            return GameItem.ORDINARY_SWORD, GameStatus.ALIVE
    elif roll < 20:
        print(f"You got {roll}")
        sleep(2)
        print(
            f"Well {player_name}, you may have ****STRAHD SLAYER SWORD***, go kill STRAHD, "
        )
        sleep(3)
        print("...the legendary item!!!")
        sleep(2)
        print("...but hope it won't fly!!!")
        sleep(2)
        return GameItem.STRAHD_SLAYER_SWORD, GameStatus.ALIVE
    elif roll == 20:
        if player_name.lower() != "snow":
            print(
                f"Well {player_name}, you may have **** STRAHD SLAYER BOW***, go kill STRAHD, special treasures awaits you!!!"
            )
            sleep(3)
            print("...the legendary perfect item!!!")
            sleep(2)
            print("...it doesn't even matter if it will fly!!!")
            sleep(2)
            return GameItem.STRAHD_SLAYER_BOW, GameStatus.ALIVE
        else:
            print(
                f"Well {player_name}, you seduced STRAHD, now you can claim your treasures"
            )
            sleep(2)
            print(f"STRAHD licks you!!!")
            sleep(4)
            return GameItem.STRAHD_SLAYER_BOW, GameStatus.ALIVE
    return None, GameStatus.ALIVE


def flee(player_name: str) -> GameStatus:
    """
    This function asks the player if they want to flee.
    It returns the status of the player after their decision to flee.
    """
    if ask_if_yes("Wanna flee now? "):
        sleep(2)
        print("...")
        sleep(1)
        print("We will see if flee you can... *** MUST ROLL THE DICE ***: ")
        sleep(2)
        print("Careful!!!")
        sleep(1)
        roll_the_dice = input(
            "*** Roll stealth *** (if you type it wrong it means you were not stealth) type: 'roll stealth' "
        )
        sleep(4)
        if roll_the_dice == "roll stealth":
            roll = randrange(1, 20)
            if roll <= 10:
                print(f"you rolled {roll}!")
                sleep(2)
                print("It means STRAHD noticed you!")
                sleep(2)
                print("...")
                sleep(2)
                print(" You are dead!!! ")
                sleep(2)
                print(" ***Bad end...*** ")
                sleep(1)
                return GameStatus.DEAD
            else:
                print(f"you rolled {roll}!!!")
                sleep(2)
                print("Congratulations, you managed to be stealth!!!")
                sleep(2)
                print("...")
                sleep(2)
                print("You may flee but you will continue being poor and weak...")
                sleep(2)
                print("...")
                sleep(2)
                print(
                    "And remember there are real treasures waiting for you over there..."
                )
                sleep(4)
                print("***Bad end...***")
                sleep(1)
                return GameStatus.ARREGAO
        else:
            if player_name.lower() in ["soren", "kaede", "leandro", "snow", "lurin"]:
                print("...")
                sleep(1)
                print("......")
                sleep(2)
                print("...........")
                sleep(2)
                print("I told you to be careful!")
                sleep(2)
                print(f"...{player_name} you are such a DOJI!!!")
                sleep(2)
                print("It means the STRAHD noticed you!")
                sleep(2)
                print("...")
                sleep(2)
                print(" You are dead!!! ")
                sleep(2)
                print(" ***Bad end...*** ")
                sleep(1)
            else:
                print("I told you to be careful!")
                sleep(2)
                print("...........")
                sleep(2)
                print(f"...{player_name} you are such a klutz!!!")
                sleep(2)
                print("It means STRAHD noticed you!")
                sleep(2)
                print("...")
                sleep(2)
                print(" You are dead!!! ")
                sleep(2)
                print(" ***Bad end...*** ")
                sleep(1)
            return GameStatus.DEAD
    else:
        return GameStatus.ALIVE


def attack(player_name: str) -> Tuple[Optional[GameItem], GameStatus]:
    """
    This function asks the player if they want to attack STRAHD.
    If the player answers yes, the player rolls for an item.
    This function returns the item obtained by a roll (if any),
    and the status of the player.
    """
    print("You shall not pass!!!")
    if ask_if_yes(f"{player_name}, will you attack STRAHD? "):
        sleep(1)
        print("I honor your courage!")
        sleep(2)
        print("therefore...")
        sleep(1)
        print("I will help you...")
        sleep(1)
        print("I am giving you a chance to kill STRAHD and reclaim your treasures...")
        sleep(2)
        print(
            "Roll the dice and have a chance to win the perfect item for you... or even some STRAHD Slayer Shit!!!"
        )
        sleep(3)
        print("It will increase your chances...")
        sleep(2)
        print(
            "....or kill you right away if you are as unlucky as Soren using his Sharp Shooting!!!"
        )
        sleep(2)
        if ask_if_yes("Wanna roll the dice? "):
            return roll_for_item(player_name)
        else:
            if ask_if_yes("Are you sure? "):
                sleep(2)
                print("So you have chosen... Death!")
                sleep(2)
                return GameItem.DEATH, GameStatus.DEAD
            else:
                sleep(2)
                print("Glad you changed your mind...")
                sleep(2)
                print("Good... very good indeed...")
                sleep(2)
                return roll_for_item(player_name)
    else:
        print("If you won't attack STRAHD... then...")
        sleep(2)
        return None, flee(player_name)


def decide_if_strahd_flies(player_name: str) -> bool:
    """
    This function asks if the player wants to roll for stealth,
    which can give a chance for STRAHD not to fly.
    It returns whether STRAHD flies.
    """
    print(
        "This is your chance... STRAHD has his attention captived by his 'vampirish's business'..."
    )
    sleep(3)
    print("You are approaching him...")
    sleep(2)
    print("Careful...")
    sleep(2)
    print("Because vampires... can fly...")
    sleep(2)
    print("Roll stealth (if you type it wrong it means you were not stealth)...")
    roll_the_dice = input("type: 'roll stealth' ")
    sleep(2)
    if roll_the_dice == "roll stealth":
        roll = randrange(1, 20)
        if roll <= 10:
            print("...")
            sleep(1)
            print("Unlucky")
            sleep(2)
            print(f"You rolled {roll}")
            sleep(2)
            print("STRAHD...")
            sleep(2)
            print("...flew up")
            sleep(2)
            print("Now, you have a huge disavantage")
            sleep(2)
            return True
        else:
            print(f"You rolled {roll}")
            sleep(2)
            print("Congratulations, you managed to be in stealth!")
            sleep(2)
            return False
    else:
        if player_name.lower() in ["soren", "kaede", "leandro", "snow"]:
            print("...")
            sleep(1)
            print("......")
            sleep(2)
            print("...........")
            sleep(2)
            print("I told you to be careful!")
            sleep(2)
            print(f"...{player_name} you are such a DOJI, STRAHD flew up...")
            sleep(2)
            print("Now, you have a huge disavantage")
            sleep(2)
        else:
            print("...")
            sleep(1)
            print("......")
            sleep(2)
            print("...........")
            sleep(2)
            print("I told you to be careful!")
            sleep(2)
            print(f"...{player_name} you are such a KLUTZ, STRAHD flew...")
            sleep(2)
            print("...STRAHD flew up...")
            sleep(2)
            print("Now, you have a huge disavantage")
            sleep(2)
    return True


def calculate_win_probability(
    player_race: str, player_name: str, item: Optional[GameItem],strahd_flying: bool
) -> int:
    """
    This function returns the probability
    that the player defeats STRAHD.
    The probability depends on the item the player is holding,
    and whether STRAHD is flying.
    """
    if item == GameItem.DEATH:
        if player_name.lower() == "snow" and player_race.lower() == "kalashatar":
            return 90
        else:
            return 0
    elif item == GameItem.WOODEN_SWORD:
        if strahd_flying:
            return 5
        else:
            return 10
    elif item == GameItem.SIMPLE_BOW:
        if player_name.lower() == "soren" and player_race.lower() in [
            "human",
            "humano",
            "elf",
            "elfo",
        ]:
            return 70
        else:
            return 30
    elif item == GameItem.VIOLIN:
        if player_name.lower() == "kaede" and player_race.lower() == "tiefling":
            return 70
        else:
            return 30
    elif item == GameItem.ORDINARY_SWORD:
        if strahd_flying:
            return 10
        elif player_name.lower() == "vis" and player_race.lower() == "draconato":
            return 80
        else:
            return 40
    elif item == GameItem.STRAHD_SLAYER_SWORD:
        if strahd_flying:
            return 20
        else:
            return 100
    elif item == GameItem.STRAHD_SLAYER_BOW:
        return 100
    else:
        return -1


def roll_for_win(probability: int) -> bool:
    """
    This function returns whether the player defeats STRAHD,
    given a probability.
    """
    return randrange(100) <= probability


def after_battle(player_race: str, player_name: str, did_win: bool) -> GameStatus:
    """
    This function conducts the scenario
    after the player has defeated, or not, STRAHD.
    It returns the status depending on whether the player won.
    """
    if did_win:
        now = datetime.now()
        print("A day may come when the courage of men fails…")
        sleep(2)
        print("but it is not THIS day, SATAN...")
        sleep(2)
        print("Because... you approached STRAHD...")
        sleep(2)
        print("Almost invisible to his senses...")
        sleep(2)
        print(
            "Somehow your weapon hit the weak point of STRAHD's... revealing his true identity"
        )
        sleep(4)
        print(
            "He was just a bat... who looked like a DREADLORD..."
        )
        sleep(4)
        print("It was a huge battle...")
        sleep(2)
        print(
            f"And it was the most awkward {now.strftime('%A')} you will ever remember."
        )
        sleep(2)
        if (
            player_race.lower() in ["master", "mestre"]
            and player_name.lower() == "zordnael"
        ):
            print("...")
            sleep(1)
            print(
                "***************************************************************************************************************************************"
            )
            sleep(1)
            print(
                f"Congratulations {player_name}!!! You are the WINNER of this week's challenge, you shall receive 5000 dullas in Anastasia Dungeons Hills Cosmetics!"
            )
            sleep(4)
            print("link")
            sleep(5)
            print("***CHEATER GOOD END***")
            sleep(2)
            return GameStatus.WINNER
        elif player_race.lower() == "racist" and player_name.lower() == "lili":
            print("...")
            sleep(1)
            print(
                "***************************************************************************************************************************************"
            )
            sleep(1)
            print(
                f"Congratulations {player_name}!!! You are the WINNER of this week's challenge, you shall receive the prizes specially prepared for everybody in dullas from Anastasia Dungeons Hills Cosmetics!"
            )
            sleep(4)
            print("https://drive.google.com/drive/folders/1Jn8YYdixNNRqCQgIClBmGLiFFxuSCQdc?usp=sharing")
            sleep(5)
            print("***BEST END***")
            sleep(2)
            return GameStatus.WINNER
        if did_win:
            print("...")
            sleep(1)
            print(
                "***************************************************************************************************************************************"
            )
            sleep(1)
            if player_name.lower() == "soren":
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you received a cash prize of five thousand dullas from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print(f"And a prize... prepared specially for you {player_name}")
                sleep(2)
                print("... I know you doubted me... but here it is:")
                sleep(2)
                print("...")
                sleep(1)
                print("https://drive.google.com/drive/folders/1FerRt3mmaOm0ohSUXTkO-CmGIAluavXi?usp=sharing")
                sleep(5)
                print("...Your motherfuger cat killer !!!")
                sleep(2)
                print("***SOREN'S GOOD END***")
                sleep(2)
            elif player_name.lower() == "snow":
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you received a cash prize of five thousand dullas from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print(f"And a prize... prepared specially for you {player_name}")
                sleep(2)
                print("... I know you doubted me... but here it is:")
                sleep(2)
                print("...")
                sleep(1)
                print("https://drive.google.com/drive/folders/16STFQ-_0N_54oNNsVQnMjwjcBgubxgk7?usp=sharing")
                sleep(5)
                print("...Your motherfuger snow flake !!!")
                sleep(2)
                print("***SNOW'S GOOD END***")
                sleep(2)
            elif player_name.lower() == "kaede":
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you received a cash prize of five thousand dullas from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print(f"And a prize... prepared specially for you {player_name}")
                sleep(2)
                print("... I know you doubted me... but here it is:")
                sleep(2)
                print("...")
                sleep(1)
                print("https://drive.google.com/drive/folders/1XN9sItRxYR4Si4gWFeJtI0HGF39zC29a?usp=sharing")
                sleep(5)
                print("...Your motherfuger idol !!!")
                sleep(2)
                print("***KAEDE'S GOOD END***")
                sleep(2)
            elif player_name.lower() == "leandro":
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you received a cash prize of five thousand dullas from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print(f"And a prize... prepared specially for you {player_name}")
                sleep(2)
                print("... I know you doubted me... but here it is:")
                sleep(2)
                print("...")
                sleep(1)
                print("https://drive.google.com/drive/folders/1eP552hYwUXImmJ-DIX5o-wlp5VA96Sa0?usp=sharing")
                sleep(5)
                print("...Your motherfuger only roll 20 !!!")
                sleep(2)
                print("***LEANDRO'S GOOD END***")
                sleep(2)
            elif player_name.lower() == "vis":
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you received a cash prize of five thousand dullas from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print(f"And a prize... prepared specially for you {player_name}")
                sleep(2)
                print("... I know you doubted me... but here it is:")
                sleep(2)
                print("...")
                sleep(1)
                print("https://drive.google.com/drive/folders/1eP552hYwUXImmJ-DIX5o-wlp5VA96Sa0?usp=sharing")
                sleep(5)
                print("...Your motherfuger iron wall !!!")
                sleep(2)
                print("***VIS'S GOOD END***")
                sleep(2)
            elif player_name.lower() == "lurin":
                print("CONGRATULATIONS!!!!! ")
                sleep(2)
                print("Bitch! ... ")
                sleep(2)
                print(" ... you stole my name...")
                sleep(2)
                print("You are arrested for identity theft!!!")
                sleep(2)
                print("...")
                sleep(1)
                print("del C://LeagueOfLegends")
                sleep(2)
                print("...")
                sleep(0.5)
                print(".....")
                sleep(0.5)
                print("......")
                sleep(0.5)
                print(".............")
                sleep(2)
                print("deletion completed")
                sleep(2)
                print("***PHONY'S GOOD END***")
                sleep(2)
            else:
                print(
                    f"Congratulations {player_name}!!! you are the WINNER of this week's challenge, you shall receive this link from Anastasia Dungeons Hills Cosmetics!"
                )
                sleep(4)
                print("https://drive.google.com/drive/folders/0B_sxkSE6-TfETlZoOHF1bTRGTXM?usp=sharing")
                sleep(5)
                print("***GOOD END***")
                sleep(2)
            sleep(1)
            return GameStatus.WINNER
    if not did_win:
        print("You tried to approach the devil carefully...")
        sleep(2)
        print("... but your hands were trembling...")
        sleep(2)
        print("...your weapon was not what you expected...")
        sleep(2)
        print("... It was a shit battle... but")
        sleep(2)
        print("The journey doesn't end here...")
        sleep(2)
        print("Death is just another way we have to choose...")
        sleep(2)
        print("...")
        sleep(1)
        if player_name.lower() == "vis":
            print("I really believed in you...")
            sleep(2)
            print("...but I guess...")
            sleep(1)
            print("you shoud have stayed in your bathroom...")
            sleep(2)
            print("eating lemon pies...")
            sleep(2)
            print("...")
            sleep(1)
            print(f"YOU DIED {player_name}")
            sleep(2)
            print("***VIS'S BAD END***")
            sleep(2)
        elif player_name.lower() == "soren":
            print("I really believed in you..")
            sleep(2)
            print("...but I guess...")
            sleep(1)
            print("Did you think it was a cat? ")
            sleep(2)
            print("Not today Satan!!!")
            sleep(2)
            print("...")
            sleep(1)
            print(f"You died! {player_name}")
            sleep(2)
            print("***SOREN'S BAD END***")
            sleep(2)
        elif player_name.lower() == "kaede":
            print("I really believed in you..")
            sleep(2)
            print("...but I guess...")
            sleep(1)
            print("お。。。。")
            sleep(2)
            print("。。。か　わ　い　い")
            sleep(2)
            print("。。。。。。こ　と")
            sleep(2)
            print("go play you Violin in Hell...")
            sleep(2)
            print("...")
            sleep(1)
            print(f"You died! {player_name}")
            sleep(2)
            print("***KAEDES'S BAD END***")
            sleep(2)
        elif player_name.lower() == "snow":
            print("I really believed in you..")
            sleep(2)
            print("...but I guess...")
            sleep(1)
            print("HAHAHAAHHAHAHA")
            sleep(2)
            print("It is cute you even tried!")
            sleep(2)
            print("but I will call you Nori!")
            sleep(2)
            print("...")
            sleep(1)
            print("You died! Nori!!!")
            sleep(2)
            print("***SNOW'S BAD END***")
            sleep(2)
        elif player_name.lower() == "lurin":
            print("I really believed in you..")
            sleep(2)
            print("...but I guess...")
            sleep(2)
            print("Bitch! ... ")
            sleep(2)
            print(" ... you stole my name...")
            sleep(2)
            print("You are arrested for identity theft!!!")
            sleep(2)
            print("...")
            sleep(1)
            print("del C://LeagueOfLegends")
            sleep(2)
            print("...")
            sleep(0.5)
            print(".....")
            sleep(0.5)
            print("......")
            sleep(0.5)
            print(".............")
            sleep(2)
            print("deletion completed")
            sleep(2)
            print("***PHONY'S GOOD END***")
            sleep(2)
        elif player_name.lower() == "leandro":
            print("nice try")
            sleep(2)
            print("...but I guess...")
            sleep(2)
            print("Try harder next time...")
            sleep(2)
            print("...Nicolas Cage Face...")
            sleep(2)
            print("***LEANDRO'S BAD END***")
            sleep(2)
        elif player_name.lower() == "buiu":
            print("nice try")
            sleep(2)
            print("...but I guess...")
            sleep(2)
            print("Try harder next time...")
            sleep(2)
            print(f"Did you really think this would work? Clown!")
            sleep(2)
            print("***RIDICULOUS BUIU'S END***")
            sleep(2)
            return GameStatus.HAHA
        elif player_name.lower() in ["strahd", "dreadlord"]:
            print("good try")
            sleep(2)
            print("...but I guess...")
            sleep(2)
            print("I never said you were in a cave...")
            sleep(2)
            print("There is sunlight now...")
            sleep(2)
            print("You are burning...")
            sleep(2)
            print("Till Death...")
            sleep(2)
            print("***RIDICULOUS STRAHD'S END***")
            sleep(2)
        else:
            print("I really believed in you..")
            sleep(2)
            print("...but I guess...")
            sleep(2)
            print("This is a shit meta game...")
            sleep(2)
            print(
                "Designed for players from a certain 16:20 tabletop Ravenloft campaign"
            )
            sleep(2)
            print(f"Sorry, {player_name}...")
            sleep(2)
            print("You are dead!!!")
            sleep(2)
            print("***BAD END***")
            sleep(2)
    sleep(1)
    return GameStatus.DEAD


def main():
    """
    This function conducts the entire game.
    """
    wanna_continue = True
    while wanna_continue:
        player_race = input("Your race? ")
        player_name = input("Your name? ")
        status = flee(player_name)
        if status == GameStatus.ALIVE:
            item, status = attack(player_name)
            if status == GameStatus.ALIVE:
                strahd_flight = decide_if_strahd_flies(player_name)
                probability = calculate_win_probability(
                    player_race, player_name, item, strahd_flight
                )
                did_win = roll_for_win(probability)
                status = after_battle(player_race, player_name, did_win)
                if status == GameStatus.WINNER:
                    sleep(5)
                    print(
                        "You are a winner, baby. But there are other possibilities over there..."
                    )
                    wanna_continue = ask_if_wanna_continue(player_name)
                elif status == GameStatus.HAHA:
                    wanna_continue = False
                else:
                    wanna_continue = ask_if_wanna_continue(player_name)
            else:
                wanna_continue = ask_if_wanna_continue(player_name)
        elif status == GameStatus.DEAD:
            wanna_continue = ask_if_wanna_continue(player_name)
        else:
            print("...")
            wanna_continue = ask_if_wanna_continue(player_name)
    input()


main()
