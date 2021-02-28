# 163_app_test
网易邮箱大师app(Android)自动化测试
功能测试：
①"通讯录">>>添加联系人
②"写邮件">>>编辑邮件并发送
③"新建待办">>>新建待办事项

测试环境：windows10 + Python3.7.5 + Pycharm2020.1

测试机型：虚拟机Pixel API 30 Android11.0

app版本：6.23.1

建议在Desired_Capabilities添加如下参数避免每次执行测试重复安装 io.appium.uiautomator.server 和 io.appium.uiautomator.server.test
