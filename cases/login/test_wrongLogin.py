import pytest

from cases.lib.webui import loginAndCheck
#
# class Test_wrongLogin:
#     def test_UI_0001(self):
#         print("\n用例 UI——0001")
#         alertText=loginAndCheck(None,'88888888')
#
#         assert alertText=='请输入用户名'
#     def test_UI_0002(self):
#         print("\n用例 UI——0002")
#         alertText=loginAndCheck('byh',None)
#         assert alertText=='请输入密码'
#
#     def test_UI_0003(self):
#         print("\n用例 UI——0003")
#         alertText=loginAndCheck('byh',88888888)
#         assert alertText=='登录失败 : 用户名或者密码错误'
class Test_错误登录:
    # 数据驱动测试
    @pytest.mark.parametrize('username, password, expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
    ]
                             )
    def test_UI_0001_0005(self, username, password, expectedalert):
        alertText = loginAndCheck(username, password)
        assert alertText == expectedalert
