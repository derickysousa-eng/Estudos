import random
import sys

# declaração das variaveis para geração do num de protoc
ano = '2026'
numero_aleatorio = random.randrange(100000000, 1000000000)
protocolo = ano + str(numero_aleatorio) 

print("Bem-vindo à Boom Net\n Conectando você ao que importa. 🚀")
nome_do_cliente = input('Me informe seu nome:\n')
 # Verificar/validar o dado preenchido pelo user é um numero e se possui 3 digitos
while True:
    digitos_do_cpf = input('Me informe os 3 primeiros digitos do seu cpf:\n')
    if not digitos_do_cpf.isdigit():
        print("\n❌ Erro: Favor preencher apenas com números.")
    elif len(digitos_do_cpf) != 3:
        print("\n❌ Erro: Favor digitar exatamente 3 números.")
    else:
        break

def fim ():
 while True:
   menu_fim = input('\n Ajudo em algo mais?\n 1 -✅ Sim\n'
   '\n 2 -❌ Não\n')
   if menu_fim == '1':
    return 'menu'
   elif  menu_fim == '2':
    print('\n Atendimento encerrado com sucesso.')
    print(f'O seu protocolo é {protocolo}')
    sys.exit()
   else:
    print('\n Opção inválida.')

def informacao_da_rede():

    ip = f'{random.randrange(100,256)}.{random.randrange(0,256)}.{random.randrange(0,256)}.{random.randrange(0,256)}'
    velocidade = [300,100,200]
    upload = random.randrange(50,200)
    download = upload + 50
    ping = random.randrange(1,20)
    if ping >= 150 :
        print(f'O {ping} ms (Horrivel)')
    elif ping >= 100 :
        print(f'O ping {ping} ms (Ruim)')
    elif ping >= 50 :
        print(f'O ping {ping} ms (Bom)')
    elif ping >= 20 :
        print(f'O ping {ping} ms (Muito bom)')
    else:
        print(f'O ping {ping} ms (Excelente)')
    
    dispositivos = random.randdrange(1,10)

    while True:
      print(f'Olá! Realizamos um teste rápido na sua linha. Aqui estão os dados atuais da sua conexão:')
      print(f'🌐 Status da Conexão: 🟢 ONLINE (Sinal Estável)')
      print(f'🌍 IP Público: {ip}')
      print(f'Velocidade Contratada: {random.choice(velocidade)} Mbps')
      print(f'📱 Dispositivos conectados: {dispositivos}')
      print(f'Download Atual: {download} Mbps | Upload: {upload} Mbps')
      print(f'📡 Ping: {ping} ms')
      fim()

def financeiro():
   while True:
     financeiro_menu = input(
        '1 -📄 Minha Fatura / Extrato\n'
        '2 -🤝 Negociação e Acordos\n'
        '3 -⬅️ Voltar\n'          )
     if financeiro_menu == '1':
        print(f'Olá, {nome_do_cliente}, não foi encontrado nenhum extrato ou fatura em seu nome.')
        print('Peço que verifique se você é realmente o titular da conta.')
        if fim() == 'menu':
         return

     elif financeiro_menu == '2':
      print(f'Olá!{nome_do_cliente} Analisamos o seu cpf e seu nome informado em nosso sistema financeiro.')
      print('Não identificamos nenhuma fatura em aberto ou conta vinculada a este cadastro.')
      if fim() == 'menu':
         return
     elif financeiro_menu == '3':
      break
     else:
      print('Opção Invalida')

def menu_wifi_solucao():
  while True:
    wifi_solucao = input(
      '\nO wifi voltou a funcionar?\n'
      '1 - Sim! Problema resolvido.\n'
      '2 - Não. Continuo com problemas.\n'
      '3 - Voltar\n'                   )
    if wifi_solucao == '1':
         print('\n Atendimento encerrado com sucesso.')
         print(f'O seu protocolo é {protocolo}')
         sys.exit()
    elif wifi_solucao == '2':
        print('\n Foi aberto um chamado para seu problema.')
        print(f'O seu protocolo é {protocolo}, a tratativa varia entre 3 a 5 dias uteis.')
        fim()
    elif wifi_solucao == '3':
          break
    else :
         print('\n Opção inválida.')

def problemas_para_conectar_ao_wi_fi():
    while True:
        menu_wifi = input(
            '\n1 - 🔑 Meu aparelho localiza a rede, mas diz Senha Incorreta ou Erro de Autenticação\n'
            '2 - 📡 A rede Wi-Fi da minha casa sumiu da lista e não aparece de jeito nenhum\n'
            '3 - 🌐 Eu consigo conectar no Wi-Fi, mas aparece Conectado, sem internet\n'
            '4 - ⬅️ Voltar\n'
        )

        if menu_wifi == '1':
            print('Muitas vezes o aparelho guarda um histórico de conexão corrompido. Vamos limpar essa rede:')
            print('1 - Vá nas configurações de Wi-Fi do seu celular/computador.')
            print('2 - Clique no nome da sua rede e selecione "Esquecer Rede" ou "Excluir Rede".')
            print('3 - Desligue o Wi-Fi do aparelho, espere 5 segundos e ligue novamente.')
            print('4 - Clique na sua rede e digite a senha novamente.')
            menu_wifi_solucao()

        elif menu_wifi == '2':
            print('Se o Wi-Fi sumiu, o emissor do modem pode ter travado ou o aparelho está longe demais.')
            print('1 - Aproxime-se do modem.')
            print('2 - Verifique se a luz do Wi-Fi está acesa.')
            print('3 - Se estiver apagada, pressione o botão Wi-Fi/WLAN por 3 segundos.')
            menu_wifi_solucao()

        elif menu_wifi == '3':
            print('Isso significa que seu aparelho conversa com o modem, mas o modem não está recebendo sinal da rua.')
            print('1 - Desconecte o modem da tomada por 30 segundos.')
            print('2 - Aguarde 3 minutos até as luzes estabilizarem.')
            print('3 - Verifique se a luz PON, Internet ou WAN está vermelha.')
            menu_wifi_solucao()

        elif menu_wifi == '4':
            break

        else:
            print('\nOpção inválida.')

def internet_fora_do_ar_ou_lenta():
    while True:
     print('\nEntendi! Vamos resolver isso juntos.')
     print('Na maioria das vezes, a internet volta a funcionar com alguns passos simples.')
     print('\n PASSO 1 - Reiniciar o Roteador')
     print('1. Vá até o modem/roteador.')
     print('2. Retire o aparelho da tomada.')
     print('3. Aguarde 30 segundos.')
     print('4. Ligue novamente e aguarde cerca de 2 minutos.')
     print('\n PASSO 2 - Verificar os Cabos')
     print('1. Verifique se todos os cabos estão bem conectados.')
     print('2. Confira se nenhum cabo está solto.')
     print('\n PASSO 3 - Testar em Outro Dispositivo')
     print('1. Tente acessar a internet por outro celular ou computador.')
     print('2. Verifique se o problema acontece em todos os aparelhos.')

     menu_internet = input(
        '\nQual foi o resultado?\n'
        '1 -✅ Funcionou! A internet voltou ao normal.\n'
        '2 -🐢 Continua lenta.\n'
        '3 -🚨 Continua sem sinal.\n'
        '4 -⬅️ Voltar.\n'
    )

     if menu_internet == '1':
        print('\n Atendimento encerrado com sucesso.')
        print(f'O seu protocolo é {protocolo}')
        sys.exit()
     elif menu_internet == '2':
        print('\n Foi aberto um chamado para seu problema com a lentidão.')
        print(f'O seu protocolo é {protocolo}, a tratativa varia entre 3 a 5 dias uteis.')
        if fim() == 'menu':
         return

     elif menu_internet == '3':
        print('\n Foi aberto um chamado com urgência pela falta de sinal.')
        print(f'O seu protocolo é {protocolo}, a tratativa varia entre 5 a 7 dias uteis.')
        if fim() == 'menu':
         return
     elif menu_internet == '4':
      break
     else:
        print('\n Opção inválida.')

def suporte_tecnico():
 while True:
  menu_suporte_tecnico = input(
    '1 - 📶 Internet fora do ar ou lenta\n'
    '2 - 📡 Problemas para conectar ao Wi-Fi\n'
    '3 - ⬅️ Voltar\n'
     )
  if menu_suporte_tecnico == "1":
    internet_fora_do_ar_ou_lenta()
  elif menu_suporte_tecnico == '2':
   problemas_para_conectar_ao_wi_fi()
  elif menu_suporte_tecnico == '3':
    break
  else:
        print('\n Opção inválida.')

def menu_principal():
 print(f'\nOlá, {nome_do_cliente}! Como podemos te ajudar hoje?')
 while True:
   menu = input(
     '\nSelecione o numero da opção que você necessita de atendimento.\n'
    '1 - 🛠️ Suporte Técnico\n'
    '2 - 💳 Financeiro\n'
    '3 - 🌐 Informações da Rede\n'
    '4 - ❌ Encerrar Atendimento\n'
)
   if menu == '1':
    print('Você acessou o suporte a')
    suporte_tecnico()
   elif menu == '2':
      print('Voce acessou ao financeiro')
      financeiro()
   elif menu == '3':
      informacao_da_rede()
   elif menu == '4':
    print('Obrigado por utilizar a Boom Net!')
    sys.exit()
   else:
        print('\n Opção inválida.')

menu_principal()
