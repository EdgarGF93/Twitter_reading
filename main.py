from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime


TWITTER_PATH = "https://twitter.com/"
FILE_AUTH = "auth.txt"
BUTTON_COOKIES_XPATH = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]'
BUTTON_GOTOLOGIN_XPATH = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div'
FILL_LOGIN_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
BUTTON_NEXT_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
FILL_PASS_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
BUTTON_LOGIN_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'
BUTTON_INIT_POST = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
FILL_POST_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'
BUTTON_POST_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'
BUTTON_UNDERSTOOD_XPATH = '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div'
BUTTON_PROFILE_XPATH = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div'
BUTTON_LOGOFF_XPATH = '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div/span'
BUTTON_CONFIRM_LOGOFF = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div'


def get_datetime_msg():
    now = datetime.now()
    return str(now)



def retry(max_retries=10, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error occurred: {e}")
                    retries += 1
                    if retries < max_retries:
                        print(f"Retrying in {delay} seconds...")
                        sleep(delay)
            # raise Exception(f"Exceeded maximum retries ({max_retries}).")
        return wrapper
    return decorator


class TwitterDriver():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.read_auth(FILE_AUTH)

    def read_auth(self, address_file_auth=str()):
        with open(address_file_auth, 'r') as f:
            for line in f.readlines():
                if 'USER' in line:
                    self._user = line.split()[-1]
                elif 'PASS' in line:
                    self._pss = line.split()[-1]

    @retry()
    def open_twitter(self):
        self.driver.get(TWITTER_PATH)

    @retry()
    def allow_cookies(self, button_cookies_xpath=str()):
        button_cookies = self.driver.find_element(By.XPATH, button_cookies_xpath)
        button_cookies.click()

    @retry()
    def goto_log_in(self, button_login_xpath=str()):
        button_login = self.driver.find_element(By.XPATH, button_login_xpath)
        button_login.click()

    @retry()
    def input_user(self, fill_user_xpath=str()):
        fill_user = self.driver.find_element(By.XPATH, fill_user_xpath)
        fill_user.send_keys(self._user)

    @retry()
    def next_after_inputuser(self, next_xpath=str()):
        next_button = self.driver.find_element(By.XPATH, next_xpath)
        next_button.click()

    @retry()
    def input_pass(self, fill_pass_xpath=str()):
        fill_pass = self.driver.find_element(By.XPATH, fill_pass_xpath)
        fill_pass.send_keys(self._pss)

    @retry()
    def click_login(self, login_xpath=str()):
        login_button = self.driver.find_element(By.XPATH, login_xpath)
        login_button.click()

    @retry()
    def init_post(self, init_post_xpath=str()):
        init_post_button = self.driver.find_element(By.XPATH, init_post_xpath)
        init_post_button.click()

    @retry()
    def fill_post(self, fill_post_xpath=str(), msg=str()):
        input_post = self.driver.find_element(By.XPATH, fill_post_xpath)
        input_post.send_keys(msg)

    @retry()
    def publish_post(self, post_xath=str()):
        post_button = self.driver.find_element(By.XPATH, post_xath)
        post_button.click()

    @retry()
    def click_understood(self, button_understood_xpath=str()):
        ok_button = self.driver.find_element(By.XPATH, button_understood_xpath)
        ok_button.click()

    @retry()
    def click_profile_bottom(self, button_xpath=str()):
        profile_button = self.driver.find_element(By.XPATH, button_xpath)
        profile_button.click()

    @retry()
    def click_logoff(self, button_xpath=str()):
        logoff_button = self.driver.find_element(By.XPATH, button_xpath)
        logoff_button.click()

    @retry()
    def click_confirm_logoff(self, button_xpath=str()):
        logoff_button = self.driver.find_element(By.XPATH, button_xpath)
        logoff_button.click()

    def log_in_twitter(self):
        self.open_twitter()
        self.allow_cookies(BUTTON_COOKIES_XPATH)
        self.goto_log_in(BUTTON_GOTOLOGIN_XPATH)
        self.input_user(fill_user_xpath=FILL_LOGIN_XPATH)
        self.next_after_inputuser(next_xpath=BUTTON_NEXT_XPATH)
        self.input_pass(fill_pass_xpath=FILL_PASS_XPATH)
        self.click_login(login_xpath=BUTTON_LOGIN_XPATH)

    def post_tweet(self, msg=str()):
        self.init_post(init_post_xpath=BUTTON_INIT_POST)
        self.fill_post(fill_post_xpath=FILL_POST_XPATH, msg=msg)
        self.publish_post(post_xath=BUTTON_POST_XPATH)
        try:
            self.click_understood(button_understood_xpath=BUTTON_UNDERSTOOD_XPATH)
        except:
            pass

    def log_off(self):
        self.click_profile_bottom(button_xpath=BUTTON_PROFILE_XPATH)
        self.click_logoff(button_xpath=BUTTON_LOGOFF_XPATH)
        self.click_confirm_logoff(button_xpath=BUTTON_CONFIRM_LOGOFF)

    @retry()
    def _exit(self):
        self.driver.close()

def run():
    twitter_driver = TwitterDriver()
    twitter_driver.log_in_twitter()
    twitter_driver.post_tweet(msg=get_datetime_msg())
    twitter_driver.log_off()
    twitter_driver._exit()

if __name__ == "__main__":
    run()