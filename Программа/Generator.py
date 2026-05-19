import random
import psycopg2
from psycopg2 import sql, extras
from faker import Faker
from typing import List, Set
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'astronomy_db',
    'user': 'postgres',
    'password': 'ChgSQL(0201)'
}

fake = Faker(['en_US'])
Faker.seed(42)
random.seed(42)

OBJECT_TYPES = ["Galaxy", "Nebula", "Star", "Cluster", "Remnant", "Quasar", "Pulsar", "BlackHole", "Dwarf", "Giant", "WDwarf"]
EDU_TYPES = ["University", "College", "Institute", "Academy", "School", "Research"]
RESEARCH_TYPES = ["State", "Private", "Mixed", "International", "Non-profit", "Commercial"]
TELESCOPE_TYPES = ["Optical", "Radio", "Infrared", "X-ray", "Gamma", "UV", "Solar"]
TELESCOPE_SPOTS = ["Space", "Hawaii", "Chile", "Canary", "Australia", "S.Africa", 
                   "Arizona", "PuertoRico", "China", "India", "Namibia", "Argentina"]

PROFESSIONS = ["Astrophysics", "Cosmology", "PlanetarySci", "StellarAstro", "RadioAstro",
               "SolarPhysics", "GalacticAstro", "Extragalactic", "Astrometry", 
               "Exoplanetology", "Heliophysics", "Astrochemistry"]

GRADUATES = ["PhD", "Master", "Bachelor", "Professor", "Dr.Science", "Cand.Science",
             "Sr.Researcher", "Lead.Researcher", "Assoc.Prof", "Postdoc"]

ORGANISATION_PREFIXES = ["Intl", "National", "European", "Asian", "African", "American",
                          "Russian", "German", "French", "Japanese", "Chinese", "Indian"]

ORGANISATION_SUFFIXES = ["SpaceInst", "Observatory", "SpaceCenter", 
                         "AstroLab", "PlanetarySoc", "CosmicCenter", 
                         "RadioStn", "CosmicLab"]

OBJECT_NAMES = ["Andromeda", "MilkyWay", "OrionNeb", "Pleiades", "Betelgeuse", "Sirius", "Vega", 
                "CrabNeb", "BlackEye", "Sombrero", "Whirlpool", "Pinwheel",
                "Triangulum", "CatsEye", "RingNeb", "EagleNeb", "Horsehead",
                "Tarantula", "RoseGal", "Sunflower", "Tadpole", "CigarGal"]

CATALOG_NAMES = ["NGC", "IC", "Messier", "Caldwell", "PGC", "UGC", "SDSS", "2MASS", "HIP", "Tycho", 
                 "GaiaDR3", "WISE", "Hipparcos", "GSC", "USNO", "NOMAD", "DENIS", "IRAS"]

COUNTRIES = ["USA", "UK", "France", "Germany", "Japan", "Russia", "China", "Italy", "Canada", "Australia", 
             "Spain", "Netherlands", "Switzerland", "Sweden", "India", "Brazil", "Mexico", "S.Africa", 
             "S.Korea", "Israel", "Poland", "Ukraine", "Norway", "Finland", "Denmark", "Austria", "Belgium"]

FIRST_NAMES = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", 
               "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
               "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
               "Matthew", "Betty", "Anthony", "Margaret", "Donald", "Sandra", "Mark", "Ashley",
               "Paul", "Kimberly", "Steven", "Emily", "Andrew", "Donna", "Kenneth", "Michelle",
               "George", "Carol", "Joshua", "Amanda", "Kevin", "Dorothy", "Brian", "Melissa",
               "Edward", "Deborah", "Ronald", "Stephanie", "Timothy", "Rebecca", "Jason", "Sharon",
               "Jeffrey", "Laura", "Ryan", "Cynthia", "Jacob", "Kathleen", "Gary", "Amy"]

LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Rodriguez", "Martinez", "Wilson", "Anderson", "Taylor", "Thomas", "Moore", "Jackson",
              "Martin", "Lee", "White", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Hall",
              "Young", "Allen", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson",
              "Hill", "Ramirez", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans",
              "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart", "Flores", "Morris"]

def create_connection():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            client_encoding='UTF8'
        )
        print(f"Connected to database '{DB_CONFIG['database']}'")
        return conn
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        raise

def init_database():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database='postgres',
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            client_encoding='UTF8'
        )
        conn.autocommit = True
        cur = conn.cursor()
        
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG['database'],))
        exists = cur.fetchone()
        
        if not exists:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_CONFIG['database'])))
            print(f"Database '{DB_CONFIG['database']}' created")
        else:
            print(f"Database '{DB_CONFIG['database']}' already exists")
        
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"Could not check/create database: {e}")
        return False

def create_schema(conn):
    with conn.cursor() as cur:
        cur.execute("CREATE SCHEMA IF NOT EXISTS Astronomy")
        cur.execute("SET search_path TO Astronomy")
        
        cur.execute("DROP TABLE IF EXISTS Object CASCADE")
        cur.execute("DROP TABLE IF EXISTS Automatic_telescope CASCADE")
        cur.execute("DROP TABLE IF EXISTS Amateur_astronomer CASCADE")
        cur.execute("DROP TABLE IF EXISTS Scientist CASCADE")
        cur.execute("DROP TABLE IF EXISTS Research_organisation CASCADE")
        cur.execute("DROP TABLE IF EXISTS Educational_institution CASCADE")
        cur.execute("DROP TABLE IF EXISTS Catalog CASCADE")
        
        cur.execute("""
            CREATE TABLE Catalog (
                ID_Catalog DECIMAL PRIMARY KEY,
                Count DECIMAL NOT NULL,
                CatalogName VARCHAR(100) NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Educational_institution (
                ID_Organisation DECIMAL PRIMARY KEY,
                Type VARCHAR(20) NOT NULL,
                Country VARCHAR(48) NOT NULL,
                Budget DECIMAL NOT NULL,
                Organisation VARCHAR(100) NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Research_organisation (
                ID_Organisation VARCHAR(100) PRIMARY KEY,
                Type VARCHAR(15) NOT NULL,
                Country VARCHAR(48) NOT NULL,
                Budget DECIMAL NOT NULL,
                Organisation VARCHAR(100) NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Scientist (
                Person VARCHAR(55) PRIMARY KEY,
                Country VARCHAR(48) NOT NULL,
                Proffesion VARCHAR(20) NOT NULL,
                Graduate VARCHAR(20) NOT NULL,
                ID_Organisations_Edu DECIMAL[] NOT NULL,
                ID_Organisations_Res VARCHAR(100)[] NOT NULL,
                ID_Catalogs DECIMAL[] NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Amateur_astronomer (
                Person VARCHAR(55) PRIMARY KEY,
                Country VARCHAR(48) NOT NULL,
                Age VARCHAR(3) NOT NULL,
                ID_Organisations_Edu DECIMAL[] NOT NULL,
                ID_Catalogs DECIMAL[] NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Automatic_telescope (
                Telescope VARCHAR(32) PRIMARY KEY,
                Type VARCHAR(32) NOT NULL,
                Year DECIMAL NOT NULL,
                Spot VARCHAR(40) NOT NULL,
                ID_Organisations_Res VARCHAR(100)[] NOT NULL,
                ID_Catalogs DECIMAL[] NOT NULL
            )
        """)
        
        cur.execute("""
            CREATE TABLE Object (
                ObjectName VARCHAR(30) PRIMARY KEY,
                Type VARCHAR(20) NOT NULL,
                Declension DECIMAL NOT NULL,
                Size DECIMAL NOT NULL,
                Magnitude DECIMAL NOT NULL,
                ID_Catalogs DECIMAL[] NOT NULL,
                ID_Telescopes VARCHAR(32)[] NOT NULL
            )
        """)
        
        conn.commit()
        print("Schema and tables created")

def generate_catalogs(conn, count: int):
    print(f"  Generating catalogs ({count} records)...")
    data = []
    for i in range(count):
        catalog = (i + 1, random.randint(10, 50000), f"{random.choice(CATALOG_NAMES)}-{random.randint(1, 999)}")
        data.append(catalog)
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Catalog (ID_Catalog, Count, CatalogName) VALUES %s", data)
    conn.commit()

def generate_educational_institutions(conn, count: int):
    print(f"  Generating educational institutions ({count} records)...")
    data = []
    for i in range(count):
        edu_type = random.choice(EDU_TYPES)
        if len(edu_type) > 20:
            edu_type = edu_type[:20]
        
        institution = (i + 1, edu_type, random.choice(COUNTRIES), 
                      round(random.uniform(1e6, 1e11), 0), f"{fake.company()} Univ")
        data.append(institution)
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Educational_institution (ID_Organisation, Type, Country, Budget, Organisation) VALUES %s", data)
    conn.commit()

def generate_research_organisations(conn, count: int):
    print(f"  Generating research organisations ({count} records)...")
    data = []
    for i in range(count):
        org_type = random.choice(RESEARCH_TYPES)
        if len(org_type) > 15:
            org_type = org_type[:15]
            
        organisation = (f"RO_{i+1:04d}", org_type, random.choice(COUNTRIES),
                       round(random.uniform(5e5, 5e10), 0), f"{random.choice(ORGANISATION_PREFIXES)} {random.choice(ORGANISATION_SUFFIXES)}")
        data.append(organisation)
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Research_organisation (ID_Organisation, Type, Country, Budget, Organisation) VALUES %s", data)
    conn.commit()

def generate_scientists(conn, target_records: int, edu_ids: list, research_ids: list, catalog_ids: list):
    print(f"  Generating scientists (target: {target_records} scientists)...")
    
    data = []
    used_names = set()
    person_index = 1
    
    for _ in range(target_records):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        
        if target_records > 5000:
            person = f"{first} {last} {person_index}"
        else:
            person = f"{first} {last}"
        
        if person in used_names:
            person_index += 1
            continue
        
        used_names.add(person)
        country = random.choice(COUNTRIES)
        profession = random.choice(PROFESSIONS)
        graduate = random.choice(GRADUATES)
        
        num_edu = random.randint(1, 5)
        num_res = random.randint(1, 5)
        num_cat = random.randint(1, 10)
        
        selected_edu = random.sample(edu_ids, min(num_edu, len(edu_ids)))
        selected_res = random.sample(research_ids, min(num_res, len(research_ids)))
        selected_cat = random.sample(catalog_ids, min(num_cat, len(catalog_ids)))
        
        scientist = (person, country, profession, graduate, 
                    selected_edu, selected_res, selected_cat)
        data.append(scientist)
        person_index += 1
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Scientist (Person, Country, Proffesion, Graduate, ID_Organisations_Edu, ID_Organisations_Res, ID_Catalogs) VALUES %s", data, page_size=1000)
    conn.commit()
    
    print(f"    Generated {len(data)} scientists")

def generate_amateurs(conn, target_records: int, edu_ids: list, catalog_ids: list):
    print(f"  Generating amateur astronomers (target: {target_records} amateurs)...")
    
    data = []
    used_names = set()
    person_index = 1
    
    for _ in range(target_records):
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        
        if target_records > 5000:
            person = f"{first} {last} {person_index}"
        else:
            person = f"{first} {last}"
        
        if person in used_names:
            person_index += 1
            continue
        
        used_names.add(person)
        country = random.choice(COUNTRIES)
        age = str(random.randint(16, 85))
        
        num_edu = random.randint(1, 5)
        num_cat = random.randint(1, 10)
        
        selected_edu = random.sample(edu_ids, min(num_edu, len(edu_ids)))
        selected_cat = random.sample(catalog_ids, min(num_cat, len(catalog_ids)))
        
        amateur = (person, country, age, selected_edu, selected_cat)
        data.append(amateur)
        person_index += 1
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Amateur_astronomer (Person, Country, Age, ID_Organisations_Edu, ID_Catalogs) VALUES %s", data, page_size=1000)
    conn.commit()
    
    print(f"    Generated {len(data)} amateurs")

def generate_telescopes(conn, target_records: int, research_ids: list, catalog_ids: list):
    print(f"  Generating telescopes (target: {target_records} telescopes)...")
    
    data = []
    telescope_names = ["Hubble", "Webb", "Keck", "VLT", "ALMA", "Chandra", "Fermi", "FAST", "Gemini", "Subaru"]
    used_names = set()
    
    for _ in range(target_records):
        while True:
            tel_name = f"{random.choice(telescope_names)}-{random.randint(1, 9999)}"
            if tel_name not in used_names:
                used_names.add(tel_name)
                break
        
        tel_type = random.choice(TELESCOPE_TYPES)
        if len(tel_type) > 32:
            tel_type = tel_type[:32]
        spot = random.choice(TELESCOPE_SPOTS)
        if len(spot) > 40:
            spot = spot[:40]
        year = random.randint(1950, 2025)
        
        num_res = random.randint(1, 5)
        num_cat = random.randint(1, 10)
        
        selected_res = random.sample(research_ids, min(num_res, len(research_ids)))
        selected_cat = random.sample(catalog_ids, min(num_cat, len(catalog_ids)))
        
        telescope = (tel_name, tel_type, year, spot, selected_res, selected_cat)
        data.append(telescope)
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Automatic_telescope (Telescope, Type, Year, Spot, ID_Organisations_Res, ID_Catalogs) VALUES %s", data)
    conn.commit()
    
    print(f"    Generated {len(data)} telescopes")

def generate_objects(conn, target_records: int, catalog_ids: list, telescope_ids: list):
    print(f"  Generating space objects (target: {target_records:,} objects)...")
    
    data = []
    used_names = set()
    
    for _ in range(target_records):
        obj_type = random.choice(OBJECT_TYPES)
        
        while True:
            obj_name = f"{random.choice(OBJECT_NAMES)}_{random.randint(1, 100000)}"
            if len(obj_name) > 30:
                obj_name = obj_name[:30]
            if obj_name not in used_names:
                used_names.add(obj_name)
                break
        
        num_cat = random.randint(1, 5)
        num_tel = random.randint(1, 5)
        
        selected_cat = random.sample(catalog_ids, min(num_cat, len(catalog_ids)))
        selected_tel = random.sample(telescope_ids, min(num_tel, len(telescope_ids)))
        
        obj = (obj_name, obj_type,
              round(random.uniform(-90, 90), 4), 
              round(random.uniform(0.01, 120), 2),
              round(random.uniform(-30, 20), 2),
              selected_cat, selected_tel)
        data.append(obj)
    
    with conn.cursor() as cur:
        extras.execute_values(cur, "INSERT INTO Object (ObjectName, Type, Declension, Size, Magnitude, ID_Catalogs, ID_Telescopes) VALUES %s", data, page_size=5000)
    conn.commit()
    
    print(f"    Generated {len(data)} objects")

def main():
    print("=" * 70)
    print("TEST DATA GENERATOR FOR ASTRONOMY DATABASE")
    print("=" * 70)
    
    counts = {
        "catalogs": 500,
        "edu_institutions": 500,
        "research_orgs": 200,
        "scientists": 5000,
        "amateurs": 10000,
        "telescopes": 500,
        "objects": 10000
    }
    
    try:
        print("\nInitializing database...")
        if not init_database():
            print("Failed to initialize database. Exiting.")
            return
        
        print("\nConnecting to PostgreSQL...")
        conn = create_connection()
        
        print("\nCreating database structure...")
        create_schema(conn)
        
        print("\nGenerating data:\n")
        
        generate_catalogs(conn, counts["catalogs"])
        generate_educational_institutions(conn, counts["edu_institutions"])
        generate_research_organisations(conn, counts["research_orgs"])
        
        catalog_ids = list(range(1, counts["catalogs"] + 1))
        edu_ids = list(range(1, counts["edu_institutions"] + 1))
        research_ids = [f"RO_{i+1:04d}" for i in range(counts["research_orgs"])]
        
        generate_scientists(conn, counts["scientists"], edu_ids, research_ids, catalog_ids)
        generate_amateurs(conn, counts["amateurs"], edu_ids, catalog_ids)
        generate_telescopes(conn, counts["telescopes"], research_ids, catalog_ids)
        
        with conn.cursor() as cur:
            cur.execute("SELECT Telescope FROM Automatic_telescope")
            telescope_ids = [row[0] for row in cur.fetchall()]
        
        generate_objects(conn, counts["objects"], catalog_ids, telescope_ids)
        
        print("\n" + "=" * 70)
        print("DATA GENERATION COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("\nDatabase connection closed")

main()