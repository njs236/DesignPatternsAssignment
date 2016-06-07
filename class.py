import cmdmodule

class Console(cmdmodule.Cmd):
    def __init__(self, view):
        """

        :return: None
        """
        cmdmodule.Cmd.__init__(self)
        self.myView = view
        self.prompt = "=>> "
        self.intro = "Welcome to console!"  # defaults to None

    def do_exit(self, line):
        """
        to Exit from the console
        :param line: a message
        :return: to Exit from console
        """
        return -1

    def do_q(self, line):
        """
        To exit from the console
        :param line: a message
        :return: to call Exit method
        """
        return self.do_exit(line)

    def do_help(self, args):
        """
        Get help on commands
           'help' or '?' with no arguments prints a list of
           commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        :param args: a message
        :return: None
        """
        # The only reason to define this method is for the help
        # text in the doc string
        cmdmodule.Cmd.do_help(self, args)

    def do_age(self, args):
        """
        Present Age Data as bar chart
        :param args: message
        :return: None
        """
        self.myView.getController().displayAgeGraph()

    def do_bmi(self, args):
        """
        Present BMI information as pie chart
        :param args: message
        :return: None
        """
        self.myView.getController().displayBMIGraph()

    def do_gender(self, args):
        """
        Present Gender information as pie chart
        :param args: message
        :return: None
        """
        self.myView.getController().displayGenderGraph()

    def do_sales(self, args):
        """
        Present Sales information as bar chart
        :param args: message
        :return: None
        """
        self.myView.getController().displaySalesGraph()

    def do_income(self, args):
        """
        Present Income information as bar chart
        :param args: message
        :return: None
        """
        self.myView.getController().displayIncomeGraph()

    def do_bmisales(self, args):
        """
        Present a scatter graph of BMI and Sales data
        :param args: message
        :return: None
        """
        self.myView.getController().displayBMISalesGraph()

    def do_loadfile(self, args):
        """
        Load File and check contents
        :param args:
        :return:
        """
        try:
            self.myView.getController().check(args[0])
        except IndexError:
            self.myView.getController().check()