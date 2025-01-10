from DrissionPage import ChromiumPage
import time

def countdown(n):
    for i in range(n, 0, -1):
        time.sleep(1)  # 让程序等待1秒

def sign_in():
    sign_in_page = ChromiumPage()
    sign_in_page.get('https://www.xiaohongshu.com')
    # 第一次运行需要扫码登录
    print("请扫码登录")
    # 倒计时30s
    countdown(20)

def open(url):
    global page, user_name
    page = ChromiumPage()
    page.get(f'{url}')
    # 页面最大化
    page.set.window.max()

if __name__ == '__main__':
    # 1、第1次运行需要登录，需要执行sign_in()步骤。第2次之后不用登录，可以注释掉sign_in()步骤。
    sign_in()

    # 2、设置主页地址url
    author_url = "https://www.xiaohongshu.com/search_result?keyword=%25E9%25BA%25A6%25E5%25BD%2593%25E5%258A%25B3&source=unknown"

    # 打开主页
    open(author_url)
