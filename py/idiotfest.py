# * * ** *** ***** ******** ************* *********************
# The Festival of Idiots. A simple machine learning algorithm
# 
# Project: IdiotFest ML
# Part:    Algorithm implementation
# Module:  idiotfest.py                               (\_/)
#                                                     (^.^)
# * * ** *** ***** ******** ************* *********************

import math

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
        
        
    # Deriving values from fad_values    

    def key(self, fad_value):
    
        return str(fad_value)
        
             
    def scale(self, fad_value):
    
        return 0    
        
        
    # Accessing an idiot's journal    
        
    def assemble_journal_entry(self, fad_value):
        
        journal_entry = { \
            "fad_value"       : fad_value, \
            "fad_scale"       : self.scale(fad_value), \
            "num_of_cases"    : 0, \
            "target_estimate" : None}
        
        return journal_entry
        
        
    def key_exists(self, key):

        return key in self._journal
            
        
    def get_fad_value(self, key):
 
        return self._journal[key]["fad_value"] if self.key_exists(key) else None 
        
        
    def get_fad_scale(self, key):

        return self._journal[key]["fad_scale"] if self.key_exists(key) else None 
        
        
    def get_num_of_cases(self, key):
        
        return self._journal[key]["num_of_cases"]
        
        
    def set_num_of_cases(self, key, num_of_cases):

        self._journal[key]["num_of_cases"] = num_of_cases
        
        
    def inc_num_of_cases(self, key):

       self.set_num_of_cases(key, self.get_num_of_cases(fad_value) + 1) 
        
        
    def get_target_estimate(self, key):
    
        return self._journal[key]["target_estimate"]
        
        
    def set_target_estimate(self, key, target_estimate):
    
        self._journal[key]["target_estimate"] = target_estimate 
        
        
    def get_sorted_keys(self):
    
        sorted_keys = \
            [key for key in sorted(self._journal, key=lambda k: self._journal[k]["fad_scale"])]

        return sorted_keys
      
      
    # Managing min and max scales 
    
    @property
    def fad_scale_min(self):

        return self._fad_scale_min
        
        
    @fad_scale_min.setter
    def fad_scale_min(self, fad_scale):

        if self._fad_scale_min is None:
            self._fad_scale_min = fad_scale
        elif self._fad_scale_min > fad_scale:
            self._fad_scale_min = fad_scale
         
            
    @property
    def fad_scale_max(self):

        return self._fad_scale_max
        
        
    @fad_scale_max.setter
    def fad_scale_max(self, fad_scale):
    
        if self._fad_scale_max is None:
            self._fad_scale_max = fad_scale
        elif self._fad_scale_max < fad_scale:
            self._fad_scale_max = fad_scale    


    def get_fad_scale_span(self):
    
        result = None
        
        if  self.fad_scale_min is not None and self.fad_scale_min is not None:
            result = self.fad_scale_max - self.fad_scale_min

        return result
          
                
    def update_fad_scale_span(self, fad_scale):
       
        self.fad_scale_min = fad_scale
        self.fad_scale_max = fad_scale

                        
    # Managing a journal
    
    def register_fad_value(self, fad_value):
    
        journal_entry = self.assemble_journal_entry(fad_value)
                                
        key = self.key(fad_value)                        
        self._journal[key] = journal_entry
        
        fad_scale = self.get_fad_scale(key)
        self.update_fad_scale_span(fad_scale)
        
    
    def fad_value_registered(self, fad_value):
               
        key = self.key(fad_value)       
               
        return self.key_exists(key)  
    

    def insert_target_estimate(self, fad_value, target_value):
        
        key = self.key(fad_value) 
        
        self.set_num_of_cases(key, 1)
        self.set_target_estimate(key, target_value)
            
    
    def update_target_estimate(self, fad_value, onemore_target_value):

        key = self.key(fad_value) 
        
        curr_num_of_cases = self.get_num_of_cases(key)
        curr_target_estimate = self.get_target_estimate(key)
        
        total_target_values_updated = \
            curr_target_estimate*curr_num_of_cases + onemore_target_value 
        
        num_of_cases_updated = curr_num_of_cases + 1
        target_estimate_updated = \
            total_target_values_updated/num_of_cases_updated    
                
        self.set_num_of_cases(key, num_of_cases_updated)
        self.set_target_estimate(key, target_estimate_updated)
        
        
    def accept_case(self, fad_value, target_value):
            
        if self.fad_value_registered(fad_value):   
            self.update_target_estimate(fad_value, target_value)                        
        else:    
            self.register_fad_value(fad_value)
            self.insert_target_estimate(fad_value, target_value)
                        
                        
    # Performing calculations over values and scales                    
                        
    def N(self, fad_scale):
    
        # N stands for normalize
   
        self.update_fad_scale_span(fad_scale)
        
        offset = fad_scale - self.fad_scale_min
        span = self.get_fad_scale_span()
        norm = offset/span if span != 0 else 0.5
                  
        return norm   
        
        
    def ND(self, fad_value_1, fad_value_2):

        # ND is a normalized difference
        
        fad_scale_1 = self.scale(fad_value_1)
        fad_scale_2 = self.scale(fad_value_2)
            
        return self.N(fad_scale_1) - self.N(fad_scale_2)    
        
        
    def IWND(self, fad_value_1, fad_value_2, weight):

        # IWND is a inverse weighted normalized difference

        result = None
        
        if weight != 0:
            result = self.ND(fad_value_1, fad_value_2)/weight

        return result
        
        
    def IWND2(self, fad_value_1, fad_value_2, weight):

        # SIWND is a squared inverse weighted normalized difference

        iwnd = self.IWND(fad_value_1, fad_value_2, weight)
        
        return iwnd*iwnd if iwnd is not None else None 
        
             
             
class AttrIdiot(Idiot):
                
    def update_fad_scale_span(self, fad_scale):

        pass
        
        
    def ND(self, fad_value_1, fad_value_2):

        return 0 if fad_value_1 == fad_value_2 else 1
        

    def deliver_verdict(self, attendee):

        verdict = 0

        fad_value = attendee.get_prop_value(self.fad_name)

        if self.fad_value_registered(fad_value):
            key = self.key(fad_value)
            verdict = self.get_target_estimate(key)
                        
        return verdict          
        
        
        
class NumericIdiot(Idiot):

    def scale(self, fad_value):
    
        return fad_value
        

    def find_bound_keys(self, fad_scale): 

        key_lt = key_rt = None
 
        keys = self.get_sorted_keys()
        last_key_idx = len(keys) - 1
        
        if last_key_idx == 0:
            key_lt = keys[0] 
            
        elif last_key_idx >= 1:    
            if fad_scale < self.get_fad_scale(keys[0]):
                key_lt = keys[0]
                key_rt = keys[1]
                
            elif fad_scale > self.get_fad_scale(keys[last_key_idx]):
                key_lt = keys[last_key_idx - 1]
                key_rt = keys[last_key_idx]
                
            else:      
                for key_idx in range(last_key_idx):
                    key_lt = keys[key_idx]
                    fad_score_lt = self.get_fad_scale(key_lt)
                    key_rt = keys[key_idx + 1]
                    fad_score_rt = self.get_fad_scale(key_rt)
                    if fad_score_lt <= fad_scale <= fad_score_rt:
                        break
        
        return key_lt, key_rt
        

    def deliver_verdict(self, attendee):

        verdict = 0
        
        attendee_fad_value = attendee.get_prop_value(self.fad_name)
        attendee_fad_scale = self.scale(attendee_fad_value)
        
        key_lt, key_rt = self.find_bound_keys(attendee_fad_scale)   
        
        if key_rt is not None:
            fad_scale_lt = self.get_fad_scale(key_lt)
            fad_scale_rt = self.get_fad_scale(key_rt)
            delta_fad_scale = fad_scale_rt - fad_scale_lt
            
            target_estimate_lt = self.get_target_estimate(key_lt)
            target_estimate_rt = self.get_target_estimate(key_rt)
            delta_target_estimate = target_estimate_rt - target_estimate_lt
                  
            a = delta_target_estimate/delta_fad_scale
            b = target_estimate_lt - a*fad_scale_lt
                    
            verdict = a*attendee_fad_scale + b
            
        elif key_lt is not None:
            verdict = self.get_target_estimate(key_lt)    
        
        return verdict          
        
        
        
class IdiotFestJury:

    def __init__(self, target_name):

        self._target_name = target_name
        self._judges = {}
        self._vip_judge_fad_names = []
        self._directory = [];
        self._margin = 0.7
	
    
    @property
    def target_name(self):
    
        return self._target_name
        
        
    @property
    def margin(self):
    
        return self._margin
        
        
    @margin.setter
    def margin(self, margin):
    
        self._margin = margin
    
    
    # Managing an attendee directory

    def append_attendee(self, attendee):
    
        directory_entry = { \
            "attendee" : attendee, \
            "weight"   : 1 \
        }
        
        self._directory.append(directory_entry)
        
        
    def get_attendee_prop_value(self, idxdir, prop_name):
    
        return self._directory[idxdir]["attendee"].get_prop_value(prop_name)
        
        
    def get_attendee_target_value(self, idxdir):

        return self.get_attendee_prop_value(idxdir, self.target_name)

              
    # Managing judges
    
    def append_judge(self, idiot):

        judge = {"idiot"  : idiot, \
                 "score"  : 0, \
                 "weight" : 0}
        
        self._judges[idiot.fad_name] = judge
       
       
    def retrieve_idiot(self, fad_name):

        return self._judges[fad_name]["idiot"]
    
    
    def get_judge_score(self, prop_name):    
     
        return self._judges[prop_name]["score"]    
    
    
    def inc_judge_score(self, prop_name, gain):
    
        self._judges[prop_name]["score"] += gain
        
        
    def get_judge_weight(self, prop_name):
    
        return self._judges[prop_name]["weight"]
        
    
    def set_judge_weight(self, prop_name, weight):    
        
        self._judges[prop_name]["weight"] = weight
    
    
    # Performing calculations over attendees
    
    def D2(self, attendee1, attendee2):
    
        # D2 is a square of distance between two attendees 

        vip_judge_fad_names = self.get_vip_judge_fad_names()
        
        d2 = 0
        for fad_name in vip_judge_fad_names:
        
            fad_value_1 = attendee1.get_prop_value(fad_name)
            fad_value_2 = attendee2.get_prop_value(fad_name)
            
            weight = self.get_judge_weight(fad_name)
            
            idiot = self.retrieve_idiot(fad_name)
            
            d2 += idiot.IWND2(fad_value_1, fad_value_2, 1)
            
        return d2  
    
   
    # Training and selecting judges
    
    def vote(self, attendee):

        verdicts = {}

        for fad_name in self._judges:
            idiot = self.retrieve_idiot(fad_name)
            verdicts[fad_name] = idiot.deliver_verdict(attendee) 
           
        return verdicts   
        
       
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
    
        self.inc_judge_score(winner_judge_fad_name, gain)


    def reward_winner_judges(self, winner_judge_fad_names):
    
        num_of_winner_judges = len(winner_judge_fad_names)
        gain = 1/num_of_winner_judges
        
        for fad_name in winner_judge_fad_names:   
            self.reward_judge(fad_name, gain)
        
        
    def retrain_judges(self, attendee):

        for fad_name in self._judges:
            idiot = self.retrieve_idiot(fad_name)
            fad_value = attendee.get_prop_value(fad_name)
            target_value = attendee.get_prop_value(self.target_name)
            idiot.accept_case(fad_value, target_value)
         

    def examine_attendee(self, attendee):
    
        verdicts = self.vote(attendee)
      
        target_value = attendee.get_prop_value(self.target_name)
      
        mistakes = self.calc_mistakes(verdicts, target_value)
        winning_mistake = self.detect_min_mistake(mistakes)
        winner_judge_fad_names = self.select_winner_judges(mistakes, winning_mistake)       
        self.reward_winner_judges(winner_judge_fad_names)      
        
        self.retrain_judges(attendee)
        
    
    def recalc_judge_weights(self):  
    
        total = 0      
        for fad_name in self._judges:
            total += self.get_judge_score(fad_name)
            
        judges_by_score = \
            sorted(self._judges, \
                   key = lambda fad_name: self._judges[fad_name]["score"], \
                   reverse = True)
            
        subtotal = 0
        significant_judges = []    
        for fad_name in judges_by_score:
            subtotal += self.get_judge_score(fad_name)
            significant_judges.append(fad_name)
            if subtotal/total >= self.margin:
                break
        
        self._vip_judge_fad_names = []        
        for fad_name in self._judges:
            if fad_name in significant_judges:
                weight = self.get_judge_score(fad_name)/subtotal
                self.set_judge_weight(fad_name, weight)
                self._vip_judge_fad_names.append(fad_name)
            else:
                self.set_judge_weight(fad_name, 0)        
        
            
    def train_judges(self):

        for directory_entry in self._directory:
            self.examine_attendee(directory_entry["attendee"])
            
        self.recalc_judge_weights() 
            
      
    def get_vip_judge_fad_names(self):
    
        return self._vip_judge_fad_names
    
    
    # Making the job ;-)    

    def evaluate_attendee_by_voting(self, attendee):
        
        verdicts = self.vote(attendee)
        
        target_estimate = 0
        for prop_name in verdicts:
            target_estimate += verdicts[prop_name]*self.get_judge_weight(prop_name)
	
        return target_estimate
        
          
    def evaluate_attendee_by_neighbours(self, attendee):
        
        winner_golden = None
        d2golden = float("inf")
        
        winner_silver = None
        d2silver = float("inf")
        
        winner_bronze = None
        d2bronse = float("inf")
        
        for known_attendee in self._directory:  
        
            d2 = self.D2(attendee, known_attendee["attendee"])
            
            if d2golden > d2:
                d2bronze = d2silver
                winner_bronze = winner_silver
                d2silver = d2golden
                winner_silver = winner_golden
                d2golden = d2
                winner_golden = known_attendee
            elif d2silver > d2:
                d2bronze = d2silver
                winner_bronze = winner_silver
                d2silver = d2
                winner_silver = known_attendee
            elif d2bronze > d2:
                d2bronze = d2
                winner_bronze =  known_attendee  
                
        target_value_golden = \
            winner_golden["attendee"].get_prop_value(self.target_name) 
        target_value_silver = \
            winner_silver["attendee"].get_prop_value(self.target_name)
        target_value_bronze = \
            winner_bronze["attendee"].get_prop_value(self.target_name)
                  
        estimate = (target_value_golden + target_value_silver + target_value_bronze)/3
        
        return estimate
            
        