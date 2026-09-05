"""
車種スペックの静的データベースと、VINの製造者識別部(WMI)テーブル。

WMI(World Manufacturer Identifier, ISO 3780)は国際公開規格であり、
VINの先頭3桁から製造者・生産国を機械的に判定できる。ただし
「年式・排気量・馬力」等の詳細スペックはVIN全体を解析する必要があり、
それには各メーカーの非公開コード体系(有料データベース)が要る。
そのため本APIは「VIN→メーカー/生産国」はアルゴリズムで、
「車名→詳細スペック」は内部データベースで、それぞれ完結させている。
"""

# WMI(先頭3桁)の一部抜粋。ISO 3780 で公開されている体系の代表例。
WMI_TABLE = {
    "1HG": {"manufacturer": "Honda", "country": "United States"},
    "1HD": {"manufacturer": "Harley-Davidson", "country": "United States"},
    "1G1": {"manufacturer": "Chevrolet", "country": "United States"},
    "1FA": {"manufacturer": "Ford", "country": "United States"},
    "1N4": {"manufacturer": "Nissan", "country": "United States"},
    "2HG": {"manufacturer": "Honda", "country": "Canada"},
    "3VW": {"manufacturer": "Volkswagen", "country": "Mexico"},
    "JHM": {"manufacturer": "Honda", "country": "Japan"},
    "JTD": {"manufacturer": "Toyota", "country": "Japan"},
    "JT2": {"manufacturer": "Toyota", "country": "Japan"},
    "JN1": {"manufacturer": "Nissan", "country": "Japan"},
    "JM1": {"manufacturer": "Mazda", "country": "Japan"},
    "JF1": {"manufacturer": "Subaru", "country": "Japan"},
    "KMH": {"manufacturer": "Hyundai", "country": "South Korea"},
    "KNA": {"manufacturer": "Kia", "country": "South Korea"},
    "WVW": {"manufacturer": "Volkswagen", "country": "Germany"},
    "WBA": {"manufacturer": "BMW", "country": "Germany"},
    "WDB": {"manufacturer": "Mercedes-Benz", "country": "Germany"},
    "WAU": {"manufacturer": "Audi", "country": "Germany"},
    "VF1": {"manufacturer": "Renault", "country": "France"},
    "VF3": {"manufacturer": "Peugeot", "country": "France"},
    "ZFA": {"manufacturer": "Fiat", "country": "Italy"},
    "SAJ": {"manufacturer": "Jaguar", "country": "United Kingdom"},
    "SAL": {"manufacturer": "Land Rover", "country": "United Kingdom"},
}

CARS = [
    {"make": "Toyota", "model": "Corolla", "year_range": "2020-2026", "engine": "1.8L I4", "horsepower": 169},
    {"make": "Toyota", "model": "Camry", "year_range": "2018-2026", "engine": "2.5L I4", "horsepower": 203},
    {"make": "Toyota", "model": "RAV4", "year_range": "2019-2026", "engine": "2.5L I4", "horsepower": 203},
    {"make": "Honda", "model": "Civic", "year_range": "2022-2026", "engine": "2.0L I4", "horsepower": 158},
    {"make": "Honda", "model": "Accord", "year_range": "2023-2026", "engine": "1.5L Turbo I4", "horsepower": 192},
    {"make": "Honda", "model": "CR-V", "year_range": "2023-2026", "engine": "1.5L Turbo I4", "horsepower": 190},
    {"make": "Nissan", "model": "Altima", "year_range": "2019-2026", "engine": "2.5L I4", "horsepower": 188},
    {"make": "Mazda", "model": "Mazda3", "year_range": "2019-2026", "engine": "2.5L I4", "horsepower": 191},
    {"make": "Subaru", "model": "Impreza", "year_range": "2017-2026", "engine": "2.0L H4", "horsepower": 152},
    {"make": "Volkswagen", "model": "Golf", "year_range": "2015-2024", "engine": "1.4L Turbo I4", "horsepower": 147},
    {"make": "BMW", "model": "3 Series", "year_range": "2019-2026", "engine": "2.0L Turbo I4", "horsepower": 255},
    {"make": "Mercedes-Benz", "model": "C-Class", "year_range": "2022-2026", "engine": "2.0L Turbo I4", "horsepower": 255},
    {"make": "Audi", "model": "A4", "year_range": "2017-2026", "engine": "2.0L Turbo I4", "horsepower": 201},
    {"make": "Ford", "model": "Mustang", "year_range": "2015-2023", "engine": "5.0L V8", "horsepower": 460},
    {"make": "Chevrolet", "model": "Camaro", "year_range": "2016-2024", "engine": "6.2L V8", "horsepower": 455},
    {"make": "Hyundai", "model": "Elantra", "year_range": "2021-2026", "engine": "2.0L I4", "horsepower": 147},
    {"make": "Kia", "model": "K5", "year_range": "2021-2026", "engine": "1.6L Turbo I4", "horsepower": 180},
]
