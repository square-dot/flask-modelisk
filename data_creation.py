import datetime
import random
from reference_data import Country, Company, Currency, Classification, CodeGenerator
from insurance_name_generator import test_insurance_data_generator
from insurance_program import Program
import ZODB, ZODB.FileStorage
import transaction



class Reference_data():

    def __init__(self):
        self.countries = []
        self.currencies = []
        self.lines_of_business = []
        self.companies = []


def root():
        storage = ZODB.FileStorage.FileStorage('modelisk_db.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root
        return root


def create_countries() -> list[Country]:
    l = []
    for t in (
        ("USA", "United States"),
        ("ITA", "Italy"),
        ("FRA", "France"),
        ("GBR", "Great Britain"),
        ("GER", "Germany"),
        ("CHE", "Switzerland"),
        ("SWE", "Sweden"),
        ("BRA", "Brazil"),
        ("ESP", "Spain"),
        ("JPN", "Japan"),
    ):

        l.append(Country(t[1], t[0]))
    return l

def create_currencies() -> list[Currency]:
    l = []
    for t in (
        ("CHF", "Swiss Franc"),
        ("USD", "US Dollar"),
        ("GBP", "British Pound"),
        ("EUR", "Euro"),
    ):
        l.append(Currency(t[1], t[0]))
    return l

def create_lobs() -> list[Classification]:
    l = []
    for t in [tup[1] for tup in ("Agriculture", "Casualty", "Motor", "Property")]:
        l.append(Classification(t))
    return l

def create_companies(countries: list[Country]):
    nr = 50
    l = []
    for v in test_insurance_data_generator(nr, countries):
        l.append(Company(
            country=next((c for c in countries if c.iso_code_3 == v[0])),
            name=v[1],
            email=v[2],
        ))
    return l

def create_programs(insureds, currencies, lobs, code_generator) -> list[Program]:
    nr = 100
    l = []
    for _ in range(nr):
        code = code_generator.next_program_code()
        currency = random.choice(currencies)
        insured = random.choice(insureds)
        lob = random.choice(lobs)
        l.append(Program(
            code = code,
            insured=insured,
            currency=currency,
            lob=lob,
            start_date=datetime.date(2020, 1, 1),
            end_date=datetime.date(2020, 12, 31),
        ))
    return l

def populate_test_data():
    rt = root()
    rt.reference_data = Reference_data()
    transaction.commit()
    rt.code_generator = CodeGenerator()
    transaction.commit()
    countries = create_countries()
    currencies = create_currencies()
    lobs = create_lobs()
    insureds = create_companies(countries)
    programs = create_programs(insureds, currencies, lobs, rt.code_generator)
    rt.programs = programs
    transaction.commit()
    ref_data = rt.reference_data
    ref_data.countries = countries
    ref_data.currencies = currencies
    ref_data.lines_of_business = lobs
    ref_data.companies = insureds
    transaction.commit()
