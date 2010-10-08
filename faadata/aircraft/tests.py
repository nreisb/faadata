import datetime
from decimal import Decimal
from django.test import TestCase
from parser import AircraftRegistration, AircraftManufacturerCode

class AircraftRegistrationFileParsing(TestCase):
    def test_1(self):
        parsed = AircraftRegistration('1    ,1071                          ,3980115,54556,1988,5,FEDERAL AVIATION ADMINISTRATION                   ,NATL FLIGHT PROGRAM OVERSIGHT OFC,6125 SW 68TH ST RM 137N          ,OKLA CITY         ,OK,73169-1225,2,109,US,20080617,19900214,1T        ,5,5,A,50000001, ,19880909,                                                  ,                                                  ,                                                  ,                                                  ,                                                  ,')
        self.failUnlessEqual(parsed.n_number, '1')
        self.failUnlessEqual(parsed.serial_number, '1071')
        self.failUnlessEqual(parsed.aircraft_mfr_model_code, '3980115')
        self.failUnlessEqual(parsed.engine_mfr_model_code, '54556')
        self.failUnlessEqual(parsed.year_mfg, '1988')
        self.failUnlessEqual(parsed.type_registrant, '5')
        self.failUnlessEqual(parsed.registrant_name, 'FEDERAL AVIATION ADMINISTRATION')
        self.failUnlessEqual(parsed.street1, 'NATL FLIGHT PROGRAM OVERSIGHT OFC')
        self.failUnlessEqual(parsed.street2, '6125 SW 68TH ST RM 137N')
        self.failUnlessEqual(parsed.city, 'OKLA CITY')
        self.failUnlessEqual(parsed.state, 'OK')
        self.failUnlessEqual(parsed.zip_code, '73169-1225')
        self.failUnlessEqual(parsed.region, '2')
        self.failUnlessEqual(parsed.county, '109')
        self.failUnlessEqual(parsed.country, 'US')
        self.failUnlessEqual(parsed.last_activity_date, datetime.datetime(year=2008, month=6, day=17).date())
        self.failUnlessEqual(parsed.certificate_issue_date, datetime.datetime(year=1990, month=2, day=14).date())
        self.failUnlessEqual(parsed.airworthiness_classification_code, '1')
        self.failUnlessEqual(parsed.aircraft_type, '5')
        self.failUnlessEqual(parsed.engine_type, '5')
        self.failUnlessEqual(parsed.status_code, 'A')
        self.failUnlessEqual(parsed.mode_s_code, '50000001')
        self.failUnlessEqual(parsed.fractional_ownership, '')
        self.failUnlessEqual(parsed.airworthiness_date, datetime.datetime(year=1988, month=9, day=9).date())
        self.failUnlessEqual(parsed.other_name_1, '')
        self.failUnlessEqual(parsed.other_name_2, '')
        self.failUnlessEqual(parsed.other_name_3, '')
        self.failUnlessEqual(parsed.other_name_4, '')
        self.failUnlessEqual(parsed.other_name_5, '')

class AircraftManufacturerCodeFileParsing(TestCase):
    def test_1(self):
        parsed = AircraftManufacturerCode('00301BR,AERO-ACE                      ,CE 1                ,4,1,1,1,01,001,CLASS 1,0082,')
        self.failUnlessEqual(parsed.code, '00301BR')
        self.failUnlessEqual(parsed.manufacturer, 'AERO-ACE')
        self.failUnlessEqual(parsed.model, 'CE 1')
        self.failUnlessEqual(parsed.aircraft_type, '4')
        self.failUnlessEqual(parsed.engine_type, '1')
        self.failUnlessEqual(parsed.category, '1')
        self.failUnlessEqual(parsed.builder_certification_code, '1')
        self.failUnlessEqual(parsed.number_of_engines, '01')
        self.failUnlessEqual(parsed.number_of_seats, '001')
        self.failUnlessEqual(parsed.aircraft_weight, 'CLASS 1')
        self.failUnlessEqual(parsed.cruising_speed, '0082')

    def test_2(self):
        parsed = AircraftManufacturerCode('0030509,HILTON FLYING SERVICE INC     ,JUNIOR ACE E        ,4,1,1,1,01,002,CLASS 1,0000,')
        self.failUnlessEqual(parsed.code, '0030509')
        self.failUnlessEqual(parsed.manufacturer, 'HILTON FLYING SERVICE INC')
        self.failUnlessEqual(parsed.model, 'JUNIOR ACE E')
        self.failUnlessEqual(parsed.aircraft_type, '4')
        self.failUnlessEqual(parsed.engine_type, '1')
        self.failUnlessEqual(parsed.category, '1')
        self.failUnlessEqual(parsed.builder_certification_code, '1')
        self.failUnlessEqual(parsed.number_of_engines, '01')
        self.failUnlessEqual(parsed.number_of_seats, '002')
        self.failUnlessEqual(parsed.aircraft_weight, 'CLASS 1')
        self.failUnlessEqual(parsed.cruising_speed, '0000')

    def test_3(self):
        parsed = AircraftManufacturerCode('0050550,ADVANCED AERODYNAMICS & STRUCT,JETCRUZER 500       ,4,2,1,1,01,006,CLASS 1,0000,')
        self.failUnlessEqual(parsed.code, '0050550')
        self.failUnlessEqual(parsed.manufacturer, 'ADVANCED AERODYNAMICS & STRUCT')
        self.failUnlessEqual(parsed.model, 'JETCRUZER 500')
        self.failUnlessEqual(parsed.aircraft_type, '4')
        self.failUnlessEqual(parsed.engine_type, '2')
        self.failUnlessEqual(parsed.category, '1')
        self.failUnlessEqual(parsed.builder_certification_code, '1')
        self.failUnlessEqual(parsed.number_of_engines, '01')
        self.failUnlessEqual(parsed.number_of_seats, '006')
        self.failUnlessEqual(parsed.aircraft_weight, 'CLASS 1')
        self.failUnlessEqual(parsed.cruising_speed, '0000')

    def test_4(self):
        parsed = AircraftManufacturerCode('0160000,AEROMOT                       ,AMT-200(SUPR XIMNGO),1,1,1,0,01,002,CLASS 1,0000,')
        self.failUnlessEqual(parsed.code, '0160000')
        self.failUnlessEqual(parsed.manufacturer, 'AEROMOT')
        self.failUnlessEqual(parsed.model, 'AMT-200(SUPR XIMNGO)')
        self.failUnlessEqual(parsed.aircraft_type, '1')
        self.failUnlessEqual(parsed.engine_type, '1')
        self.failUnlessEqual(parsed.category, '1')
        self.failUnlessEqual(parsed.builder_certification_code, '0')
        self.failUnlessEqual(parsed.number_of_engines, '01')
        self.failUnlessEqual(parsed.number_of_seats, '002')
        self.failUnlessEqual(parsed.aircraft_weight, 'CLASS 1')
        self.failUnlessEqual(parsed.cruising_speed, '0000')

    def test_4(self):
        parsed = AircraftManufacturerCode('7102802,PIPER                         ,PA-28-140           ,4,1,1,0,01,004,CLASS 1,0107,')
        self.failUnlessEqual(parsed.code, '7102802')
        self.failUnlessEqual(parsed.manufacturer, 'PIPER')
        self.failUnlessEqual(parsed.model, 'PA-28-140')
        self.failUnlessEqual(parsed.aircraft_type, '4')
        self.failUnlessEqual(parsed.engine_type, '1')
        self.failUnlessEqual(parsed.category, '1')
        self.failUnlessEqual(parsed.builder_certification_code, '0')
        self.failUnlessEqual(parsed.number_of_engines, '01')
        self.failUnlessEqual(parsed.number_of_seats, '004')
        self.failUnlessEqual(parsed.aircraft_weight, 'CLASS 1')
        self.failUnlessEqual(parsed.cruising_speed, '0107')
