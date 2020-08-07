import sys

sys.path.append("../py")

from idiotfest import *


# Testing a numeric idiot

numeric_idiot = NumericIdiot("size")

numeric_idiot.accept_case(0,  0)
numeric_idiot.accept_case(1,  1)
numeric_idiot.accept_case(2,  4)
numeric_idiot.accept_case(2,  4)
numeric_idiot.accept_case(3,  9)
numeric_idiot.accept_case(4, 16) 

assert len(numeric_idiot._journal) == 5
assert numeric_idiot.fad_scale_min == 0
assert numeric_idiot.fad_scale_max == 4
assert numeric_idiot.N(0) == 0
assert numeric_idiot.N(2) == 0.5
assert numeric_idiot.N(4) == 1

attendee_1  = IdiotFestAttendee({"size"  : -1})
attendee0   = IdiotFestAttendee({"size"  :  0})
attendee2   = IdiotFestAttendee({"size"  :  2})
attendee2_5 = IdiotFestAttendee({"size"  :  2.5})
attendee4   = IdiotFestAttendee({"size"  :  4})
attendee5   = IdiotFestAttendee({"size"  :  5})

assert numeric_idiot.deliver_verdict(attendee_1)  == -1
assert numeric_idiot.deliver_verdict(attendee0)   ==  0
assert numeric_idiot.deliver_verdict(attendee2)   ==  4
assert numeric_idiot.deliver_verdict(attendee2_5) ==  6.5
assert numeric_idiot.deliver_verdict(attendee4)   == 16
assert numeric_idiot.deliver_verdict(attendee5)   == 23


# Testing an attributive idiot

attr_idiot = AttrIdiot("city")

attr_idiot.accept_case("Tel-Aviv", 30)
attr_idiot.accept_case("Tel-Aviv", 29)
attr_idiot.accept_case("Moscow",   10)
attr_idiot.accept_case("Moscow",   10)
attr_idiot.accept_case("Kiev",     15)
attr_idiot.accept_case("Kiev",     17)
attr_idiot.accept_case("London",   18)
attr_idiot.accept_case("London",   17)
attr_idiot.accept_case("Berlin",   16)
attr_idiot.accept_case("Berlin",   15) 

assert len(attr_idiot._journal) == 5
assert attr_idiot.fad_scale_min == None
assert attr_idiot.fad_scale_max == None

attendee1 = IdiotFestAttendee({"city"  : "Tel-Aviv"})
attendee2 = IdiotFestAttendee({"city"  : "Moscow"})
attendee3 = IdiotFestAttendee({"city"  : "Kiev"})
attendee4 = IdiotFestAttendee({"city"  : "London"})
attendee5 = IdiotFestAttendee({"city"  : "Berlin"})

assert attr_idiot.deliver_verdict(attendee1) == 29.5
assert attr_idiot.deliver_verdict(attendee2) == 10
assert attr_idiot.deliver_verdict(attendee3) == 16
assert attr_idiot.deliver_verdict(attendee4) == 17.5
assert attr_idiot.deliver_verdict(attendee5) == 15.5

