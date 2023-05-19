from mrjob.job import MRJob
from mrjob.step import MRStep


class MRPeliculas(MRJob):

    # Configurar argumentos adicionales
    def configure_args(self):
        super(MRPeliculas, self).configure_args()
        self.max_date = None
        self.min_date = None
        self.min_rating_date = None
        self.max_rating_date = None

    # Función de mapeo: emitir pares clave-valor para cada línea del archivo de entrada
    def mapper(self, _, line):
        # Dividir la línea en campos
        user, movie, rating, genre, date = line.split(',')
        # Emitir el ID de usuario y el rating como clave-valor
        yield ('user', user), float(rating)
        # Emitir la fecha y un contador como clave-valor
        yield ('date', date), 1
        # Emitir el ID de la película y el rating como clave-valor
        yield ('movie', movie), float(rating)
        # Emitir la fecha y el rating como clave-valor
        yield ('rating_date', date), float(rating)
        # Emitir el género y el rating como clave-valor
        yield ('genre', genre), float(rating)

    # Función de reducción: calcular resultados a partir de los pares clave-valor emitidos por la función de mapeo
    def reducer(self, key, values):
        # Si la clave es 'user'
        if key[0] == 'user':
            total = 0
            num = 0
            for value in values:
                total += value
                num += 1
            # Calcular el número de películas vistas por cada usuario y el promedio de calificación para cada usuario
            yield key[1], (num, total/num, "N MOV SEE BY US, AVR RTG")
        # Si la clave es 'date'
        elif key[0] == 'date':
            total = sum(values)
            # Calcular el total de películas vistas en cada fecha
            yield key[0], (key[1], total)
        # Si la clave es 'movie'
        elif key[0] == 'movie':
            total = 0
            num = 0
            for value in values:
                total += value
                num += 1
            # Calcular el número de usuarios que han visto cada película y el promedio de calificación para cada película
            yield key[1], (num, total/num, "N US that see a MV, AVR RTG")
        # Si la clave es 'rating_date'
        elif key[0] == 'rating_date':
            total = 0
            num = 0
            for value in values:
                total += value
                num += 1
            # Calcular el promedio de calificación para cada fecha
            yield key[0], (key[1], total/num)
        # Si la clave es 'genre'
        elif key[0] == 'genre':
            total = 0
            num = 0
            for value in values:
                total += value
                num += 1
            # Calcular el promedio de calificación para cada género
            yield key[1], (total/num)

    # Definir las etapas del trabajo de MapReduce
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_max_min)
        ]

    # Función de reducción para calcular máximos y mínimos a partir de los resultados emitidos por la primera etapa de reducción.
    def reducer_max_min(self, key, values):
        # Si la clave es 'date'
        if key == 'date':
            values = list(values)
            if values:
                max_date = max(values, key=lambda x: x[1])
                min_date = min(values, key=lambda x: x[1])
                self.max_date = max_date[0]
                self.min_date = min_date[0]
                yield 'Max Date', (max_date)
                yield 'Min Date', (min_date)
        # Si la clave es 'rating_date'
        elif key == 'rating_date':
            values = list(values)
            if values:
                max_rating_date = max(values, key=lambda x: x[1])
                min_rating_date = min(values, key=lambda x: x[1])
                self.max_rating_date = max_rating_date[0]
                self.min_rating_date = min_rating_date[0]
                yield 'Max Rating Date', max_rating_date
                yield 'Min Rating Date', min_rating_date
        # Si la clave es 'genre'
        elif key == 'genre':
            values = list(values)
            if values:
                max_genre_rating = max(values)
                min_genre_rating = min(values)
                yield 'Max Genre Rating', (key, max_genre_rating)
                yield 'Min Genre Rating', (key, min_genre_rating)
        else:
            for value in values:
                yield key, value


if __name__ == '__main__':
    MRPeliculas.run()
