import unittest
#* Section 1 (Git)

#* Section 2 (Data Definitions)

#* 1)#Fahrenheit is of data type integer and is used to represent temperature in degrees Fahrenheit
    #Celsius is of data type integer and is used to represent the temperature in degrees Celsius

#* 2)#Price is of data type float, is positive, and is used to represent the price of an item in cents

#* 3)
class Price_Record:
    def __init__(self, item, price):
        self.item=item  # a string
        self.price=price # a Price
    def __repr__(self):
        return "Price_Record({!r},{!r})".format(self.item, self.price)
    def __eq__(self,other):
        return (type(other)==Price_Record
            and self.item == other.item
            and self.price == other.price)

#* 4)
# a URL is a string used to represent the website address accessed
# a date is a string in the format ddmmyyyy which represents the day month and year respectively

class Tab:
    def __init__(self, URL, date_loaded):
        self.URL=URL # a URL
        self.date_loaded=date_loaded # a date
    def __repr__(self):
        return "Tab({!r},{!r})".format(self.URL, self.date_loaded)
    def __eq__(self,other):
        return (type(other)==Price_Record
            and self.URL == other.URL
            and self.date_loaded == other.date_loaded)
#* Section 3 (Signature, Purpose Statements, Headers)

#* 1) Signature: Int Int -> Int
#     Purpose Statement: #return the sum of the price of an item and its sales tax
#     Header: def Total(price, sales_tax):

#* 2) Signature: Str -> Int
#     Purpose Statement: #return the price of an item given the item name
#     Header: def search_item(item_name):

#* 3) Signature: Str -> Int
#     Purpose Statement: #return the median income given a geographic region
#     Header: def median_income(region):

#* 4) Signature: Str -> List
#     Purpose Statement: #return the cities located within a geograhic region given the region
#     Header: def cities_in_region(geo_region):

#* Section 4 (Test Cases)

#* 1) Signature: Int Int Int -> Int
#     Purpose Statement: #return the second largest number given three distinct numbers
def middle_number(first_number, second_number, third_number):
    pass

class TestNumbers(unittest.TestCase):
    def test_negative(self):
            self.assertEqual(middle_number(-300, -10, -20), -20)
    def test_postive(self):
            self.assertEqual(middle_number(1, 20, 30), 20)
    def test_zero(self):
            self.assertEqual(middle_number(0, 0, 0), 0)

#* 2) Signature: Str -> Bool
#return true if the string given has no capital letters otherwise return false
def string_check(input_string):
        pass
class TestString(unittest.TestCase):
    def test_capital(self):
            self.assertEqual(string_check('Hello World'), True)
    def test_lowercase(self):
            self.assertEqual(string_check('hello world'), False)

#* 3) Signature: Str Str -> Str
#return the name of the state that is northernmost given the name of two states
def northernmost_state(state_name1, state_name2):
    pass
class TestState(unittest.TestCase):
    def test_first_north(self):
            self.assertEqual(northernmost_state('Oregon', 'California'), 'Oregon')

#* Section 5 (Whole Functions)

#* 1) int -> int
#return the length in meters given the length in feet
#meter is an int representing length
#feet is an int representing length
def f2m(feet):
    meters = feet * .3048
    return meters

#* 2) a pitch is an int represented as a frequency in Hz
#a duration is a length of time in seconds represented by an int
#a musical note is made of pitch and duration
class Musical_Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch #a pitch
        self.duration = duration #a duration
    def __repr__(self):
        return "Musical_Note({!r},{!r})".format(self.pitch, self.duration)
    def __eq__(self,other):
        return (type(other)== Musical_Note
            and self.pitch == other.pitch
            and self.duration == other.duration)
#* 3)

def up_one_octave(note):
    up_octave = note.pitch * 2
    new_note = Musical_Note(up_octave, note.duration)
    return new_note

#* 4)
def up_one_octave_m(note):
    note.pitch = note.pitch * 2
    return None

class TestCase(unittest.TestCase):
    def test_up_octave(self):
        self.assertEqual(up_one_octave(Musical_Note(200, 3)), Musical_Note(400, 3))

    def test_up_octave_m(self):
        testnote = Musical_Note(200, 3)
        self.assertEqual(up_one_octave_m(testnote), None)
        self.assertEqual(testnote.pitch, 400)

    def test_convert_meter_one(self):
        self.assertEqual(f2m(1), .3048)

    def test_convert_meter_zero(self):
        self.assertEqual(f2m(0), 0)


if __name__ == '__main__':
    unittest.main()


