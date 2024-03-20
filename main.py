import random
from teams import Team
import time
# Creating 16 teams, team power is based on current FIFA ranking(1st place = 100p.).
NED = Team("NED", 94, "NETHERLANDS")
USA = Team("USA", 87, "UNITED STATES")
ARG = Team("ARG", 100, "ARGENTINA")
AUS = Team("AUS", 77, "AUSTRALIA")
JPN = Team("JPN", 82, "JAPAN")
CRO = Team("CRO", 90, "CROATIA")
BRA = Team("BRA", 95, "BRAZIL")
KOR = Team("KOR", 78, "SOUTH KOREA")
ENG = Team("ENG", 97, "ENGLAND")
SEN = Team("SEN", 83, "SENEGAL")
FRA = Team("FRA", 99, "FRANCE")
POL = Team("POL", 70, "POLAND")
MAR = Team("MAR", 88, "MOROCCO")
ESP = Team("ESP", 92, "SPAIN")
POR = Team("POR", 93, "PORTUGAL")
SUI = Team("SUI", 81, "SWITZERLAND")
teams = [NED, USA, ARG, AUS, JPN, CRO, BRA, KOR, ENG, SEN, FRA, POL, MAR, ESP, POR, SUI]
current_teams = teams.copy()

def create_brackets_initial(teams):
    brackets = []
    while len(teams) != 0:
        i = 0
        choose1 = random.choice(teams)
        brackets.insert(i, [choose1])
        teams.remove(choose1)
        choose2 = random.choice(teams)
        brackets[i].append(choose2)
        teams.remove(choose2)
        i += 1
    return brackets


def create_brackets(teams):
    brackets = [teams[i:i+2] for i in range(0, len(teams), 2)]
    return brackets

def represent(arr, num_of_rounds):
    num = 1
    for pair in arr:
        print('-----------')
        print(f'{num} pair draws')
        time.sleep(2)
        num += 1
        for team in pair:
            print(team.get_name())
        time.sleep(0.5)
    print("-----------")
    print("Whole bracket: ")
    if num_of_rounds == 0:
        print("Semifinals")
        print(f"  {arr[0][0].get_name()} vs {arr[0][1].get_name():<15}")
        print(f"  {arr[1][0].get_name()} vs {arr[1][1].get_name():<15}")
    for i in range(num_of_rounds):
        print(f"Round {i+1}:")
        print(f"  {arr[2*i][0].get_name()} vs {arr[2*i][1].get_name():<15}")
        print(f"  {arr[2*i+1][0].get_name()} vs {arr[2*i+1][1].get_name():<15}")
        print("---------------")

def playoff(arr):
    winners = []
    for pair in arr[:]:
        time.sleep(1)
        print(f"Match: {pair[0].get_name()} vs {pair[1].get_name()}")
        sum = pair[0].get_tp() + pair[1].get_tp()
        random_int = random.randint(0, sum)
        if random_int > pair[0].get_tp():
            winners.append(pair[1])
            time.sleep(2)
            print(f"{pair[1].get_full_name().title()} wins!")
        else:
            winners.append(pair[0])
            time.sleep(2)
            print(f"{pair[0].get_full_name().title()} wins!")
    return winners

def semifinals(arr):
    winners = []
    losers = []
    for pair in arr[:]:
        time.sleep(1)
        print(f"Match: {pair[0].get_name()} vs {pair[1].get_name()}")
        sum = pair[0].get_tp() + pair[1].get_tp()
        random_int = random.randint(0, sum)
        if random_int > pair[0].get_tp():
            winners.append(pair[1])
            losers.append(pair[0])
            time.sleep(2)
            print(f"{pair[1].get_full_name().title()} wins!")
        else:
            winners.append(pair[0])
            losers.append(pair[1])
            time.sleep(2)
            print(f"{pair[0].get_full_name().title()} wins!")
    return winners, losers

def finals(winners, losers):
    final = []
    print(f"3rd Place match: {losers[0].get_name()} vs {losers[1].get_name()}")
    time.sleep(2)
    sum = losers[0].get_tp() + losers[1].get_tp()
    random_int = random.randint(0, sum)
    if random_int > losers[0].get_tp():
        print(f"{losers[1].get_full_name().title()} wins!")
        final.append(losers[0])
        final.append(losers[1])
    else:
        print(f"{losers[0].get_full_name().title()} wins!")
        final.append(losers[1])
        final.append(losers[0])
    time.sleep(2)
    print(f"Final match: {winners[0].get_name()} vs {winners[1].get_name()}")
    time.sleep(2)
    sum = winners[0].get_tp() + winners[1].get_tp()
    random_int = random.randint(0, sum)
    if random_int > winners[0].get_tp():
        print(f"{winners[1].get_full_name().title()} wins world cup!")
        final.append(winners[0])
        final.append(winners[1])
    else:
        print(f"{winners[0].get_full_name().title()} wins world cup!")
        final.append(winners[1])
        final.append(winners[0])
    return final


top16 = create_brackets_initial(current_teams)
represent(top16, 4)
time.sleep(10)
top16_winners = playoff(top16)
top_8 = create_brackets(top16_winners)
time.sleep(5)
represent(top_8, 2)
time.sleep(10)
top8_winners = playoff(top_8)
top_4 = create_brackets(top8_winners)
time.sleep(5)
represent(top_4, 0)
time.sleep(10)
top_4_winners, top_4_losers = semifinals(top_4)
time.sleep(10)
print('--------')
final = finals(top_4_winners, top_4_losers)
time.sleep(5)
print(f"Winner of the world cup 2022: {final[-1].get_full_name().title()}")
time.sleep(1)
print(f"Second place: {final[-2].get_full_name().title()}")
time.sleep(1)
print(f"Third place: {final[-3].get_full_name().title()}")
time.sleep(1)
print(f"Fourth place: {final[-4].get_full_name().title()}")