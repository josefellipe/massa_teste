from faker import Faker

#Criar uma instância com dados Br
fake = Faker('pt_BR')

def create_person():
    #Gerar dados fictícios
    person = {
        "name" : fake.name(),
        "phone" : fake.phone_number(),
        "cpf" : fake.cpf(),
        "sexo" : fake.random_element(elements=('M', 'F')), # Cria randomicamente os elementos listados
        "state" : fake.estado(),
        "city" : fake.city()
    }

    return person

