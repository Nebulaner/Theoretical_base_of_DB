import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

OBJECT_NAMES = ["Andromeda", "Milky Way", "Orion Nebula", "Pleiades", "Betelgeuse", "Sirius", "Vega", "Crab Nebula", "Black Eye Galaxy", "Sombrero Galaxy"]
OBJECT_TYPES = ["Galaxy", "Nebula", "Star", "Globular Cluster", "Supernova Remnant"]
DECLINATION_RANGE = (-90.0, 90.0)
SIZE_RANGE = (0.01, 120.0)
MAGNITUDE_RANGE = (-30.0, 20.0)

EDU_NAMES = ["Harvard University", "MIT", "Cambridge University", "Oxford University", "Sorbonne", "Heidelberg University", "Tokyo University", "Moscow State University", "Beijing University", "Stanford University"]
EDU_TYPES = ["University", "College", "Institute", "Academy"]
COUNTRIES = ["USA", "UK", "France", "Germany", "Japan", "Russia", "China", "Italy", "Canada", "Australia", "Spain", "Netherlands", "Switzerland", "Sweden", "India"]
BUDGET_RANGE = (1e6, 1e11)

SCIENTIST_NAMES = ["John Smith", "Jane Doe", "Ivan Petrov", "Maria Garcia", "Hans Mueller", "Yuki Tanaka", "Pierre Dubois", "Anna Kowalski", "Carlos Fernandez", "Olga Smirnova"]
PROFESSIONS = ["Astrophysics", "Cosmology", "Planetary Science", "Stellar Astronomy", "Radio Astronomy"]
GRADUATES = ["PhD", "Master", "Bachelor", "Professor", "Doctor of Science"]

RESEARCH_TYPES = ["State", "Private", "Mixed", "International"]
RESEARCH_BUDGET_RANGE = (5e5, 5e10)

TELESCOPE_NAMES = ["Hubble", "Webb", "Keck", "VLT", "ALMA", "Chandra", "Fermi", "Arecibo", "FAST", "Gemini"]
TELESCOPE_TYPES = ["Optical", "Radio", "Infrared", "X-ray", "Gamma-ray"]
TELESCOPE_SPOTS = ["Space", "Hawaii", "Chile", "Canary Islands", "Australia", "South Africa", "Arizona", "Puerto Rico", "China", "India"]
YEAR_START = 1950
YEAR_END = 2025

AMATEUR_NAMES = ["Bob Williams", "Alice Brown", "Charlie Davis", "Diana Prince", "Ethan Hunt", "Fiona Gallagher", "George Costanza", "Helen Keller"]
AMATEUR_AGE_RANGE = (16, 85)

CATALOG_NAMES = ["NGC", "IC", "Messier", "Caldwell", "PGC", "UGC", "SDSS", "2MASS", "HIP", "Tycho"]
CATALOG_SIZE_RANGE = (10, 50000)
CATALOG_YEAR_RANGE = (1600, 2025)

def random_date(start_year: int, end_year: int) -> str:
    """Генерирует случайную дату в формате YYYY-MM-DD"""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def random_float(min_val: float, max_val: float, precision: int = 2) -> float:
    return round(random.uniform(min_val, max_val), precision)

def escape_sql_string(s: str) -> str:
    """Экранирует одинарные кавычки для SQL"""
    return s.replace("'", "''")

def generate_objects(n: int = 20) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        obj = {
            "ObjectName": random.choice(OBJECT_NAMES) + f"_{random.randint(1, 100)}",
            "Type": random.choice(OBJECT_TYPES),
            "Declension": random_float(DECLINATION_RANGE[0], DECLINATION_RANGE[1], 3),
            "Size": random_float(SIZE_RANGE[0], SIZE_RANGE[1], 2),
            "Magnitude": random_float(MAGNITUDE_RANGE[0], MAGNITUDE_RANGE[1], 2)
        }
        data.append(obj)
    return data

def generate_educational_institutions(n: int = 15) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        inst = {
            "Organisation": random.choice(EDU_NAMES) + f" {random.randint(1, 20)}",
            "Type": random.choice(EDU_TYPES),
            "Country": random.choice(COUNTRIES),
            "Budget": random_float(BUDGET_RANGE[0], BUDGET_RANGE[1], 0)
        }
        data.append(inst)
    return data

def generate_scientists(n: int = 25) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        scientist = {
            "Person": random.choice(SCIENTIST_NAMES) + f" {random.randint(1, 99)}",
            "Organisation": random.choice(EDU_NAMES) + f" {random.randint(1, 5)}",
            "Country": random.choice(COUNTRIES),
            "Proffesion": random.choice(PROFESSIONS),
            "Graduate": random.choice(GRADUATES)
        }
        data.append(scientist)
    return data

def generate_research_organisations(n: int = 12) -> List[Dict[str, Any]]:
    data = []
    prefixes = ["RI", "Institute", "Center", "Lab", "Foundation"]
    for _ in range(n):
        org = {
            "Organisation": random.choice(prefixes) + " " + random.choice(OBJECT_NAMES) + f" {random.randint(1, 30)}",
            "Type": random.choice(RESEARCH_TYPES),
            "Country": random.choice(COUNTRIES),
            "Budget": random_float(RESEARCH_BUDGET_RANGE[0], RESEARCH_BUDGET_RANGE[1], 0)
        }
        data.append(org)
    return data

def generate_telescopes(n: int = 15) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        tel = {
            "Telescope": random.choice(TELESCOPE_NAMES) + f"-{random.randint(1, 50)}",
            "Type": random.choice(TELESCOPE_TYPES),
            "Owner": random.choice(EDU_NAMES + RESEARCH_TYPES) + f" {random.randint(1, 10)}",
            "Year": random_date(YEAR_START, YEAR_END),
            "Spot": random.choice(TELESCOPE_SPOTS)
        }
        data.append(tel)
    return data

def generate_amateurs(n: int = 18) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        amateur = {
            "Person": random.choice(AMATEUR_NAMES) + f" {random.randint(1, 999)}",
            "Country": random.choice(COUNTRIES),
            "Age": random.randint(AMATEUR_AGE_RANGE[0], AMATEUR_AGE_RANGE[1])
        }
        data.append(amateur)
    return data

def generate_catalogs(n: int = 12) -> List[Dict[str, Any]]:
    data = []
    for _ in range(n):
        catalog = {
            "CatalogName": random.choice(CATALOG_NAMES) + f"-{random.randint(1, 999)}",
            "Size": random.randint(CATALOG_SIZE_RANGE[0], CATALOG_SIZE_RANGE[1]),
            "Year": random_date(CATALOG_YEAR_RANGE[0], CATALOG_YEAR_RANGE[1])
        }
        data.append(catalog)
    return data

def generate_insert_sql(table_name: str, columns: List[str], rows: List[Dict[str, Any]]) -> str:
    if not rows:
        return f"-- Нет данных для таблицы {table_name}\n"
    
    col_list = ", ".join(columns)
    values_lines = []
    
    for row in rows:
        values = []
        for col in columns:
            val = row.get(col, None)
            if val is None:
                values.append("NULL")
            elif isinstance(val, str):
                values.append(f"'{escape_sql_string(val)}'")
            elif isinstance(val, (int, float)):
                values.append(str(val))
            else:
                values.append(f"'{escape_sql_string(str(val))}'")
        values_lines.append(f"({', '.join(values)})")
    
    values_block = ",\n".join(values_lines)
    return f"INSERT INTO {table_name} ({col_list}) VALUES\n{values_block};\n"

def main():
    random.seed(42)  # Для воспроизводимости результатов
    
    # Генерация данных
    objects = generate_objects(20)
    edu_institutions = generate_educational_institutions(15)
    scientists = generate_scientists(25)
    research_orgs = generate_research_organisations(12)
    telescopes = generate_telescopes(15)
    amateurs = generate_amateurs(18)
    catalogs = generate_catalogs(12)
    
    # Формирование SQL-скрипта
    sql_script = "-- Сгенерированные данные для базы данных\n"
    sql_script += "-- Таблица: Object\n"
    sql_script += generate_insert_sql("Object", ["ObjectName", "Type", "Declension", "Size", "Magnitude"], objects)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Educational_institution\n"
    sql_script += generate_insert_sql("Educational_institution", ["Organisation", "Type", "Country", "Budget"], edu_institutions)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Scientist\n"
    sql_script += generate_insert_sql("Scientist", ["Person", "Organisation", "Country", "Proffesion", "Graduate"], scientists)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Research_organisation\n"
    sql_script += generate_insert_sql("Research_organisation", ["Organisation", "Type", "Country", "Budget"], research_orgs)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Automatic_telescope\n"
    sql_script += generate_insert_sql("Automatic_telescope", ["Telescope", "Type", "Owner", "Year", "Spot"], telescopes)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Amateur_astronomer\n"
    sql_script += generate_insert_sql("Amateur_astronomer", ["Person", "Country", "Age"], amateurs)
    sql_script += "\n"
    
    sql_script += "-- Таблица: Catalog\n"
    sql_script += generate_insert_sql("Catalog", ["CatalogName", "Size", "Year"], catalogs)
    
    # Сохранение в файл
    with open("generated_data.sql", "w", encoding="utf-8") as f:
        f.write(sql_script)
    
    print("SQL-скрипт успешно сгенерирован и сохранён в файл 'generated_data.sql'")
    print(f"Сгенерировано записей:")
    print(f"  Object: {len(objects)}")
    print(f"  Educational institution: {len(edu_institutions)}")
    print(f"  Scientist: {len(scientists)}")
    print(f"  Research organisation: {len(research_orgs)}")
    print(f"  Automatic telescope: {len(telescopes)}")
    print(f"  Amateur astronomer: {len(amateurs)}")
    print(f"  Catalog: {len(catalogs)}")

if __name__ == "__main__":
    main()