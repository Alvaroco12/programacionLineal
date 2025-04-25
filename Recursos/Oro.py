from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData

# Crear la conexión a la base de datos SQLite
engine = create_engine('sqlite:///unidades.db', echo=True)
metadata = MetaData()

# Definir la tabla
unidades = Table(
    'unidades', metadata,
    Column('id', Integer, primary_key=True),
    Column('nombre', String, nullable=False),
    Column('comida', Integer, nullable=False),
    Column('madera', Integer, nullable=False),
    Column('oro', Integer, nullable=False),
    Column('poder', Integer, nullable=False)
)

# Crear la tabla en la base de datos
metadata.create_all(engine)

# Insertar los datos
with engine.connect() as connection:
    connection.execute(unidades.insert(), [
        {'nombre': 'Espadachín', 'comida': 60, 'madera': 20, 'oro': 0, 'poder': 70},
        {'nombre': 'Arquero', 'comida': 80, 'madera': 10, 'oro': 40, 'poder': 95},
        {'nombre': 'Jinete', 'comida': 140, 'madera': 0, 'oro': 100, 'poder': 230}
    ])

print("Datos guardados correctamente.")