from selenium import webdriver

PATH = "/usr/local/bin/chromedriver"

driver= webdriver.Chrome(PATH)

# driver.get("https://gunargessner.com/")
driver.get("https://www.google.com/")


'''
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwjWt4zSnrD5AhUjxoUKHUJaBlwQ39UDCAQ">
'''