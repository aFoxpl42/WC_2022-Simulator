class Team:
    def __init__(self, name, team_power, full_name):
        self.name = name
        self.team_power = team_power
        self.full_name = full_name
        
    def get_tp(self):
        return self.team_power
    
    def get_name(self):
        return self.name
    
    def get_full_name(self):
        return self.full_name