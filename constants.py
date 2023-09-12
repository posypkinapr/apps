from PyQt5.QtCore import QTime
greetings = 'Добро пожаловать в программу по определению состояния здоровья!'
description = '''Тест Руфье является простым и быстрым способом
оценки физической выносливости и сердечно-сосудистой системы.

Результаты теста могут быть использованы для
оценки общего уровня физической формы человека.'''

start_text = 'Начать'
title = 'Здоровье'

window_1_size = (300, 300)

time_1 = QTime(0, 0, 15)
txt_timer_1 = time_1.toString("hh:mm:ss")

time_2 = QTime(0, 0, 45)
txt_timer_2 = time_2.toString("hh:mm:ss")

description_1 = 'Вам нужно лечь на спину и измерить пульс в течение 15 секунд'
timer_1 = 'Таймер:'
button_1 = 'Старт!'
next_button1 = 'Далее'
title_1 = 'Тест 1'
d_title_1 = 'Описание теста 1'

d_title_2 = 'Описание теста 2'
description_2 = 'Выполните 30 приседаний за 45 секунд'
title_2 = 'Тест 2'

description_3 = 'Лягте на спину, и в течение минуты измерьте пульс в первые 15 секунд, и в последние 15.'
d_title_3 = 'Описание теста 3'
title_3 = 'Тест 3'

description_r = 'Ваш результат:'
title_r = 'Результаты'
end_button = 'Завершить'