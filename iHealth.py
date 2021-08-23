#Iniciamos com uma apresentação do aplicativo.
print('-' * 100)
print('                                 iHelth')
print('-' * 100)
print('     iHealth is an system that try to help you in times of need or emergency \nwhen you have a suspected illness, when you are not feeling well, or have suffered\n some trauma that and need hospital care.')
print('     To get started, we need some data from you or the person who needs assistance.\n It is a quick and necessary screening so that the hospital professionals can better\n understand the problem to be treated.')
print('-' * 100)
 
 
# Em seguida, criamos com uma função Menu, dando
# as opções para o usuário começar a responder as questões da triagem.
def menu():
    print('-' * 100)
    print('                                 MENU')
    print('-' * 100)
    print('Press the number 1 to star answering the questions, than come back to menu to answer the rest.')
    print("[1] - Patient personal Data.")
    print("[2] - Patient adress.")
    print("[3] - Patient problem.")
    print("[4] - Patient Status.")
 
    res = int(input("Option: "))
    if res == 1:
        personaldata()
    elif res == 2:
        location()
    elif res == 3:
        illness()
    elif res == 4:
        statusatendimento()
    else:
        while res != (1,2,3,4):
          return res
 
 
# Aqui foi usado uma função para guardar os dados pessoais do paciente: nome, idade, sexo, RG, estado civil,
# nome e RG do cônjuge, e se o paciente tem plano de saúde. O ".title" vai fazer com que seu nome fique com
# as primeiras letras da cada palavra em maiúsclo, "upper" para fazer com que o UF fique em maiúsculo
def personaldata():
    print('-' * 100)
    print("Here you will answer some questions about the patien's pesonal data.")
    print('-' * 100)
    name = input('Write your full name?: ').title()
    age = int(input('How old are you?(Use numbers. Ex.: 25): '))
    sex = input('What is your gender?(Male or Female): ').title()
    colorskin = input('What is yor skin color?: ').title()
    ID = int(input('Write your ID number: '))
    CPF = int(input('White your Social Security Number: )'))
    telephone = int(input('Patient phone number:  '))
    maritalstate = input('Is the patient married? (Yes or No): ')
    if maritalstate == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
      partnername = input("What is your partner's full name?: ").title()
      partnerID = int(input("Write your partner's ID number: "))
      partnertelephone = int(input('Partner phone number:  '))
    healthplan = input('Do your have private healthcare?(Yes or No): ')
    if healthplan == ('yes' or 'YES' or 'Yes' or 'Y'):
      healthcarename = input('What is your private health care name?: ').title()
      
      
menu()
 
 
# Esta função foi criada para o paciente colocar os dados do seu endereço, contato e o nome do acompanhante caso seja necessário.
def location():
    print('-' * 100)
    print("Here you will discribe the address where the patinet lives.")
    print('-' * 100)
    address = input('Address (Av. St. etc): ').title()
    complement = input('Complement:  ').title()
    neighborthood = input('Neighborthood: ').title()
    city = input('City/Town: ').title()
    FU = input('Federative Unit (FU): ').upper()
    compainion = input("Do the patient has a companion: ")
    if compainion == ('yes' or 'YES' or 'Yes' or 'Y'):
      compainionname = input("Compainion's name?: ")
      
      
menu()
 
 
# Esta função vai questionar o tipo do problema de saúde que o usuário busca resolver naquele momento: se houve perda de consciência
# se é um caso de envenenamento, se foi acidente de trabalho, se foi alguma colisão automotiva (dentro disto questionar se o paciente
# era o passageiro ou motorista no momento da colisão), se foi atropelamento e em qual local do corpo aconteceu o impacto, se o paciente
# possui algum ferimento ou queimadura. Todas as resposatas é necessário apenas responder Sim ou Não.
def illness():
    trauma = input('Loss of consciousness? (Yes or No): ')
    emec = input('Swallowed something that needs to be put out through vomiting?(Yes or No): ')
    if emec == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
        emeticoproblem = input('What kind?: ')
    workaccident = input('Work accident? (Yes ou No): ')
    if workaccident == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
        accidentkind = input('What kind?: ')
    collision = input('Car collision?: ')
    if collision == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
        position = input('At the time of collision, was the patient passenger or driver?: ')
    injuri = input('Are there any injuries? (Yes or No): ')
    if injuri == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
        injuriplace = input('Which part of the body is injured?: ')
    burn = input('Is there burn body parts? (Yes or No): ')
    if burn == ('yes' or 'y' or 'YES' or 'Yes' or 'Y'):
      burnplace = input('Which part of the body is burned?: ')
      
      
menu()
 
 
# Esta função informa as cores correspondente a gravidade do problema do paciente e questiona ao usuário em qual das 4 opções
# qual mais tem relação com seu problema. Foi usado o laço/loop para que o paciente não escolha uma opção fora das oferecidas.
def statusatendimento():
    print("We need to be aware of the patient's severity.  For this, we divided into four colors some of the \nmost common problems in hospital screening.  Carefully read each description of each table.  \nThen mention some or some of the problems and which color you believe is ideal for the patient.:")
    print('-' * 100)
    print('                                 [1]Blue')
    blue = print('-Complaints without acute changes; \n-Necessary procedures: dressing, changing dressings or requesting a prescription.')
    print('-' * 100)
 
    print('                                 [2]Green')
    print('-Age over 60 years or children, without any clinical changes;\n-Disability of any nature, no clinical changes;\n-Asthma history but no crisis;\n-Migraine;\n-Earache;\n-Mild abdominal pain, no change in vital signs;\n-Vaginal bleeding, no abdominal pain;\n-Vomiting and diarrhea, no signs of dehydration;\n-Abscesses;\n-Neurovegetative disorders;\n-Backache;\n-Gastroenteritis without changes in vital signs;\n-Orthopedic complications.')
    print('-' * 100)
 
    print('                                 [3]Yellow')
    print('-Sudden onset severe headache;\n-Acute changes in behavior, agitation and mental confusion, fainting;\n-Seizure history;\n-Severe chest pain;\n-Asthmatic crisis or respiratory distress;\n-Diabetic plus sweating, mental status changes, blurred vision, fever, vomiting, tachypnea, tachycardia;\n-Changes in vital signs in symptomatic patients;\n-Recent history of melena or hermatemesis or enterorrhagia;\n-Epistaxis;\n-Severe pain of any kind;\n-Vaginal bleeding with abdominal pain;\n-Nausea, vomiting and persistent diarrhea plus signs of severe dehydration;\n-High fever (39/40°C);\n-Dislocations, sprains more intense pain;\n-Accidents by poisonous animals;\n-Bronchospasm.')
    print('-' * 100)
 
    print('                                 [4]Red')
    print('-Polytrauma ;\n-Big burns;\n-Consciousness alteration;\n-Spinal Injury;\n-Severe respiratory distress;\n-Chest pain plus shortness of breath plus cyanosis;\n-Vomiting plus loss of consciousness or chest pain for more than 30 minutes;\n-Piercing in the chest, abdomen or head;\n-Convulsive crisis;\n-Exogenous poisonings or suicide attempts;\n-Anaphylaxis or allergic reactions plus shortness of breath;\n-Hyper or hypoglycemia (diagnosed);\n-Cardiorespiratory arrest;\n-Changes in vital signs plus symptoms (diagnosed);\n-Uncontrollable bleeding;\n-Fractures, injuries (cuts).')
    print('-' * 100)
 
    problems = input('Which of the problems mentioned above is the patient aware of being a carrier?: ')
    num = int(input('Choose a number from 1 to 4: '))
    description = input("Describe the patient's problem with your words: ")
    while num < 1 or num > 4:
        num = int(input("Choose a number from 1 to 4: ."))
        
        
menu()
