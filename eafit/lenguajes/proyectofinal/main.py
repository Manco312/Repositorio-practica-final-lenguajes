from eafit.lenguajes.proyectofinal.concurso.concurso import Concurso


def main():
    print("-" * 50)
    print(f'Bienvenido al Registro de las emisiones del programa "¿Quién quiere ser millonario?"')
    print(f'A continuación encontrará un registro de la información por cada emisión diaria de esta semana')
    print(f'Finalmente, un cálculo del dinero total entregado por la semana')

    concurso = Concurso()

    concurso.generarConcurso()
    concurso.visualizarRegistroConcurso()


if __name__ == '__main__':
    main()
