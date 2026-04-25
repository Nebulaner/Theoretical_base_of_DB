-- Сгенерированные данные для базы данных
-- Таблица: Object
INSERT INTO Object (ObjectName, Type, Declension, Size, Magnitude) VALUES
('Milky Way_4', 'Star', -45.919, 16.75, -24.88),
('Black Eye Galaxy_12', 'Supernova Remnant', -14.054, 3.59, -19.07),
('Black Eye Galaxy_78', 'Galaxy', 11.024, 85.93, 5.07),
('Vega_29', 'Globular Cluster', 16.068, 97.13, -29.68),
('Orion Nebula_90', 'Globular Cluster', -28.755, 18.67, 17.86),
('Sirius_14', 'Galaxy', -21.613, 43.08, -12.8),
('Betelgeuse_6', 'Globular Cluster', 6.521, 116.77, -11.07),
('Black Eye Galaxy_38', 'Supernova Remnant', 69.381, 43.4, -20.39),
('Milky Way_6', 'Nebula', 49.152, 118.23, 12.77),
('Milky Way_49', 'Star', -8.386, 100.09, -21.87),
('Sirius_27', 'Star', 36.328, 82.03, -26.43),
('Orion Nebula_69', 'Nebula', -60.588, 45.54, 19.48),
('Black Eye Galaxy_29', 'Star', 61.713, 93.12, -18.55),
('Andromeda_41', 'Globular Cluster', -41.807, 25.33, 17.15),
('Sirius_28', 'Globular Cluster', -18.786, 109.75, -7.06),
('Betelgeuse_18', 'Nebula', 44.098, 64.68, 7.35),
('Vega_75', 'Globular Cluster', -24.841, 119.68, -23.08),
('Crab Nebula_12', 'Galaxy', 64.999, 18.35, -22.0),
('Vega_77', 'Galaxy', -20.742, 71.51, -6.6),
('Betelgeuse_71', 'Galaxy', 32.451, 13.76, 14.24);

-- Таблица: Educational_institution
INSERT INTO Educational_institution (Organisation, Type, Country, Budget) VALUES
('Sorbonne 11', 'University', 'Japan', 43477090302.0),
('Moscow State University 1', 'Institute', 'Canada', 76196457943.0),
('Beijing University 4', 'Institute', 'Sweden', 63895310537.0),
('Stanford University 7', 'College', 'Russia', 76251317497.0),
('Beijing University 17', 'University', 'Australia', 32416281544.0),
('Harvard University 4', 'Institute', 'India', 98532152573.0),
('Sorbonne 8', 'University', 'Germany', 87801081911.0),
('MIT 3', 'Academy', 'Sweden', 6922182634.0),
('Beijing University 5', 'College', 'Spain', 47528762527.0),
('Beijing University 6', 'Institute', 'Canada', 87243431675.0),
('Tokyo University 7', 'College', 'Netherlands', 31172317414.0),
('Heidelberg University 15', 'Academy', 'UK', 24791313461.0),
('MIT 11', 'University', 'Australia', 55392598321.0),
('Stanford University 8', 'University', 'UK', 70784386814.0),
('Harvard University 8', 'University', 'India', 3142264392.0);

-- Таблица: Scientist
INSERT INTO Scientist (Person, Organisation, Country, Proffesion, Graduate) VALUES
('Yuki Tanaka 10', 'Beijing University 2', 'Japan', 'Stellar Astronomy', 'Master'),
('Carlos Fernandez 17', 'Stanford University 5', 'Italy', 'Cosmology', 'Professor'),
('Pierre Dubois 25', 'MIT 1', 'Spain', 'Stellar Astronomy', 'Bachelor'),
('Pierre Dubois 53', 'Moscow State University 1', 'Spain', 'Astrophysics', 'PhD'),
('Pierre Dubois 94', 'Heidelberg University 1', 'Germany', 'Cosmology', 'Master'),
('Carlos Fernandez 58', 'Cambridge University 4', 'France', 'Planetary Science', 'Professor'),
('Maria Garcia 10', 'Moscow State University 5', 'UK', 'Astrophysics', 'Doctor of Science'),
('John Smith 12', 'Oxford University 2', 'China', 'Stellar Astronomy', 'Professor'),
('Maria Garcia 52', 'Harvard University 2', 'China', 'Astrophysics', 'Professor'),
('Hans Mueller 59', 'Sorbonne 4', 'Netherlands', 'Radio Astronomy', 'Professor'),
('Ivan Petrov 25', 'Sorbonne 2', 'USA', 'Radio Astronomy', 'Doctor of Science'),
('John Smith 96', 'Heidelberg University 1', 'USA', 'Radio Astronomy', 'Professor'),
('Carlos Fernandez 68', 'Cambridge University 1', 'Canada', 'Astrophysics', 'Master'),
('Jane Doe 77', 'MIT 2', 'China', 'Astrophysics', 'Doctor of Science'),
('Maria Garcia 75', 'Stanford University 1', 'Australia', 'Astrophysics', 'Professor'),
('Olga Smirnova 73', 'Beijing University 3', 'India', 'Planetary Science', 'Master'),
('Yuki Tanaka 31', 'Sorbonne 4', 'France', 'Planetary Science', 'Professor'),
('Yuki Tanaka 97', 'MIT 1', 'Italy', 'Radio Astronomy', 'Doctor of Science'),
('Jane Doe 10', 'Beijing University 2', 'Canada', 'Planetary Science', 'Master'),
('Yuki Tanaka 9', 'Oxford University 3', 'Japan', 'Cosmology', 'Professor'),
('Carlos Fernandez 91', 'Sorbonne 5', 'Switzerland', 'Radio Astronomy', 'PhD'),
('Carlos Fernandez 39', 'MIT 2', 'Japan', 'Astrophysics', 'PhD'),
('Carlos Fernandez 20', 'Sorbonne 3', 'Australia', 'Cosmology', 'Bachelor'),
('Maria Garcia 88', 'Sorbonne 5', 'Italy', 'Planetary Science', 'PhD'),
('Jane Doe 82', 'Tokyo University 3', 'USA', 'Astrophysics', 'Bachelor');

-- Таблица: Research_organisation
INSERT INTO Research_organisation (Organisation, Type, Country, Budget) VALUES
('Institute Betelgeuse 6', 'International', 'Canada', 35283519504.0),
('Foundation Andromeda 4', 'State', 'India', 34551135678.0),
('Institute Black Eye Galaxy 2', 'Mixed', 'Australia', 27626478575.0),
('Lab Orion Nebula 2', 'Mixed', 'Russia', 44949124946.0),
('RI Sirius 7', 'Private', 'Spain', 5140129687.0),
('Foundation Vega 20', 'Private', 'India', 46494085844.0),
('Institute Orion Nebula 29', 'International', 'USA', 8968443491.0),
('Center Vega 26', 'Private', 'Japan', 7960312550.0),
('RI Vega 28', 'State', 'Sweden', 23534765709.0),
('Institute Crab Nebula 12', 'Mixed', 'Sweden', 39767377285.0),
('Institute Pleiades 1', 'Private', 'China', 16413433429.0),
('RI Betelgeuse 12', 'International', 'Spain', 49057493785.0);

-- Таблица: Automatic_telescope
INSERT INTO Automatic_telescope (Telescope, Type, Owner, Year, Spot) VALUES
('FAST-22', 'Optical', 'MIT 5', '1966-01-08', 'India'),
('ALMA-3', 'Optical', 'Stanford University 7', '1981-01-05', 'South Africa'),
('Fermi-39', 'Gamma-ray', 'MIT 7', '2001-09-23', 'Canary Islands'),
('ALMA-3', 'X-ray', 'Harvard University 9', '2022-05-10', 'China'),
('VLT-24', 'X-ray', 'MIT 6', '2005-11-27', 'South Africa'),
('Webb-47', 'Infrared', 'Beijing University 5', '2009-10-30', 'Arizona'),
('Chandra-26', 'Infrared', 'Beijing University 3', '1967-03-19', 'Arizona'),
('Fermi-44', 'Radio', 'Stanford University 10', '1976-12-31', 'Arizona'),
('FAST-1', 'Infrared', 'Sorbonne 4', '1988-07-26', 'India'),
('Gemini-42', 'Infrared', 'Moscow State University 8', '1989-09-01', 'Canary Islands'),
('FAST-31', 'Radio', 'State 2', '1975-06-18', 'China'),
('Gemini-22', 'Optical', 'International 4', '2010-05-12', 'Australia'),
('VLT-13', 'Radio', 'Harvard University 1', '1971-12-20', 'Puerto Rico'),
('Gemini-50', 'Optical', 'Moscow State University 7', '2006-07-02', 'India'),
('VLT-46', 'X-ray', 'Moscow State University 7', '1971-11-21', 'Chile');

-- Таблица: Amateur_astronomer
INSERT INTO Amateur_astronomer (Person, Country, Age) VALUES
('Bob Williams 915', 'Switzerland', 29),
('George Costanza 225', 'France', 82),
('Helen Keller 52', 'Canada', 47),
('Alice Brown 468', 'France', 75),
('Fiona Gallagher 973', 'Switzerland', 72),
('George Costanza 851', 'India', 73),
('Charlie Davis 762', 'Sweden', 76),
('Helen Keller 266', 'Switzerland', 47),
('Ethan Hunt 785', 'Switzerland', 82),
('Helen Keller 642', 'Germany', 51),
('Helen Keller 80', 'Netherlands', 52),
('Diana Prince 279', 'Russia', 56),
('Alice Brown 142', 'France', 45),
('George Costanza 711', 'France', 43),
('Alice Brown 425', 'China', 58),
('Helen Keller 426', 'USA', 42),
('George Costanza 399', 'India', 18),
('George Costanza 489', 'USA', 61);

-- Таблица: Catalog
INSERT INTO Catalog (CatalogName, Size, Year) VALUES
('PGC-772', 25568, '1900-09-28'),
('HIP-766', 48154, '1991-12-22'),
('Tycho-920', 14463, '1950-06-01'),
('Caldwell-280', 28572, '1948-07-23'),
('NGC-399', 22038, '1890-03-10'),
('Messier-861', 30640, '1691-08-07'),
('Tycho-547', 1777, '1882-10-19'),
('Tycho-578', 43460, '1619-06-14'),
('IC-659', 28099, '1697-05-23'),
('2MASS-187', 3305, '1786-09-20'),
('SDSS-336', 13881, '1926-05-08'),
('UGC-346', 49897, '1872-02-09');
