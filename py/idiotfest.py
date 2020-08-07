# * * ** *** ***** ******** ************* *********************
# The Festival of Idiots. A simple machine learning algorithm
# 
# Project: IdiotFest ML
# Part:    Algorithm implementation
# Module:  idiotfest.py                               (\_/)
#                                                     (^.^)
# * * ** *** ***** ******** ************* *********************

class IdiotFestAttendee:

    def __init__(self, prop_values):
    
        self._prop_values = prop_values
 
          
    def get_prop_value(self, prop_name):

        return self._prop_values[prop_name]



class Idiot:

    def __init__(self, fad_name):
    
        self._fad_name = fad_name
        
        self._journal = {}
        
        self._fad_scale_min = None
        self._fad_scale_max = None
        
                        
    @property
    def fad_name(self):

        return self._fad_name
        

    def key(self, fad_value):
    
        return str(fad_value)
        
        
    def key_exists(self, key):

        return key in self._journal
            
        
    def get_fad_value(self, key):
 
        return self._journal[key].fad_value if self.key_exists(key) else None 
        
    
    def scale(self, fad_value):
    
        return 0
        
        
    def get_scale(self, key):

        return self._journal[key].scale if self.key_exists(key) else None 
        
    
    @property
    def fad_scale_min(self):

        return self._fad_scale_min
        
        
    @setter.fad_scale_min
    def fad_scale_min(self, fad_scale):

        if self._fad_scale_min is None:
            self._fad_scale_min = fad_scale
        elif fad_scale_min > fad_scale:
            self._fad_scale_min = fad_scale
         
            
    @property
    def fad_scale_max(self):

        return self._fad_scale_max
        
        
    @setter.fad_scale_max
    def fad_scale_max(self, fad_scale):
    
        if self._fad_scale_max is None:
            self._fad_scale_max = fad_scale
        elif fad_scale_max < fad_scale:
            self._fad_scale_max = fad_scale    


    def fad_scale_span(self):

        return self.fad_scale_max - self.fad_scale_min 
          
                
    def update_fad_scale_range(self, fad_scale):
       
        self.fad_scale_min = fad_scale
        self_fad_scale_max = fad_scale

                        
    def N(self, fad_scale):
    
        # N stands for normalize
   
        self.update_fad_scale_range(fad_scale)
        
        offset = fad_scale - self.fad_scale_min
        
        span = self.fad_scale_span()
        
        norm = offset/span if span != 0 else 0.5
                  
        return norm   
        
        
    def ND(self, fad_value_1, fad_value_2):

        # ND is a normalized difference
        
        fad_scale_1 = self.scale(fad_value_1)
        fad_scale_2 = self.scale(fad_value_2)
            
        return self.N(fad_scale_1) - self.N(fad_scale_2)    
        
        
    def IWND(self, fad_value_1, fad_value_2):

        # IWND is a inverse weighted normalized difference

        result = None
        
        if self.influence != 0:
            result = self.ND(fad_value_1, fad_value_2)/self.influence

        return result
        
        
    def SIWND(self, fad_value_1, fad_value_2):

        # SIWND is a squared inverse weighted normalized difference

        iwnd = self.IWND(fad_value_1, fad_value_2)
        
        return iwnd*iwnd if iwnd is not None else None 
        
             
    def register_fad_value(self, fad_value):
    
        fad_scale = self.scale(fad_value)
        self.update_fad_scale_range(fad_scale)
    
        entry = {"fad_value"       : fad_value, \
                 "fad_scale"       : fad_scale, \
                 "num_of_cases"    : 0, \
                 "target_estimate" : None}
                                
        key = self.key(fad_value)                        
        self._journal[key] = entry
        
    
    def fad_value_registered(self, fad_value):
               
        key = self.key(fad_value)       
               
        return self.key_exists(key)  
    
    
    def get_num_of_cases(self, fad_value):
    
        key = self.key(fad_value)
        
        return self._journal[key]["num_of_cases"]
        
        
    def set_num_of_cases(self, fad_value, num_of_cases):
    
        key = self.key(fad_value)

        self._journal[key]["num_of_cases"] = num_of_cases
        
        
    def inc_num_of_cases(self, fad_value):

       self.set_num_of_cases(fad_value, self.get_num_of_cases(fad_value) + 1) 
        
        
    def get_target_estimate(self, fad_value):
    
        key = self.key(fad_value)
    
        return self._journal[key]["target_estimate"]
        
        
    def set_target_estimate(self, fad_value, target_estimate):
    
        key = self.key(fad_value)

        self._journal[key]["target_estimate"] = target_estimate 
    
    
    def insert_target_estimate(self, fad_value, target_value):
        
        self.set_num_of_cases(fad_value, 1)
        self.set_target_estimate(fad_value, target_value)
            
    
    def update_target_estimate(self, fad_value, onemore_target_value):

        curr_num_of_cases = self.get_num_of_cases(fad_value)
        curr_target_estimate = self.get_target_estimate(fad_value)
        
        total_target_values_updated = \
            curr_target_estimate*curr_num_of_cases + onemore_target_value 
        
        num_of_cases_updated = curr_num_of_cases + 1
        target_estimate_updated = \
            total_target_values_updated/num_of_cases_updated    
                
        self.set_num_of_cases(fad_value, num_of_cases_updated)
        self.set_target_estimate(fad_value, target_estimate_updated)
        
        
    def accept_case(self, fad_value, target_value):
            
        if self.fad_value_registered(fad_value):   
            self.update_target_estimate(fad_value, target_value)                        
        else:    
            self.register_fad_value(fad_value)
            self.insert_target_estimate(fad_value, target_value)

        
        
class AttrIdiot(Idiot):
                
    def update_fad_value_range(self, fad_value):

        pass
        
        
    def ND(self, fad_value_1, fad_value_2):

        return 0 if fad_value_1 == fad_value_2 else 1
        

    def deliver_verdict(self, attendee):

        verdict = 0

        fad_value = attendee.get_prop_value(self.fad_name)

        if self.fad_value_registered(fad_value):
            verdict = self.get_target_estimate(fad_value)
                        
        return verdict          
        
        
        
class NumericIdiot(Idiot):

    def find_reference_fad_values(self, fad_value): 

        x1 = x2 = None
        
        scale = self.scale(fad_value)

        pairs = [[key, self.key2scale(key)] for key in self._journal]  
        pairs_sorted_by_scales = sorted(pairs, key=itemgetter(1))
        
        sorted_keys = [pair[0] for pair in pairs_sorted_by_scales]  
        sorted_scales = [pair[1] for pair in pairs_sorted_by_scales]     
        
        last_fad_value_idx = len(sorted_keys) - 1
        
        if last_fad_value_idx < 0:
            x1 = None
            x2 = None
        
        elif last_fad_value_idx == 0:
            x1 = sorted_keys[0] 
            x2 = None
            
        else:    
            if scale < sorted_scales[0]:
                x1 = sorted_keys[0]
                x2 = sorted_keys[1]
                
            elif scale > sorted_scales[last_fad_value_idx]:
                x1 = sorted_keys[last_fad_value_idx - 1]
                x2 = sorted_keys[last_fad_value_idx]
                
            else:      
                for fad_value_idx in range(last_fad_value_idx):
                    x1 = sorted_keys[fad_value_idx]
                    x2 = sorted_keys[fad_value_idx + 1]
                    if x1 <= scale <= x2:
                        break
        
        return x1, x2
        

    def deliver_verdict(self, attendee):

        verdict = 0
        
        fad_value = attendee.get_prop_value(self.fad_name)
        
        x1, x2 = self.find_reference_fad_values(fad_value)
        
        if x1 is None and x2 is None:
            verdict = 0
        elif x1 is not None and x2 is None:
            verdict = self.get_target_estimate(x1)
        else:
            y1 = self.get_target_estimate(x1)
            y2 = self.get_target_estimate(x2)
                    
            a = (y2 - y1)/(x2 - x1)
            b = y1 - a*x1
                    
            verdict = a*fad_value + b
        
        return verdict          
        
        
        
class IdiotFestJuri:

    def __init__(self, target_name):

        self._target_name = target_name
        self._judges = {}
        self._gallery = [];
	
    
    @property
    def target_name(self):
    
        return self._target_name
    
    
    def append_judge(self, idiot):

        judge = {"idiot"     : idiot, \
                 "score"     : 0, \
                 "influence" : 0}
        
        self._judges[idiot.fad_name] = judge
       
       
    def retrieve_idiot(self, fad_name):

        return self._judges[fad_name]["idiot"]
        
        
    def vote(self, attendee):

        verdicts = {}

        for fad_name in self._judges:
            idiot = self.retrieve_idiot(fad_name)
            verdicts[fad_name] = idiot.deliver_verdict(attendee) 
           
        return verdicts   
        
            
    def get_score(self, prop_name):    
     
        return self._judges[prop_name]["score"]
    
    
    def inc_score(self, prop_name, gain):
    
        self._judges[prop_name]["score"] += gain
    
    
    def set_influence(self, prop_name, influence):    
        
        self._judges[prop_name]["influence"] = influence
        
       
    def calc_mistakes(self, verdicts, target_value):
    
        mistakes = {}
      
        for fad_name in verdicts:
            mistakes[fad_name] = abs(target_value - verdicts[fad_name])
            
        return mistakes   
    

    def debunk_min_mistake(self, leader, applicant):
      
        return True if leader is None else leader > applicant


    def detect_min_mistake(self, mistakes):
    
        min_mistake = None
    
        for prop_name in mistakes:
            if self.debunk_min_mistake(min_mistake, mistakes[prop_name]):
                min_mistake = mistakes[prop_name]
                
        return min_mistake    


    def select_winner_judges(self, mistakes, winning_mistake):
        
        winner_judge_fad_names = []  
        
        for fad_name in mistakes:
            if mistakes[fad_name] == winning_mistake:
                winner_judge_fad_names.append(fad_name)
                
        return winner_judge_fad_names
        
    
    def reward_judge(self, winner_judge_fad_name, gain):
    
        self.inc_score(winner_judge_fad_name, gain)


    def reward_winner_judges(self, winner_judge_fad_names):
    
        num_of_winner_judges = len(winner_judge_fad_names)
        gain = 1/num_of_winner_judges
        
        for fad_name in winner_judge_fad_names:   
            self.reward_judge(fad_name, gain)
        
        
    def recalc_influence_of_judges(self):  
    
        total = 0
        
        for fad_name in self._judges:
            total += self.get_score(fad_name)
            
        for fad_name in self._judges:
            influence = self.get_score(fad_name)/total
            self.set_influence(fad_name, influence)    
        
        
    def retrain_judges(self, attendee):

        for fad_name in self._judges:
            idiot = self.retrieve_idiot(fad_name)
            fad_value = attendee.get_prop_value(fad_name)
            target_value = attendee.get_prop_value(self.target_name)
            idiot.accept_case(fad_value, target_value)
       
       
    def remember(self, attendee):
        
        self._gallery.append(attendee)
        
        for prop_name in self._judges:
            self._judges[prop_name].rememberValues
        

    def accept_attendee(self, attendee):
    
        verdicts = self.vote(attendee)
      
        target_value = attendee.get_prop_value(self.target_name)
      
        mistakes = self.calc_mistakes(verdicts, target_value)
        winning_mistake = self.detect_min_mistake(mistakes)
        winner_judge_fad_names = self.select_winner_judges(mistakes, winning_mistake)       
        self.reward_winner_judges(winner_judge_fad_names)      
        self.recalc_influence_of_judges()
        
        self.retrain_judges(attendee)
        
        self.remember(attendee)
        
       
    def get_influence(self, prop_name):
    
        return self._judges[prop_name]["influence"]
        

    def evaluate_attendee(self, attendee):
        
        verdicts = self.vote(attendee)
        
        target_estimate = 0
        for prop_name in verdicts:
            target_estimate += verdicts[prop_name]*self.get_influence(prop_name)
	
        return target_estimate
        