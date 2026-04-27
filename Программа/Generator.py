import random
import csv
import os
from typing import Dict, List, Any

COUNTRIES = ["USA", "UK", "France", "Germany", "Japan", "Russia", "China", "Italy", "Canada", "Australia", 
             "Spain", "Netherlands", "Switzerland", "Sweden", "India", "Brazil", "Mexico", "South Africa", 
             "South Korea", "Israel", "Poland", "Ukraine", "Norway", "Finland", "Denmark", "Austria", "Belgium",
             "South Africa", "Arizona", "Puerto Rico", "China", "India", "Namibia", "Argentina"]

OBJECT_TYPES = ["Galaxy", "Nebula", "Star", "Globular Cluster", "Open Cluster", "Supernova Remnant", 
                "Planetary Nebula", "Quasar", "Pulsar", "Black Hole", "Brown Dwarf", "Red Giant", "White Dwarf"]

EDU_TYPES = ["University", "College", "Institute", "Academy", "School", "Research Center", "Polytechnic"]
RESEARCH_TYPES = ["State", "Private", "Mixed", "International", "Non-profit", "Commercial", "Foundation"]
TELESCOPE_TYPES = ["Optical", "Radio", "Infrared", "X-ray", "Gamma-ray", "UV", "Solar", "Neutrino", "Gravitational"]
TELESCOPE_SPOTS = ["Space", "Hawaii", "Chile", "Canary Islands", "Australia", "South Africa", 
                   "Arizona", "Puerto Rico", "China", "India", "Namibia", "Argentina", "Tenerife", "Antarctica"]

PROFESSIONS = ["Astrophysics", "Cosmology", "Planetary Science", "Stellar Astronomy", "Radio Astronomy",
               "Solar Physics", "Galactic Astronomy", "Extragalactic Astronomy", "Astrometry", 
               "Exoplanetology", "Heliophysics", "Astrochemistry"]
GRADUATES = ["PhD", "Master", "Bachelor", "Professor", "Doctor of Science", "Candidate of Science", 
             "Senior Researcher", "Leading Researcher", "Associate Professor", "Postdoc"]

ORGANISATION_PREFIXES = ["International", "National", "European", "Asian", "African", "American"]
ORGANISATION_SUFFIXES = ["Space Research Institute", "Astronomical Observatory", "Space Center", 
                         "Astrophysics Lab", "Planetary Society", "Cosmic Research Center", 
                         "Radio Astronomy Station", "Cosmic Ray Laboratory"]

OBJECT_NAMES = ["Andromeda Galaxy", "Milky Way", "Orion Nebula", "Pleiades", "Betelgeuse", "Sirius", "Vega", 
                "Crab Nebula", "Black Eye Galaxy", "Sombrero Galaxy", "Whirlpool Galaxy", "Pinwheel Galaxy",
                "Triangulum Galaxy", "Cat's Eye Nebula", "Ring Nebula", "Eagle Nebula", "Horsehead Nebula",
                "Tarantula Nebula", "Rose Galaxy", "Sunflower Galaxy", "Tadpole Galaxy", "Cigar Galaxy"]

CATALOG_NAMES = ["NGC", "IC", "Messier", "Caldwell", "PGC", "UGC", "SDSS", "2MASS", "HIP", "Tycho", 
                 "Gaia DR3", "WISE", "Hipparcos", "GSC", "USNO", "NOMAD", "DENIS", "IRAS"]

SCIENTIST_FIRST = ["John", "Jane", "Ivan", "Maria", "Hans", "Yuki", "Pierre", "Anna", "Carlos", "Olga",
                   "David", "Sarah", "Michael", "Elena", "Thomas", "Natalia", "Robert", "Patricia", 
                   "James", "Linda", "William", "Barbara", "Richard", "Jennifer", "Joseph", "Maria"]
SCIENTIST_LAST = ["Smith", "Doe", "Petrov", "Garcia", "Mueller", "Tanaka", "Dubois", "Kowalski", "Fernandez", 
                  "Smirnova", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Martinez",
                  "Anderson", "Taylor", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson"]

AMATEUR_FIRST = ["Bob", "Alice", "Charlie", "Diana", "Ethan", "Fiona", "George", "Helen", "Ian", "Julia",
                 "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quentin", "Rachel", "Steve", "Tina",
                 "Ursula", "Victor", "Wendy", "Xavier", "Yvonne", "Zachary"]
AMATEUR_LAST = ["Williams", "Brown", "Davis", "Prince", "Hunt", "Gallagher", "Costanza", "Keller", "Anderson",
                "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "Clark", "Rodriguez",
                "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright"]

def random_float(min_val: float, max_val: float, precision: int = 2) -> float:
    return round(random.uniform(min_val, max_val), precision)

def random_int(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

def random_date_year(min_year: int, max_year: int) -> int:
    return random.randint(min_year, max_year)

def random_name(first_names: List[str], last_names: List[str]) -> str:
    """Генерирует случайное имя"""
    return f"{random.choice(first_names)} {random.choice(last_names)}"

class DataGenerator:
    def __init__(self):
        self.data = {}
        
    def generate_catalogs(self, count: int) -> List[Dict[str, Any]]:
        """Каталог - независимая таблица"""
        print(f"  Генерация каталогов ({count} записей)...")
        catalogs = []
        for i in range(count):
            catalog = {
                "ID_Catalog": i + 1,
                "Count": random_int(10, 50000),
                "CatalogName": f"{random.choice(CATALOG_NAMES)}-{random_int(1, 999)}"
            }
            catalogs.append(catalog)
        self.data['catalogs'] = catalogs
        return catalogs
    
    def generate_educational_institutions(self, count: int) -> List[Dict[str, Any]]:
        """Образовательное учреждение - независимая таблица"""
        print(f"  Генерация образовательных учреждений ({count} записей)...")
        institutions = []
        for i in range(count):
            inst = {
                "ID_Organisation": i + 1,
                "Type": random.choice(EDU_TYPES),
                "Country": random.choice(COUNTRIES),
                "Budget": random_float(1e6, 1e11, 0),
                "Organisation": f"{random.choice(EDU_TYPES)} of {random.choice(COUNTRIES)} {random_int(1, 50)}"
            }
            institutions.append(inst)
        self.data['edu_institutions'] = institutions
        return institutions
    
    def generate_research_organisations(self, count: int) -> List[Dict[str, Any]]:
        """Исследовательская организация - независимая таблица"""
        print(f"  Генерация исследовательских организаций ({count} записей)...")
        organisations = []
        for i in range(count):
            org = {
                "ID_Organisation": f"RO_{i+1:04d}",
                "Type": random.choice(RESEARCH_TYPES),
                "Country": random.choice(COUNTRIES),
                "Budget": random_float(5e5, 5e10, 0),
                "Organisation": f"{random.choice(ORGANISATION_PREFIXES)} {random.choice(ORGANISATION_SUFFIXES)} {random_int(1, 99)}"
            }
            organisations.append(org)
        self.data['research_orgs'] = organisations
        return organisations
    
    def generate_scientists(self, count: int) -> List[Dict[str, Any]]:
        """Учёный - зависит от организаций и каталогов"""
        print(f"  Генерация ученых ({count} записей)...")
        scientists = []
        
        # Получаем списки ID организаций и каталогов
        all_orgs = self.data.get('edu_institutions', []) + self.data.get('research_orgs', [])
        org_ids = [org["ID_Organisation"] for org in all_orgs]
        catalog_ids = [cat["ID_Catalog"] for cat in self.data.get('catalogs', [])]
        
        for i in range(count):
            scientist = {
                "Person": random_name(SCIENTIST_FIRST, SCIENTIST_LAST),
                "Country": random.choice(COUNTRIES),
                "Proffesion": random.choice(PROFESSIONS),
                "Graduate": random.choice(GRADUATES),
                "ID_Organisation": random.choice(org_ids) if org_ids else None,
                "ID_Catalog": random.choice(catalog_ids) if catalog_ids else None
            }
            scientists.append(scientist)
        self.data['scientists'] = scientists
        return scientists
    
    def generate_amateurs(self, count: int) -> List[Dict[str, Any]]:
        """Астроном-любитель - зависит от организаций и каталогов"""
        print(f"  Генерация астрономов-любителей ({count} записей)...")
        amateurs = []
        
        # Получаем числовые ID организаций (только из образовательных учреждений)
        edu_org_ids = [org["ID_Organisation"] for org in self.data.get('edu_institutions', [])]
        catalog_ids = [cat["ID_Catalog"] for cat in self.data.get('catalogs', [])]
        
        for i in range(count):
            amateur = {
                "Person": random_name(AMATEUR_FIRST, AMATEUR_LAST),
                "Country": random.choice(COUNTRIES),
                "Age": str(random_int(16, 85)),
                "ID_Organisation": random.choice(edu_org_ids) if edu_org_ids else None,
                "ID_Catalog": random.choice(catalog_ids) if catalog_ids else None
            }
            amateurs.append(amateur)
        self.data['amateurs'] = amateurs
        return amateurs
    
    def generate_telescopes(self, count: int) -> List[Dict[str, Any]]:
        """Автоматический телескоп - зависит от организаций и каталогов"""
        print(f"  Генерация телескопов ({count} записей)...")
        telescopes = []
        
        # Получаем список ID организаций
        all_orgs = self.data.get('edu_institutions', []) + self.data.get('research_orgs', [])
        org_ids = [org["ID_Organisation"] for org in all_orgs]
        catalog_ids = [cat["ID_Catalog"] for cat in self.data.get('catalogs', [])]
        
        for i in range(count):
            tel = {
                "Telescope": f"{random.choice(['Hubble', 'Webb', 'Keck', 'VLT', 'ALMA', 'Chandra', 'Fermi', 'FAST', 'Gemini', 'Subaru', 'GTC', 'LBT'])}-{random_int(1, 99)}",
                "Type": random.choice(TELESCOPE_TYPES),
                "ID_Organisation": random.choice(org_ids) if org_ids else None,
                "Year": random_date_year(1950, 2025),
                "Spot": random.choice(TELESCOPE_SPOTS),
                "ID_Catalog": random.choice(catalog_ids) if catalog_ids else None
            }
            telescopes.append(tel)
        self.data['telescopes'] = telescopes
        return telescopes
    
    def generate_objects(self, count: int) -> List[Dict[str, Any]]:
        """Объект космоса - зависит от каталогов"""
        print(f"  Генерация объектов космоса ({count:,} записей)...")
        objects = []
        
        catalog_ids = [cat["ID_Catalog"] for cat in self.data.get('catalogs', [])]
        
        for i in range(count):
            obj = {
                "ID_Catalog": random.choice(catalog_ids) if catalog_ids else None,
                "Type": random.choice(OBJECT_TYPES),
                "Declension": random_float(-90, 90, 4),
                "Size": random_float(0.01, 120, 2),
                "Magnitude": random_float(-30, 20, 2),
                "Object": f"{random.choice(OBJECT_NAMES)}_{random_int(1, 10000)}"
            }
            objects.append(obj)
        self.data['objects'] = objects
        return objects

def generate_sql_insert(table_name: str, columns: List[str], rows: List[Dict[str, Any]], batch_size: int = 1000) -> str:
    """Генерирует SQL INSERT запросы с поддержкой батчей для больших таблиц"""
    if not rows:
        return f"-- Нет данных для таблицы {table_name}\n"
    
    result = []
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i+batch_size]
        values_list = []
        
        for row in batch:
            values = []
            for col in columns:
                val = row.get(col, None)
                if val is None:
                    values.append("NULL")
                elif isinstance(val, str):
                    val_escaped = val.replace("'", "''")
                    values.append(f"'{val_escaped}'")
                elif isinstance(val, (int, float)):
                    values.append(str(val))
                else:
                    values.append(f"'{str(val)}'")
            values_list.append(f"({', '.join(values)})")
        
        values_block = ",\n".join(values_list)
        if i == 0:
            result.append(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{values_block};\n")
        else:
            result.append(f"\nINSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{values_block};\n")
    
    return "\n".join(result)

def save_to_csv(data_dict: Dict, output_dir: str = "astronomy_data_csv"):
    """Сохраняет данные в CSV файлы"""
    os.makedirs(output_dir, exist_ok=True)
    
    datasets = [
        ("catalogs", data_dict.get('catalogs', []), ["ID_Catalog", "Count", "CatalogName"]),
        ("educational_institutions", data_dict.get('edu_institutions', []), ["ID_Organisation", "Type", "Country", "Budget", "Organisation"]),
        ("research_organisations", data_dict.get('research_orgs', []), ["ID_Organisation", "Type", "Country", "Budget", "Organisation"]),
        ("scientists", data_dict.get('scientists', []), ["Person", "Country", "Proffesion", "Graduate", "ID_Organisation", "ID_Catalog"]),
        ("amateurs", data_dict.get('amateurs', []), ["Person", "Country", "Age", "ID_Organisation", "ID_Catalog"]),
        ("telescopes", data_dict.get('telescopes', []), ["Telescope", "Type", "ID_Organisation", "Year", "Spot", "ID_Catalog"]),
        ("objects", data_dict.get('objects', []), ["ID_Catalog", "Type", "Declension", "Size", "Magnitude", "Object"])
    ]
    
    for name, data, columns in datasets:
        if data:
            with open(f"{output_dir}/{name}.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=columns)
                writer.writeheader()
                writer.writerows(data)
            print(f"  • {name}.csv ({len(data):,} записей)")

def main():
    print("=" * 60)
    print("ГЕНЕРАТОР ДАННЫХ ДЛЯ АСТРОНОМИЧЕСКОЙ БАЗЫ ДАННЫХ")
    print("=" * 60)
    
    counts = {
        "catalogs": 500,
        "edu_institutions": 500,
        "research_orgs": 200,
        "scientists": 5000,
        "amateurs": 10000,
        "telescopes": 500,
        "objects": 200000
    }
    
    # Создаем генератор
    generator = DataGenerator()
    
    print("\nГенерация данных (с учетом зависимостей по FK):\n")
    
    generator.generate_catalogs(counts["catalogs"])
    generator.generate_educational_institutions(counts["edu_institutions"])
    generator.generate_research_organisations(counts["research_orgs"])
    
    generator.generate_scientists(counts["scientists"])
    generator.generate_amateurs(counts["amateurs"])
    generator.generate_telescopes(counts["telescopes"])
    generator.generate_objects(counts["objects"])
    
    print("\nГенерация SQL скрипта...")
    
    sql = "-- ===========================================\n"
    sql += "-- АСТРОНОМИЧЕСКАЯ БАЗА ДАННЫХ\n"
    sql += "-- Сгенерированные данные\n"
    sql += "-- ===========================================\n\n"
    
    sql += "CREATE SCHEMA IF NOT EXISTS Astronomy;\n\n"
    sql += "SET search_path TO Astronomy;\n\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 1. Таблица: Catalog (независимая)\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Catalog", ["ID_Catalog", "Count", "CatalogName"], 
                               generator.data.get('catalogs', []))
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 2. Таблица: Educational_institution (независимая)\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Educational_institution", ["ID_Organisation", "Type", "Country", "Budget", "Organisation"], 
                               generator.data.get('edu_institutions', []))
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 3. Таблица: Research_organisation (независимая)\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Research_organisation", ["ID_Organisation", "Type", "Country", "Budget", "Organisation"], 
                               generator.data.get('research_orgs', []))
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 4. Таблица: Scientist\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Scientist", ["Person", "Country", "Proffesion", "Graduate", "ID_Organisation", "ID_Catalog"], 
                               generator.data.get('scientists', []), batch_size=1000)
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 5. Таблица: Amateur_astronomer\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Amateur_astronomer", ["Person", "Country", "Age", "ID_Organisation", "ID_Catalog"], 
                               generator.data.get('amateurs', []), batch_size=1000)
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 6. Таблица: Automatic_telescope\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Automatic_telescope", ["Telescope", "Type", "ID_Organisation", "Year", "Spot", "ID_Catalog"], 
                               generator.data.get('telescopes', []))
    sql += "\n"
    
    sql += "-- ===========================================\n"
    sql += "-- 7. Таблица: Object\n"
    sql += "-- ===========================================\n"
    sql += generate_sql_insert("Object", ["ID_Catalog", "Type", "Declension", "Size", "Magnitude", "Object"], 
                               generator.data.get('objects', []), batch_size=5000)
    
    with open("astronomy_data.sql", "w", encoding="utf-8") as f:
        f.write(sql)
    
    print("\n💾 Сохранение CSV файлов...")
    save_to_csv(generator.data)
    
    print("\n" + "=" * 60)
    print("ГЕНЕРАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
    print("=" * 60)
    print("\nСТАТИСТИКА СГЕНЕРИРОВАННЫХ ДАННЫХ:")
    print("-" * 40)
    print(f"  • Каталоги:                          {len(generator.data.get('catalogs', [])):,}")
    print(f"  • Образовательные учреждения:        {len(generator.data.get('edu_institutions', [])):,}")
    print(f"  • Исследовательские организации:     {len(generator.data.get('research_orgs', [])):,}")
    print(f"  • Ученые:                            {len(generator.data.get('scientists', [])):,}")
    print(f"  • Астрономы-любители:                {len(generator.data.get('amateurs', [])):,}")
    print(f"  • Автоматические телескопы:          {len(generator.data.get('telescopes', [])):,}")
    print(f"  • Объекты космоса:                   {len(generator.data.get('objects', [])):,}")
    print("-" * 40)
    total = sum(len(v) for v in generator.data.values())
    print(f"  • ВСЕГО ЗАПИСЕЙ:                    {total:,}")
    print("\nВЫХОДНЫЕ ФАЙЛЫ:")
    print(f"  • astronomy_data.sql - SQL скрипт с INSERT запросами")
    print(f"  • astronomy_data_csv/ - CSV файлы для каждой таблицы")
    print("=" * 60)

if __name__ == "__main__":
    random.seed(42)
    main()