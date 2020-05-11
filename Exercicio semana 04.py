users = [
 {"id": 0, "name": "Hero"},
 {"id": 1, "name": "Dunn"},
 {"id": 2, "name": "Sue"},
 {"id": 3, "name": "Chi"},
 {"id": 4, "name": "Thor"},
 {"id": 5, "name": "Clive"},
 {"id": 6, "name": "Hicks"},
 {"id": 7, "name": "Devin"},
 {"id": 8, "name": "Kate"},
 {"id": 9, "name": "Klein"},
]


#print(users)

friendships = [
 (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

#lista de amigos vazia para cada usuário da rede
for user in users:
    user["friends"] = []

#percorre a lista de tuplas adicionando o usuário i à lista do usuário j e vice-versa

#for friendship in friendships:
#    users[friendship[0]]['friends'].append(users[friendship[1]])
#    users[friendship[1]]['friends'].append(users[friendship[0]])

#tuple unpacking
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

#print(users[0])

def number_of_friends(user):
    return len(user['friends'])

#print(number_of_friends(users[2]))

#[2, 3, 3, 2, 3] quantidade de amizades

#para cada usuario na colecao usuarios, eu quero uma expressão: number_of_friends
lista = [number_of_friends(user) for user in users]
#print(lista)

total_connections = sum(number_of_friends(user) for user in users)
#print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users

#print(avg_connections)

#[(0, 2), (1, 3), (2, 3)]


number_of_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

#print(number_of_friends_by_id)

#sorted - função de mais alta ordem, ou seja, pode receber função como parâmetro e devolver função

lista_ordenada = sorted(number_of_friends_by_id, key = lambda num_friends: num_friends[1], reverse=True )
#print(lista_ordenada)

def friends_of_friends_ids_bad(user):
    return [
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
    ]

#funcão decisora = função que toma uma decisão

def not_the_same (user, other_user):
    return user['id'] != other_user['id']


def not_friend(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user['friends'])

def friends_of_friends_ids (user):
    return set([
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friend(user, foaf)
    ])

#[True, True, False]
#[True, True, True]



# ATIVIDADE SEMANA 04

#1 Adicione os atributos sexo e idade aos usuários da rede

for user in users:
    user['sexo'], user['idade'] = '', ''

users[0]['sexo'] = 'm'
users[1]['sexo'] = 'm'
users[2]['sexo'] = 'f'
users[3]['sexo'] = 'm'
users[4]['sexo'] = 'm'
users[5]['sexo'] = 'm'
users[6]['sexo'] = 'm'
users[7]['sexo'] = 'm'
users[8]['sexo'] = 'f'
users[9]['sexo'] = 'm'

#2 Monte um dicionário que tem como chave o id do usuário e como valor uma tupla. O primeiro
#elemento da tupla deve ter a quantidade de amigos do sexo masculino e o segundo elemento da
#tupla deve ter a quantidade de amigos do sexo feminino. Escreva funções conforme achar
#apropriado.

def number_of_friends_sexo (user, sexo):
    s = 0
    for friend in user['friends']:

        if(friend['sexo']== sexo):
            s = s+1
    return s    

dicionario_num_friends_sexo_by_id = {user['id']: (number_of_friends_sexo(user, 'm'), 
                                       number_of_friends_sexo(user, 'f')) for user in users}                                       

print(dicionario_num_friends_sexo_by_id)