from .person_create import create_person
from tqdm import tqdm


def save_csv(n):
    file = open('massa_teste.csv', 'w') #O 'w' sempre cria um arquivo novo

    text_file = ["name,phone,cpf,sexo,state,city"]
    for i in tqdm(range(n)):
        person = create_person()
        text_file.append(f'{person["name"]},{person["phone"]},{person["cpf"]},{person["sexo"]},{person["state"]},{person["city"]}')

    file.write('\n'.join(text_file))