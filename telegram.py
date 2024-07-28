import telebot
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.blackbox.ai")

bot = telebot.TeleBot("6391937928:AAEqfMyR-xCRVzWeNvWJlxdt1qU_2D3vaSk")
@bot.message_handler(commands=['start', 'help','hi','hello'])
def starting(message):
    bot.reply_to(message,"Hello Feel free to ask me anything")
    # bot.edit_message_text("1",message.chat.id,greets.message_id)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
    # while True:
            elem = driver.find_element(By.TAG_NAME,"textarea")
            elem.clear()
            elem.send_keys(message.text)
            elem.send_keys(Keys.RETURN)
            waitingMsg = bot.reply_to(message,"Generating Response")
            sleep(10)
            answer = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "prose"))
            )
            bot.edit_message_text(answer[-1].text,message.chat.id,waitingMsg.message_id)
            # bot.reply_to(message,answer[-1].text)
            assert "quit" or "exit" or "q" in message.text
    # driver.close()


bot.infinity_polling()
