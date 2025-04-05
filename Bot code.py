from telebot import TeleBot, types
import time

TOKEN = '7719143446:AAF6gORTdtn2dWzlD3hYuHwPGnPFRVkZx08'
bot = TeleBot(TOKEN)

user_state = {}

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Готов")
    markup.add(button)

    bot.send_message(message.chat.id, "Добро пожаловать! Если вы готовы ознакомиться с правилами игры, нажмите на кнопку «Готов»", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Готов")
def button_pressed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Начать игру")
    markup.add(button)

    bot.send_message(message.chat.id, "Доброго времени суток, уважаемый пользователь! Ты попал в игру, под названием «The Legend of the Knight». \nПравила игры: Вам будет повествоваться история некого рыцаря, и вы будете делать выбор на протяжении всей игры. Рекомендуем вам поспешно не нажимать на кнопки и обдумывать выбор, ведь от ваших выборов зависит исход игры. Удачи! \nЕсли вы ознакомились с правилами и готовы начать игру, нажмите на кнопку «Начать игру»", reply_markup=markup) 

@bot.message_handler(func=lambda message: message.text == "Начать игру")
def button_pressed(message):
    user_state[message.chat.id] = "start_game" 

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Идти к королю сразу")
    button2 = types.KeyboardButton("Не торопится")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, "Глава 1. Начало...", reply_markup=types.ReplyKeyboardRemove())
    time.sleep(2)
    bot.send_message(message.chat.id, "Сон: В мире, где бескрайние горизонты были залиты кровью нелюдей и прах сгоревших тел витал в воздухе перемешиваясь с сильным смрадом гнили, идёт война рода людского и рода нечисти. \nРод нечисти смог выкрасть артефакт небывалой мощи у людей и военный перевес сил встал на сторону нечисти.")
    time.sleep(13)
    bot.send_message(message.chat.id, "- Вы: Немного приоткрыв глаза видите силуэт человека, облачённого в железные латы возле вашей кровати. Спустя пару секунд вы осознали, что это командир и приняли положение сидя. \n- Командир: Вставай отброс, тебя вызывает король и хочет дать тебе поручение, и не вздумай опаздывать еже ли жизнь дорога. ")
    photo_path = 'D:\Картинки для проекта\глава 1 в начало.png'
    caption = "Командир вас разбудил" 
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=caption)
    time.sleep(12)
    bot.send_message(message.chat.id, "Идти к королю сразу или не торопится?", reply_markup=markup) 

@bot.message_handler(func=lambda message: message.chat.id in user_state)
def handle_choice(message):
    state = user_state[message.chat.id] 

    if state == "start_game":
        if message.text == "Идти к королю сразу":
            user_state[message.chat.id] = "action_1_1_1"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Да")
            button2 = types.KeyboardButton("Нет")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы сразу поняли, что с королём медлить нельзя и ринулись в тронный зал по пути надевая свои латы. Вы входите в тронный зал и видите огромную комнату, наполненную драгоценностями и невероятных размеров королевский трон и величественного короля, сидящего на нём. Вы подходите ближе и встаёте на колено.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\Действие 1.1.png'
            caption = "Король рода людского" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(13) 
            bot.send_message(message.chat.id, "– Король: Приветствую тебя воин, как ты знаешь, конфликт между нашими расами идёт уже много столетий, и чтобы заполучить преимущество, необходимо проникнуть во вражеский замок и вернуть принадлежащий нам по праву артефакт лучезарность! Ты обязан пойти в это путешествие, чтобы защитить своё королевство и отдать честь своему королю! ")
            photo_path = 'D:\Картинки для проекта\Действие 1.2.png' 
            caption = "Артефакт лучезарность"
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption) 
            time.sleep(15) 
            bot.send_message(message.chat.id, "Согласиться с предложением короля?", reply_markup=markup) 
            time.sleep(10)        
        elif message.text == "Не торопится":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы подумали, что дело не может быть настолько срочным, чтобы отвлечь вас от ежедневных утренних процедур.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\Действие 1.1.2.png'
            caption = "Утренние процедуры" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(7)
            bot.send_message(message.chat.id, "После утренних процедур вы пошли на завтрак, и только после этого вы выдвинулись в тронный зал. ")
            time.sleep(5)
            bot.send_message(message.chat.id, "Вы входите в тронный зал и видите огромную комнату, наполненную драгоценностями и невероятных размеров королевский трон и величественного короля, сидящего на нём. Вы подходите ближе и встаёте на колено.")
            photo_path = 'D:\Картинки для проекта\Действие 1.1.png'
            caption = "Король рода людского" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(10)
            bot.send_message(message.chat.id, "- Король: Ты смеешь испытывать мое терпение, жалкий простолюдин. Стража! Снесите ему голову с плеч. \nВас казнили за высокомерие по отношению к королю. ")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            time.sleep(5)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)
            time.sleep(2) 

    elif state == "action_1_1_1":
        if message.text == "Да":
            user_state[message.chat.id] = "action_2_3"
            bot.send_message(message.chat.id, "Вы приняли предложение короля и по его приказу идёте в оружейную, чтобы собраться в путешествие. \nВ оружейной вам предоставили выбор снаряжения и оруженосца.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(7)
            bot.send_message(message.chat.id, "Вы посмотрели на всех оруженосцев и удивились, ведь все кроме самого левого выглядели как спички. Вы выбрали самого левого оруженосца.") 
            photo_path = 'D:\Картинки для проекта\Действие 1.3.2.png'
            caption = "Ваш оруженосец" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(8)
            bot.send_message(message.chat.id, "Далее перед вами оказалась оружейная комната. В оружейной комнате вас уже встречал человек, который выдал вам стартовое снаряжения. Все, вы готовы к путешествию!") 
            photo_path = 'D:\Картинки для проекта\Действие 1.4.png'
            caption = "Вы с оруженосцем" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(8)
            bot.send_message(message.chat.id, "Поздравляю! Вы прошли 1-ую главу игры! \nВыполнено достижений: 1/4") 
            time.sleep(3)
            bot.send_message(message.chat.id, "Глава 2. Путешествие по континенту людей")
            time.sleep(3)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Да")
            button2 = types.KeyboardButton("Нет")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "После того как вы собрали припасы, снаряжение и выбрали оруженосца, вы вышли в путешествие! \n- Оруженосец: Сколько нам идти до замка нечисти? \n- Вы: Идти около двух недель, поэтому припасы тратим рационально. \n- Оруженосец: Хорошо!")
            time.sleep(12)
            bot.send_message(message.chat.id, "Прошел целый день. Неловкая тишина прошла между нашими путешественниками, но вы увидели, как оруженосец начал трястись от страха и начали разговор первым. \n- Вы: Что ты трясёшься, ты же будущий рыцарь, рыцари не должны бояться! \n- Оруженосец: Я боюсь нечести и мне кажется, что я никогда не стану рыцарем, так как мне уже 30 лет и я все ещё хожу в оруженосцах! \n- Вы: Самое главное верь в себя и при виде нечисти не начни трястись, а то опозоришь род людской! Если справимся с заданием, то тогда ты точно станешь рыцарем!")
            photo_path = 'D:\Картинки для проекта\ааа.jpg'
            caption = "Вы с оруженосцем" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(25)
            bot.send_message(message.chat.id, "Наши путники шли всю ночь, и когда наступил день они вышли в поле и смотря в горизонт, оруженосец заметил около 10 силуэтов. Пройдя несколько минут силуэты становились все ближе и ближе. Как только силуэты приблизились, вы разглядели в них известных бандитов, которые грабят абсолютно всех и не оставляют никого в живых!")
            photo_path = 'D:\Картинки для проекта\ййй.jpg'
            caption = "Бандиты" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(13)
            bot.send_message(message.chat.id, "Убежать от бандитов?", reply_markup=markup)
        elif message.text == "Нет": 
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "- Король: Ты отказываешь королю? Стража! Снесите ему голову с плеч. \nВас казнили за высокомерие по отношению к королю. ")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            time.sleep(5)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)

    elif state == "game_over":
        if message.text == "Начать заново":
            user_state[message.chat.id] = "start_game"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button = types.KeyboardButton("Начать игру")
            markup.add(button)
            bot.send_message(message.chat.id, "Вы начали новую игру! Нажмите на кнопку «Начать игру» для старта.", reply_markup=markup)
        if message.text == "Завершить игру":
            bot.send_message(message.chat.id, "Игра завершена", reply_markup=types.ReplyKeyboardRemove())
    
    elif state == "action_2_3":
        user_state[message.chat.id] = "action_2_5"
        if message.text == "Да":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Налево")
            button2 = types.KeyboardButton("Направо")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Не будем отвлекаться на этот сброд, просто убегай! \nЧерез некоторое время наши герои с легкостью оторвались от бандитов и продолжили свое путешествие.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\ццц.png'
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            time.sleep(9)
            bot.send_message(message.chat.id, "- Оруженосец: Фууух! Еле оторвались от них… \n- Вы: Да. Ну что, сделаем привал? А то мы уже 3 дня без остановки идём! \nНаши герои развели костер и собрали палатки. \n- Вы: А ведь знаешь, оруженосец, я тоже боялся во время своего первого путешествия, но мой наставник, с которым я путешествовал огромное количество времени поведал мне тайну, как перестать трусить. - Оруженосец: Спасибо за наставления. Я не подведу вас и стану рыцарем! Так что вам помогло перестать боятся? \n- Вы: Так это же очевидно! Алкоголь!!! \n- Оруженосец: Вы уверенны, что это тот совет, который мне сейчас нужен? Я много слышал о вреде алкоголя внутри стен замка. \n- Вы: Не неси чушь, пару кружек для храбрости ещё никому не помешали! Завтра утром пойдем в таверну, чтобы ты перестал бояться! Тут как раз близко есть таверна. \nНочь прошла. Наши путешественники выдвинулись в сторону таверны. \n- Вы: Ну что, оруженосец, ты готов? \n- Оруженосец: Да, я готов. Надеюсь мне поможет этот совет, и я перестану бояться в бою.")        
            time.sleep(43)
            photo_path = 'D:\Картинки для проекта\цц.jpg'
            caption = "Привал в лесу" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(5)
            bot.send_message(message.chat.id, "- Прошло несколько часов, и вы с оруженосцем уже добрались до таверны. Зайдя во внутрь, вы сразу увидели огромное количество людей, которые выпивали за барной стойкой и столами. Вы с оруженосцем сели за свободный стол и заказали по бочонку пива.\nСпустя несколько минут вам принесли заказ.  Вы сразу же сделали глоток и почувствовали силу в руках. Оруженосец долго смотрел на бочонок, не притронувшись вовсе… \n- Вы: Если ты хочешь перебороть страх быстро взял и выпил залпом! \nОруженосец всё-таки решился. Он схватил бочонок руками и двумя глотками выпил всё. \nНесмотря на то, что это был его первый бочонок в жизни, он сразу же заказал еще 2! Прошло несколько часов. Оруженосец уже выпил около 10 литров пива. \n- Вы: Все, на первый раз достаточно. Собирайся, мы уходим от сюда. \nВы с оруженосцем начали собираться. Когда вы встали из-за стола оруженосцу стало плохо. Явно он перепил. Пройдя ещё несколько метров, он упал… Из его рта пошла пена, а из его глаз потекла кровь. Пиво было отравлено! Надо быть осторожнее. К сожалению оруженосец умер.")        
            time.sleep(45)
            photo_path = 'D:\Картинки для проекта\ц.jpg'
            caption = "Мертвый оруженосец..." 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(5)
            bot.send_message(message.chat.id, "Теперь путь вы продолжаете один! Вы выдвинулись в сторону леса. Зайдя в лес, вы шли несколько часов по тропинке. Вы подошли к развилке.")
            photo_path = 'D:\Картинки для проекта\развилка.jpg'
            caption = "Развилка в лесу" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(6)
            bot.send_message(message.chat.id, "Куда вы пойдете? Налево или направо?", reply_markup=markup)
        elif message.text == "Нет":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Налево")
            button2 = types.KeyboardButton("Направо")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "- Вы: Примем бой с честью! Оруженосец, приготовься к бою и будь на чеку. Прикрывай мою спину, и самое главное не умирай! \nБуквально в мгновение вы перебили почти всех бандитов, осталось всего трое. Вы побежали в атаку и своим мечом отрубили голову одному из оставшихся бандитов и ранили второго, но последний бандит, пока вы убивали остальных, решил забрать жизнь оруженосца и проткнул его грудь кинжалом. Вы моментально убили бандита, который отправил на тот свет вашего оруженосца. Вы потеряли половину снаряжение и продолжаете путь один...", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\й.jpg'
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            time.sleep(25)
            bot.send_message(message.chat.id, "Вы вышли с поля боя и идёте в сторону леса. Зайдя в лес, и пройдя несколько часов по тропинке, вы увидели развилку. Одна дорога ведёт направо, а другая налево.") 
            photo_path = 'D:\Картинки для проекта\развилка.jpg'
            caption = "Развилка в лесу" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(8)
            bot.send_message(message.chat.id, "Куда вы пойдете? Налево или направо?", reply_markup=markup)
            time.sleep(2)

    elif state == "action_2_5":
        if message.text == "Налево":
            user_state[message.chat.id] = "action_2_5_2"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Убежать")
            button2 = types.KeyboardButton("Зелезть на дерево")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы решили пойти налево. Пройдя несколько минут, вы видите, как за вами несётся огромный медведь.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\медведь.jpg'
            caption = "Медведь бежит за вами" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            bot.send_message(message.chat.id, "Убежать от медведя или залезть на дерево?", reply_markup=markup)
        elif message.text == "Направо":
            user_state[message.chat.id] = "action_2_5_4"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Заплатить")
            button2 = types.KeyboardButton("Не платить")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы вышли к берегу континента людей и встретили паромщика, который предложил перевести вас на континент нечисти за 5 золотых.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(7)
            bot.send_message(message.chat.id, "Будете ли вы платить паромщику за переправу на другой берег на лодке или вы проплывёте реку?", reply_markup=markup)
        
    elif state == "action_2_5_2":
        if message.text == "Убежать":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вас съел медведь.")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)
        elif message.text == "Зелезть на дерево":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вас съел медведь.")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)

    elif state == "action_2_5_4":
        if message.text == "Заплатить":
            user_state[message.chat.id] = "action_3"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Кинжалом")
            button2 = types.KeyboardButton("Мечом")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Ваc перевез паромщик на другой берег, и вы вступили на вражескую территорию...", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\фф.jpg'
            caption = "Паромщик" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(5)
            bot.send_message(message.chat.id, "Поздравляю! Вы прошли 2-ую главу игры! \nВыполнено достижений: 2/4")
            time.sleep(3)
            bot.send_message(message.chat.id, "Глава 3. Путешествие по континенту нечести")
            time.sleep(3)
            bot.send_message(message.chat.id, "Переправившись на другой берег с паромщиком, вы оказались на вражеской территории. Пройдя несколько километров от берега, вас заметили вражеские войны и побежали на прямую к вам… Сейчас начнётся битва. Увидев трёх упырей, вы срази начали доставать оружие, но вопрос в том, какое именно оружие вы возьмете?")
            photo_path = 'D:\Картинки для проекта\ее.jpg'
            caption = "Вражеские упыри" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(15)
            bot.send_message(message.chat.id, "Чем вы будете отбиваться от упырей?", reply_markup=markup)

        elif message.text == "Не платить":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы решили не платить паромщику и отправились вплавь. Из-за снаряжения ваш вес оказался слишком большим, и вы пошли ко дну.")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)

    elif state == "action_3":
        if message.text == "Кинжалом":
            user_state[message.chat.id] = "action_3_2"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Да")
            button2 = types.KeyboardButton("Нет")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы быстро расправились с тремя упырями, получив незначительное ранение.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(4)
            bot.send_message(message.chat.id, "Убив трёх упырей, вы продолжили свой путь на вражеской территории. Ваш путь длится уже несколько дней. Вы идёте по лесу, в сторону замка нечисти. Идя по тропинке, в дали вы заметили силуэт и удивившись, направились прямо в его сторону. Подойдя к нему, поняли, что это тоже человек. Вы подошли к нему и начали разговор первым. \n- Вы: Приветствую тебя. Что ты здесь делаешь? \n- Незнакомец: Приветствую тебя, воин. По поручению короля я должен украсть артефакт и вернуть его нашему королю! Идём со мной, так как я знаю короткий путь до замка. \nУдивившись, вы решили расспросить его, ведь король не говорил, что кто-то кроме него будет выполнять это задание.\n - Вы: А можешь сказать, как зовут нашего короля? \n- Незнакомец: Что за опрос ты устроил? Ты меня в чём-то подозреваешь? \n- Вы: Просто ответь на вопрос. \n- Незнакомец: На последнем задании я сильно ударился головой, и поэтому у меня небольшие провалы в памяти. Я затрудняюсь ответить… \n- Вы: Услышал, родной. \n- Незнакомец: Давай поговорим завтра, ведь уже темнеет. Продолжим путь завтра, а сейчас спать! \nВы сильно усомнились в незнакомце. И перед вами встал выбор.")
            time.sleep(46)
            photo_path = 'D:\Картинки для проекта\нез.jpg'
            caption = "Вы с незнакомцем" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(3)
            bot.send_message(message.chat.id, "Довериться ему?", reply_markup=markup)        
        elif message.text == "Мечом":
            user_state[message.chat.id] = "action_3_2"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Да")
            button2 = types.KeyboardButton("Нет")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы с лёгкостью убили трёх упырей, не получив ранений.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(5)
            bot.send_message(message.chat.id, "Убив трёх упырей, вы продолжили свой путь на вражеской территории. Ваш путь длится уже несколько дней. Вы идёте по лесу, в сторону замка нечисти. Идя по тропинке, в дали вы заметили силуэт и удивившись, направились прямо в его сторону. Подойдя к нему, поняли, что это тоже человек. Вы подошли к нему и начали разговор первым. \n- Вы: Приветствую тебя. Что ты здесь делаешь? \n- Незнакомец: Приветствую тебя, воин. По поручению короля я должен украсть артефакт и вернуть его нашему королю! Идём со мной, так как я знаю короткий путь до замка. \nУдивившись, вы решили расспросить его, ведь король не говорил, что кто-то кроме него будет выполнять это задание.\n - Вы: А можешь сказать, как зовут нашего короля? \n- Незнакомец: Что за опрос ты устроил? Ты меня в чём-то подозреваешь? \n- Вы: Просто ответь на вопрос. \n- Незнакомец: На последнем задании я сильно ударился головой, и поэтому у меня небольшие провалы в памяти. Я затрудняюсь ответить… \n- Вы: Услышал, родной. \n- Незнакомец: Давай поговорим завтра, ведь уже темнеет. Продолжим путь завтра, а сейчас спать! \nВы сильно усомнились в незнакомце. И перед вами встал выбор.")
            time.sleep(46)
            photo_path = 'D:\Картинки для проекта\нез.jpg'
            caption = "Вы с незнакомцем" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(3)
            bot.send_message(message.chat.id, "Довериться ему?", reply_markup=markup) 
    
    elif state == "action_3_2":
        if message.text == "Да":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы решили, что его история правдоподобна и доверились ему.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(3)
            bot.send_message(message.chat.id, "Когда вы прилегли отдохнуть незнакомец превратился в свой настоящий облик и убил вас, пока вы отдыхали. Оказывается, он был доппельгангер.\nДоппельгангер – это существо, копирующее людей, которых он убил.")
            photo_path = 'D:\Картинки для проекта\Дефолт смерть.png' 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
            time.sleep(10)
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)
        elif message.text == "Нет":
            user_state[message.chat.id] = "action_4"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Пойти в лобовую")
            button2 = types.KeyboardButton("Кинуть камешек в кусты")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы решили не доверять незнакомцу и подгадать момент для нападения. Когда незнакомец лёг, вы тихо подобрались к нему и перерезали ему глотку. После смерти незнакомца его тело превратилось в жуткое чудище. Это оказался доппельгангер. \nДоппельгангер – это существо, копирующее людей, которых он убил. \nНа следующие утро вы пошли в сторону замка. Пройдя весь день сквозь тёмную чащу леса, вы подошли к подножию замка нечисти.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\ппп.jpg'
            caption = "Доппельгангер" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(15)
            bot.send_message(message.chat.id, "Поздравляю! Вы прошли 3-ю главу игры! \nВыполнено достижений: 3/4")
            time.sleep(4)
            bot.send_message(message.chat.id, "Глава 4. Конец истории...") 
            time.sleep(3)
            bot.send_message(message.chat.id, "Подойдя поближе к подножью замка, вы видите у входа два огромных и сильных стражника, каждый из них был ростом под 3 метра. Оба стражника выглядели угрожающе. Прикинув шансы, вы начали думать что делать дальше…")
            photo_path = 'D:\Картинки для проекта\ннн.png'
            caption = "Охранники замка" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(15)
            bot.send_message(message.chat.id, "Что вы сделаете, пойдёте сражаться с ними в лобовую как храбрый воин или решите отвлечь охранников и втихую пробраться в замок?", reply_markup=markup) 
    
    elif state == "action_4":
        if message.text == "Пойти в лобовую":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Когда вы резко выбежали на охранников они не придали этому значения, но, когда вы подбежали слишком близко один из охранников, резко схватил вас за руку. В этот момент другой охранник хватает вас за ноги, и они дружно рвут вас пополам и используют ваши кости как зубочистки.", reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)
        elif message.text == "Кинуть камешек в кусты": 
            user_state[message.chat.id] = "action_4_4"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Да")
            button2 = types.KeyboardButton("Нет")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Вы решили кинуть камень в кусты и отвлечь их внимание. К счастью оба охранника отвлеклись на примитивную приманку, и вы быстро прошмыгнули в замок, минуя препятствия.", reply_markup=types.ReplyKeyboardRemove())
            photo_path = 'D:\Картинки для проекта\яяя.png'
            caption = "Вы заходите в замок" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(9)
            bot.send_message(message.chat.id, "По наводкам короля вы спустились в подземелье, чудом проходя все опасности. Пройдя пару коридоров, вы увидели дверь в комнату с трофеями. Дверь была заперта, но вспомнив что у нечисти слабый интеллект вы решили проверить под ковриком. Удивительно, нечисти и правда слабы умом, подумали вы, заходя в трофейную комнату.")
            photo_path = 'D:\Картинки для проекта\ыыы.png'
            caption = "Вы заходите в трофейню комнату" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(15)
            bot.send_message(message.chat.id, "Зайдя в трофейную комнату вас ослепило количество блестящего золота, лежащего по всей комнате, гигантская гора золота и сокровищ будто бы манила вас, а рядом с ней на пьедестале лежал сияющий артефакт, который вам и нужно было забрать.")
            time.sleep(15)
            bot.send_message(message.chat.id, "Вы взяли артефакт, но на полу лежит ещё куча драгоценностей. Возьмете их с собой?", reply_markup=markup)

    elif state == "action_4_4":
        if message.text == "Да":
            user_state[message.chat.id] = "game_over" 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Начать заново")
            button2 = types.KeyboardButton("Завершить игру")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "При пробеге из замка вы уронили пару драгоценностей и вас услышали охранники. Вас догнали и убили.... Жадность фраера сгубила", reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, "Вы погибли. Хотите начать игру заново?", reply_markup=markup)
        elif message.text == "Нет":
            user_state[message.chat.id] = "action_4_7"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
            button1 = types.KeyboardButton("Подслушать")
            button2 = types.KeyboardButton("Зайти")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, "Взяв только артефакт вы быстро и незаметно улизнули из замка. На выходе вы провернули тот же трюк с охранниками и убежали от замка подальше.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(6)
            bot.send_message(message.chat.id, "Вы решили незамедлительно покинуть континент нечисти. На своём пути обратно вас встретило много неприятностей, такие как драконы, нечисть, преследователи из замка, но вы ловко улизнули от всех. И вот попав на континент людей вы отправились к замку, чтобы принести королю артефакт. Дойдя до подножия замка, вы зашли в него и подошли к двери в тронный зал, вы услышали голоса за дверью.")
            time.sleep(20)
            bot.send_message(message.chat.id, "Вы задумались, стоит ли подслушать что там говорят или же стоит незамедлительно зайти?", reply_markup=markup)

    elif state == "action_4_7":
        if message.text == "Подслушать":
            bot.send_message(message.chat.id, "Вы прислонились ухом к двери и услышали, как король хочет посадить вас в темницу за столь долгое ожидание.", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(6)
            bot.send_message(message.chat.id, "Вы решили предать короля и ушли из замка. Вы продали артефакт в ломбарде. Выкупили дом в лесу и огромное количество алкоголя до конца жизни. Теперь вам никто не указ.")
            time.sleep(9)
            photo_path = 'D:\Картинки для проекта\конец.png'
            caption = "Вы в своем новом доме"
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(3)
            bot.send_message(message.chat.id, "Поздравляю! Вы прошли игру! \nВыполнено достижений: 4/4")
        elif message.text == "Зайти":
            bot.send_message(message.chat.id, "Вы широко распахиваете дверь тронного зала и громко говорите, что вернулись к своему королю с долгожданным артефактом. Король с нахмуренным лицом говорит страже немедленно схватить вас за руки и в таком положении король начал отчитывать вас. \n-Король: Как ты смел испытывать моё терпение и возвращаться так долго, в темницу его!", reply_markup=types.ReplyKeyboardRemove())
            time.sleep(10)
            bot.send_message(message.chat.id, "Вас кинули в темницу по приказу короля до конца ваших дней.")
            photo_path = 'D:\Картинки для проекта\темница.png'
            caption = "Вы в темнице" 
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=caption)
            time.sleep(4)
            bot.send_message(message.chat.id, "Поздравляю! Вы прошли игру! \nВыполнено достижений: 4/4") 

bot.polling()  
