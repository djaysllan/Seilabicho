from telegram.ext import Updater, CommandHandler

# Função para o comando /start
def start(update, context):
    update.message.reply_text('Olá! Eu sou o seu bot.')

def main():
    # Substitua 'SEU_TOKEN' pelo token do seu bot
    updater = Updater(token='6627677020:AAGhZ5Kkv1v1tSVIkxTNBBAgYEAsnIp_eP4')

    # Obtenha o despachante para registrar os manipuladores de comandos
    dp = updater.dispatcher

    # Registre o manipulador para o comando /start
    dp.add_handler(CommandHandler('start', start))

    # Inicie o bot
    updater.start_polling()

    # Mantenha o bot em execução até Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
