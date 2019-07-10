from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class AppGrid(GridLayout):
    def __init__(self, **kwargs):
        super(AppGrid, self).__init__(**kwargs)
        #Create Text Box
        self.cols = 2
        self.add_widget(Label(text="Binary: ", font_size=40))
        #Create Input Box 1  #Multiline=False Because we want only one line of INPUT
        self.firstNumber = TextInput(multiline=False)
        self.add_widget(self.firstNumber)
        self.add_widget(Label(text="Decimal: ", font_size=40))
        self.firstNumber.font_size ='150dp'
        # Create Box 2 #Multiline=False Because we want only one line of INPUT
        self.secondNumber = TextInput(multiline=False)
        self.add_widget(self.secondNumber)
        self.secondNumber.font_size = '150dp'
        #Create Button and Set Font Size
        self.submit = Button(text='Trans', font_size=40)
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.pressed)
    def pressed(self, instance):
        firstNum = self.firstNumber.text
        secNum = self.secondNumber.text
        a = 0
        b = 0
        c = 0
        d = 0
        length = len(firstNum)
        if length == 4 and (firstNum[0] == '1' or firstNum[0] == '0')and (firstNum[1] == '1' or firstNum[1] == '0')\
            and (firstNum[2] == '1' or firstNum[2] == '0')and (firstNum[3] == '1' or firstNum[3] == '0'):
            for i in range(4):
                print('i right now = ' + str(i))
                if firstNum[i] == '1':
                    a = 8
                    print(a)
                if firstNum[i+1] == '1':
                    b = 4
                    print(b)
                if firstNum[i+2] == '1':
                    c = 2
                    print(c)
                if firstNum[i+3] == '1':
                    d = 1
                    print(d)
                break
            deci = (a + b + c + d)
            print(deci)
            self.secondNumber.text = str(deci)
        elif length != 4 or (firstNum[0] != '0' or firstNum[0] != '1') or (firstNum[1] != '0' or firstNum[1] != '1') \
             or (firstNum[2] != '0' or firstNum[2] != '1') or (firstNum[3] != '0' or firstNum[3] != '1'):
            self.firstNumber.text=''
            self.firstNumber.text= 'Error'






class TestApp(App):
      def build(self):
            return AppGrid()
            #while (answer1)>=0:
             #   breakTestApp().run()

TestApp().run()
