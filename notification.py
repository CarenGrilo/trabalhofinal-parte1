from plyer import notification

def notify(nome_do_erro, mensagem_do_erro):
    return notification.notify (
        title=nome_do_erro,
        message=mensagem_do_erro,
        app_name="TrabalhoFinalParte1"
    )