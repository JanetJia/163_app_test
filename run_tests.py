import os
import unittest
import yagmail
from Common.HTMLTestRunner import HTMLTestRunner


# 把测试报告作为附件发送到指定邮箱。
def send_mail(report):
    yag = yagmail.SMTP(
        user="wangyiwebtest@163.com",
        password="NEPXGACWQWRERVNZ",
        host='smtp.163.com'
    )
    subject = "网易邮箱大师自动化测试报告"
    contents = "请查看附件。"
    yag.send('957584602@qq.com', subject, contents, report)
    print('email has send out !')


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # print(base_dir)
    test_dir = base_dir + '/TestCase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
    html_report = base_dir + '/TestReport/report.html'
    with open(html_report, 'wb') as fp:
        # 调用HTMLTestRunner，运行测试用例
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title="网易邮箱大师app自动化测试报告",
            description="win10，Pixel API 30,"
        )
        runner.run(suite)
        fp.close()
        # send_mail(html_report)  # 发送测试报告
