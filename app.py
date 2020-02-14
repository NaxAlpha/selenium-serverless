from flask import *
from uuid import uuid4
from selenium import webdriver


app = Flask(__name__)


def _create_driver(w, h):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('window-size={}x{}'.format(w, h))
    chrome_options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome('chromedriver', options=chrome_options)


@app.route('/')
def home():
    return redirect('/render?w=1280&h=720&url=https://google.com/')


@app.route('/render')
def scrape():
    w = int(request.params.get('w', 1280))
    h = int(request.params.get('w', 720))
    url = request.params.get('url', 'https://google.com')
    wd = _create_driver(w, h)
    wd.get(url)
    fn = str(uuid4()) + '.jpg'
    wd.save_screenshot(fn)
    return send_file(fn)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
