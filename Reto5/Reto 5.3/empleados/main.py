from mrjob.job import MRJob
from mrjob.step import MRStep


class MREmployee(MRJob):
    def __init__(self, *args, **kwargs):
        super(MREmployee, self).__init__(*args, **kwargs)
        self.options.line_num = 0

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, line):
        # Extraer los campos del archivo de entrada
        idemp, sector, salary, year = line.split(',')
        salary = float(salary)

        # Generar pares clave-valor para el salario promedio por SE
        yield ('SE', sector), ('salary', salary)

        # Generar pares clave-valor para el salario promedio por Empleado
        yield ('Emp', idemp), ('salary', salary)

        # Generar pares clave-valor para el número de SE por Empleado
        yield ('Emp', idemp), ('sector', sector)

    def reducer(self, key, values):
        total = 0
        count = 0
        sectors = set()

        for value in values:
            if value[0] == 'salary':
                total += value[1]
                count += 1
            elif value[0] == 'sector':
                sectors.add(value[1])

        if key[0] == 'SE':
            # Calcular el salario promedio por SE
            yield ('Average Salary By SE ' + key[1] + ':'), total / count
        elif key[0] == 'Emp':
            # Calcular el salario promedio por Empleado y el número de SE por Empleado
            yield ('Average Salary By Emp ' + key[1] + ':'), total / count
            yield ('SE number that had EMP ' + key[1] + ':'), len(sectors)


if __name__ == '__main__':
    MREmployee.run()
