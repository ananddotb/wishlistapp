from datetime import date
from enum import Enum

Status = Enum('status', 'open fulfilled abandoned re-open')

class Wish : 
    
    def __init__(self, txt) :
        self._text = txt
        self._date_added = date.today
        self._status = 'open'
    
    def __str__(self) :
        return self._text

    def set_date_added(self, dt) :
        self._date_added = dt

    def set_date_expected(self, dtf) :
        self._date_expected = dtf

    def set_status(self, status) :
        self._status = status
    
    def set_event(self, evt) :
        self._event = evt
    
    def set_emotion (self, emote) :
        self._emotion = emote
    
    def set_reminder(self, rem) :
        self._reminder = rem
    
    def set_tag(self, tag) :
        self._tag = tag
    
    def tag(self) :
        return self._tag
    
    def reminder(self) :
        return self._reminder
    
    def emotion(self) :
        return self._emotion
    
    def event(self) :
        return self._event

    def status (self):
        return self._status
    
    def date_added(self) :
        return self._date_added
    
    def date_expected(self) :
        return self._date_expected



    

    



