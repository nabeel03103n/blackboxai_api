import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.blackbox.ai")

while True:
    if prompt := st.chat_input("Message CodeSolveAI"):
        with st.chat_message("user"):
                st.markdown(prompt)

        with st.chat_message("assistant"):
                elem = driver.find_element(By.TAG_NAME,"textarea")
                elem.clear()
                elem.send_keys(prompt)
                elem.send_keys(Keys.RETURN)
                waitingMsg = st.markdown("Generating Response...")
                sleep(10)
                answer = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "prose"))
                )
                # bot.reply_to(message,answer[-1].text)
                st.write(answer[-1].text)
                assert "quit" or "exit" or "q" in prompt