from mrjob.job import MRJob
from mrjob.step import MRStep


class MRStocks(MRJob):

    def steps(self):
        # Definir los pasos del trabajo de MapReduce
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_final)
        ]

    def mapper(self, _, line):
        # Extraer los campos de cada línea del archivo de entrada
        company, price, date = line.split(',')
        price = float(price)

        # Generar pares clave-valor para cada compañía
        yield company, (price, date)

    def reducer(self, key, values):
        # Inicializar variables para calcular el mínimo y el máximo
        min_price = float('inf')
        max_price = float('-inf')
        min_date = None
        max_date = None
        stable = True
        prev_price = None

        # Iterar sobre los valores para calcular el mínimo y el máximo
        for value in values:
            price, date = value

            if price < min_price:
                min_price = price
                min_date = date

            if price > max_price:
                max_price = price
                max_date = date

            if prev_price is not None and price < prev_price:
                stable = False

            prev_price = price

        # Generar pares clave-valor con los resultados
        yield key, (min_price, min_date, max_price, max_date, stable)

    def reducer_final(self, key, values):
        # Inicializar variable para calcular el "día negro"
        black_day = {}

        # Iterar sobre los valores para calcular todos los resultados
        for value in values:
            min_price, min_date, max_price, max_date, stable = value

            # Generar pares clave-valor para el día con el menor valor y el día con el mayor valor por acción
            yield key + ' - Lowest Value Day:', min_date
            yield key + ' - Highest Value Day:', max_date

            # Generar pares clave-valor para el listado de acciones que siempre han subido o se han mantenido estables
            if stable:
                yield key + ' - Always Up or Stable:', stable

            # Acumular valores para calcular el "día negro"
            if min_date not in black_day:
                black_day[min_date] = 0
            black_day[min_date] += 1

        # Calcular y generar par clave-valor para el "día negro"
        black_day_sorted = sorted(
            black_day.items(), key=lambda x: x[1], reverse=True)
        yield 'Black Day:', black_day_sorted[0][0]


if __name__ == '__main__':
    MRStocks.run()
