import random
import sys
import telebot

# Substitua pelo Token do seu bot gerado no @BotFather
TOKEN = "SEU_TOKEN_AQUI"
bot = telebot.TeleBot(TOKEN)

# Dicionário global para simular as variáveis que eram locais/globais no terminal
# necessário porque o Telegram atende várias pessoas ao mesmo tempo
estado_usuarios = {}

# --- SUA LÓGICA DE VARIÁVEIS INALTERADA ---
ip = f'{random.randrange(100,256)}.{random.randrange(0,256)}.{random.randrange(0,256)}.{random.randrange(0,256)}'
velocidade = [300,100,200]
upload = random.randrange(50,200)
download = upload + 50
ping = random.randrange(1,20)

# Guardamos o texto do ping baseado no seu IF original
txt_ping = ""
if ping >= 150:
    txt_ping = f'O {ping} ms (Horrivel)'
elif ping >= 100:
    txt_ping = f'O ping {ping} ms (Ruim)'
elif ping >= 50:
    txt_ping = f'O ping {ping} ms (Bom)'
elif ping >= 20:
    txt_ping = f'O ping {ping} ms (Muito bom)'
else:
    txt_ping = f'O ping {ping} ms (Excelente)'

dispositivos = random.randrange(1,10)
ano = '2026'
numero_aleatorio = random.randrange(100000000, 1000000000)
protocolo = ano + str(numero_aleatorio)

# --- ADAPTAÇÃO DAS SUAS FUNÇÕES ORIGINAIS PARA O TELEGRAM ---

def fim(message):
    chat_id = message.chat.id
    texto = ('\n Ajudo em algo mais?\n'
             '1 - ✅ Sim\n'
             '2 - ❌ Não\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_fim)

def processa_fim(message):
    chat_id = message.chat.id
    opcao = message.text
    if opcao == '1':
        menu_principal(message)
    elif opcao == '2':
        bot.send_message(chat_id, f'\n Atendimento encerrado com sucesso.\nO seu protocolo é {protocolo}')
        # No Telegram não usamos sys.exit() para não derrubar o bot para os outros usuários
    else:
        bot.send_message(chat_id, '\n Opção inválida.')
        fim(message)

def informacao_da_rede(message):
    chat_id = message.chat.id
    texto = (f'Olá! Realizamos um teste rápido na sua linha. Aqui estão os dados atuais da sua conexão:\n'
             f'🌐 Status da Conexão: 🟢 ONLINE (Sinal Estável)\n'
             f'🌍 IP Público: {ip}\n'
             f'Velocidade Contratada: {random.choice(velocidade)} Mbps\n'
             f'📱 Dispositivos conectados: {dispositivos}\n'
             f'Download Atual: {download} Mbps | Upload: {upload} Mbps\n'
             f'📡 Ping: {txt_ping}\n')
    bot.send_message(chat_id, texto)
    fim(message)

def financeiro(message):
    chat_id = message.chat.id
    texto = ('1 - 📄 Minha Fatura / Extrato\n'
             '2 - 🤝 Negociação e Acordos\n'
             '3 - ⬅️ Voltar\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_financeiro)

def processa_financeiro(message):
    chat_id = message.chat.id
    opcao = message.text
    nome_do_cliente = estado_usuarios[chat_id]['nome']

    if opcao == '1':
        bot.send_message(chat_id, f'Olá, {nome_do_cliente}, não foi encontrado nenhum extrato ou fatura em seu nome.\n'
                                  f'Peço que verifique se você é realmente o titular da conta.')
        fim(message)
    elif opcao == '2':
        bot.send_message(chat_id, f'Olá! {nome_do_cliente} Analisamos o seu cpf e seu nome informado em nosso sistema financeiro.\n'
                                  f'Não identificamos nenhuma fatura em aberto ou conta vinculada a este cadastro.')
        fim(message)
    elif opcao == '3':
        menu_principal(message)
    else:
        bot.send_message(chat_id, 'Opção Invalida')
        financeiro(message)

def menu_wifi_solucao(message):
    chat_id = message.chat.id
    texto = ('\nO wifi voltou a funcionar?\n'
             '1 - Sim! Problema resolvido.\n'
             '2 - Não. Continuo com problemas.\n'
             '3 - Voltar\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_wifi_solucao)

def processa_wifi_solucao(message):
    chat_id = message.chat.id
    opcao = message.text
    if opcao == '1':
        bot.send_message(chat_id, f'\n Atendimento encerrado com sucesso.\O seu protocolo é {protocolo}')
    elif opcao == '2':
        bot.send_message(chat_id, f'\n Foi aberto um chamado para seu problema.\n'
                                  f'O seu protocolo é {protocolo}, a tratativa varia entre 3 a 5 dias uteis.')
        fim(message)
    elif opcao == '3':
        problemas_para_conectar_ao_wi_fi(message)
    else:
        bot.send_message(chat_id, '\n Opção inválida.')
        menu_wifi_solucao(message)

def problemas_para_conectar_ao_wi_fi(message):
    chat_id = message.chat.id
    texto = ('\n1 - 🔑 Meu aparelho localiza a rede, mas diz Senha Incorreta ou Erro de Autenticação\n'
             '2 - 📡 A rede Wi-Fi da minha casa sumiu da lista e não aparece de jeito nenhum\n'
             '3 - 🌐 Eu consigo conectar no Wi-Fi, mas aparece Conectado, sem internet\n'
             '4 - ⬅️ Voltar\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_problemas_wifi)

def processa_problemas_wifi(message):
    chat_id = message.chat.id
    opcao = message.text
    if opcao == '1':
        bot.send_message(chat_id, 'Muitas vezes o aparelho guarda um histórico de conexão corrompido. Vamos limpar essa rede:\n'
                                  '1 - Vá nas configurações de Wi-Fi do seu celular/computador.\n'
                                  '2 - Clique no nome da sua rede e selecione "Esquecer Rede" ou "Excluir Rede".\n'
                                  '3 - Desligue o Wi-Fi do aparelho, espere 5 segundos e ligue novamente.\n'
                                  '4 - Clique na sua rede e digite a senha novamente.')
        menu_wifi_solucao(message)
    elif opcao == '2':
        bot.send_message(chat_id, 'Se o Wi-Fi sumiu, o emissor do modem pode ter travado ou o aparelho está longe demais.\n'
                                  '1 - Aproxime-se do modem.\n'
                                  '2 - Verifique se a luz do Wi-Fi está acesa.\n'
                                  '3 - Se estiver apagada, pressione o botão Wi-Fi/WLAN por 3 segundos.')
        menu_wifi_solucao(message)
    elif opcao == '3':
        bot.send_message(chat_id, 'Isso significa que seu aparelho conversa com o modem, mas o modem não está recebendo sinal da rua.\n'
                                  '1 - Desconecte o modem da tomada por 30 segundos.\n'
                                  '2 - Aguarde 3 minutos até as luzes estabilizarem.\n'
                                  '3 - Verifique se a luz PON, Internet ou WAN está vermelha.')
        menu_wifi_solucao(message)
    elif opcao == '4':
        suporte_tecnico(message)
    else:
        bot.send_message(chat_id, '\nOpção inválida.')
        problemas_para_conectar_ao_wi_fi(message)

def internet_fora_do_ar_ou_lenta(message):
    chat_id = message.chat.id
    instrucoes = ('\nEntendi! Vamos resolver isso juntos.\n'
                  'Na maioria das vezes, a internet volta a funcionar com alguns passos simples.\n\n'
                  ' PASSO 1 - Reiniciar o Roteador\n'
                  '1. Vá até o modem/roteador.\n'
                  '2. Retire o aparelho da tomada.\n'
                  '3. Aguarde 30 segundos.\n'
                  '4. Ligue novamente e aguarde cerca de 2 minutos.\n\n'
                  ' PASSO 2 - Verificar os Cabos\n'
                  '1. Verifique se todos os cabos estão bem conectados.\n'
                  '2. Confira se nenhum cabo está solto.\n\n'
                  ' PASSO 3 - Testar em Outro Dispositivo\n'
                  '1. Tente acessar a internet por outro celular ou computador.\n'
                  '2. Verifique se o problema acontece em todos os aparelhos.\n\n'
                  'Qual foi o resultado?\n'
                  '1 - ✅ Funcionou! A internet voltou ao normal.\n'
                  '2 - 🐢 Continua lenta.\n'
                  '3 - 🚨 Continua sem sinal.\n'
                  '4 - ⬅️ Voltar.\n')
    msg = bot.send_message(chat_id, instrucoes)
    bot.register_next_step_handler(msg, processa_internet_fora_do_ar)

def processa_internet_fora_do_ar(message):
    chat_id = message.chat.id
    opcao = message.text
    if opcao == '1':
        bot.send_message(chat_id, f'\n Atendimento encerrado com sucesso.\nO seu protocolo é {protocolo}')
    elif opcao == '2':
        bot.send_message(chat_id, f'\n Foi aberto um chamado para seu problema com a lentidão.\n'
                                  f'O seu protocolo é {protocolo}, a tratativa varia entre 3 a 5 dias uteis.')
        fim(message)
    elif opcao == '3':
        bot.send_message(chat_id, f'\n Foi aberto um chamado com urgência pela falta de sinal.\n'
                                  f'O seu protocolo é {protocolo}, a tratativa varia entre 5 a 7 dias uteis.')
        fim(message)
    elif opcao == '4':
        suporte_tecnico(message)
    else:
        bot.send_message(chat_id, '\n Opção inválida.')
        internet_fora_do_ar_ou_lenta(message)

def suporte_tecnico(message):
    chat_id = message.chat.id
    texto = ('1 - 📶 Internet fora do ar ou lenta\n'
             '2 - 📡 Problemas para conectar ao Wi-Fi\n'
             '3 - ⬅️ Voltar\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_suporte_tecnico)

def processa_suporte_tecnico(message):
    opcao = message.text
    if opcao == "1":
        internet_fora_do_ar_ou_lenta(message)
    elif opcao == '2':
        problemas_para_conectar_ao_wi_fi(message)
    elif opcao == '3':
        menu_principal(message)
    else:
        bot.send_message(message.chat.id, '\n Opção inválida.')
        suporte_tecnico(message)

def menu_principal(message):
    chat_id = message.chat.id
    texto = ('\n 🚀 Bem-vindo à Boom Net\n Conectando você ao que importa.\n'
             '1 - 🛠️ Suporte Técnico\n'
             '2 - 💳 Financeiro\n'
             '3 - 🌐 Informações da Rede\n'
             '4 - ❌ Encerrar Atendimento\n')
    msg = bot.send_message(chat_id, texto)
    bot.register_next_step_handler(msg, processa_menu_principal)

def processa_menu_principal(message):
    opcao = message.text
    if opcao == '1':
        bot.send_message(message.chat.id, 'Você acessou o suporte Técnico')
        suporte_tecnico(message)
    elif opcao == '2':
        bot.send_message(message.chat.id, 'Voce acessou ao financeiro')
        financeiro(message)
    elif opcao == '3':
        informacao_da_rede(message)
    elif opcao == '4':
        bot.send_message(message.chat.id, 'Obrigado por utilizar a Boom Net!')
    else:
        bot.send_message(message.chat.id, '\n Opção inválida.')
        menu_principal(message)

# --- COMANDO INICIAL DO BOT NO TELEGRAM (/start) ---
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    estado_usuarios[chat_id] = {'nome': '', 'cpf': ''}
    msg = bot.send_message(chat_id, 'Me informe seu nome:\n')
    bot.register_next_step_handler(msg, obter_nome)

def obter_nome(message):
    chat_id = message.chat.id
    estado_usuarios[chat_id]['nome'] = message.text
    msg = bot.send_message(chat_id, 'Me informe os 3 primeiros digitos do seu cpf\n')
    bot.register_next_step_handler(msg, obter_cpf)

def obter_cpf(message):
    chat_id = message.chat.id
    estado_usuarios[chat_id]['cpf'] = message.text
    bot.send_message(chat_id, f'\nOlá, {estado_usuarios[chat_id]["nome"]}')
    menu_principal(message)

# Mantém o Bot rodando
print("🤖 Bot em execução. Vá no Telegram e digite /start")
bot.infinity_polling()
