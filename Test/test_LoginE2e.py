import pytest as pytest
from Test.InitPagesWithDriver import init


class TestLoginE2e:
    def setup_class(self):
        self.initial = init.pageWithDriver()

    def test_LoginE2e(self):
        self.initial.goTo.bp.moveToSite("https://www.saucedemo.com")
        uNames = self.initial.goTo.lp.getAllUserNames()
        password = self.initial.goTo.lp.getPassword()
        self.initial.goTo.lp.insertDifferentValidCredentials(unames=uNames, password=password)
        self.initial.goTo.lp.clickLoginBtnWithoutCredentials()
        self.initial.goTo.lp.insertOnlyUsername(username="123")
        self.initial.goTo.lp.insertOnlyPassword(password="123")
        self.initial.goTo.lp.insertWrongCredentials(username="123", password="123")
        self.initial.goTo.seleniumInfra.close()



if __name__ == '__main__':
    import sys, inspect, os

    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    class_name = getattr(sys.modules[__name__], clsmembers[0][0])
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    method_list = [func for func in dir(class_name) if
                   callable(getattr(class_name, func)) and not func.startswith("__") and func.startswith("test")]
    function_dict = {}
    function_dict["0"] = "run all tests"
    for i in range(1, len(method_list) + 1):
        function_dict[str(i)] = method_list[i - 1]
    print(function_dict)
    txt = input("please choose test you want to run or debug and then press enter")
    command = "-v " + module_name + ".py::" + clsmembers[0][0] + "::" + function_dict[txt] + ""
    if txt != "0":
        pytest.main(command.split(" "))
    else:
        pytest.main(["-v", module_name + ".py"])