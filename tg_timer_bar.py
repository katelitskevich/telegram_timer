import os
import ptbot
from pytimeparse import parse


TG_TOKEN = os.environ["TG_TOKEN"]
TG_CHAT_ID = os.environ["TG_CHAT_ID"]


def reply(chat_id, message):
    parsed_time = parse(message)
    message_id = bot.send_message(chat_id, "Таймер запущен")
    bot.create_countdown(parsed_time, notify_progress, chat_id=chat_id, message_id=message_id, parsed_time=parsed_time)
    bot.create_timer(parsed_time, notify, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, parsed_time):
    bot.update_message(chat_id, message_id,
                     "Осталось секунд: {}\n{}".format(secs_left, render_progressbar(parsed_time, parsed_time-secs_left)))


def notify(chat_id):
    bot.send_message(chat_id, "Время вышло!")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

if __name__ == '__main__' :
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()