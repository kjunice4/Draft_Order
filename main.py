# Draft order randomizer

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import random

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Draft Order Randomizer"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 

""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    GridLayout:
        cols: 1
        
        Label:
            font_size: 75
            size_hint_y: None
            height: 200
            padding: 10, 10
            text: "Menu"
                
        Button:
            font_size: 75
            background_color: 0, 0 , 1, 1
            size_hint_y: None
            height: 200
            text: "Draft Order Randomizer"
            on_release:
                app.root.current = "draft_order"
                root.manager.transition.direction = "left" 

        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 400
            text: "Visit KSquared,LLC"
            on_release:
                import webbrowser
                webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 400
            text: "Other apps from KSquared,LLC"
            on_release:
                import webbrowser
                webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')   
            
            
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 400
            text: "Donate to KSquared,LLC"
            on_release:
                import webbrowser
                webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/about-ksquared')
            
                
            
""")

#Draft Order
Builder.load_string("""
<draft_order>
    id:draft_order
    name:"draft_order"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Draft order randomizer"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        one.text = ""
                        two.text = ""
                        three.text = ""
                        four.text = ""
                        five.text = "" 
                        six.text = ""
                        seven.text = ""
                        eight.text = "" 
                        nine.text = "" 
                        ten.text = "" 
                        eleven.text = "" 
                        twelve.text = "" 
                        thirteen.text = ""
                        fourteen.text = "" 
                        fifteen.text = "" 
                        sixteen.text = "" 
                        seventeen.text = "" 
                        eighteen.text = "" 
                        nineteen.text = "" 
                        twenty.text = ""
                        list_of_steps.clear_widgets()     
                        
                Button:
                    id: steps
                    text: "Randomize"   
                    font_size: 60
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 100
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        draft_order.randomize(one.text + "&" + two.text + "&" + three.text + "&" + four.text + "&" + five.text + "&" + six.text + "&" + seven.text + "&" + eight.text + "&" + nine.text + "&" + ten.text + "&" + eleven.text + "&" + twelve.text + "&" + thirteen.text + "&" + fourteen.text + "&" + fifteen.text + "&" + sixteen.text + "&" + seventeen.text + "&" + eighteen.text + "&" + nineteen.text + "&" + twenty.text)
                          
        
            TextInput:
                id: one
                text: one.text
                hint_text: "1)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: two
                text: two.text
                hint_text: "2)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: three
                text: three.text
                hint_text: "3)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: four
                text: four.text
                hint_text: "4)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: five
                text: five.text
                hint_text: "5)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: six
                text: six.text
                hint_text: "6)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: seven
                text: seven.text
                hint_text: "7)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: eight
                text: eight.text
                hint_text: "8)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: nine
                text: nine.text
                hint_text: "9)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: ten
                text: ten.text
                hint_text: "10)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: eleven
                text: eleven.text
                hint_text: "11)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: twelve
                text: twelve.text
                hint_text: "12)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: thirteen
                text: thirteen.text
                hint_text: "13)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: fourteen
                text: fourteen.text
                hint_text: "14)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: fifteen
                text: fifteen.text
                hint_text: "15)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: sixteen
                text: sixteen.text
                hint_text: "16)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10                 

            TextInput:
                id: seventeen
                text: seventeen.text
                hint_text: "17)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: eighteen
                text: eighteen.text
                hint_text: "18)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10 
                
            TextInput:
                id: nineteen
                text: nineteen.text
                hint_text: "19)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10
                
            TextInput:
                id: twenty
                text: twenty.text
                hint_text: "20)"
                multiline: False
                font_size: 60
                size_hint_y: None
                height: 100
                padding: 10  
                
              
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class draft_order(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(draft_order, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current == "Homepage":
            pass
        elif sm.current == "Menu":
            pass
        elif sm.current == "Algebra_App_List":
            sm.transition.direction = 'right'
            sm.current = "Menu"
        elif sm.current == "Expressions":
            sm.transition.direction = 'right'
            sm.current = "Algebra_App_List"
            
    layouts = []
    def randomize(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print("Trying...")
            print("entry",entry)
                        
            entry_list = entry.split("&")
            print("entry_list",entry_list)
            
            new_list = []
            j = 0
            while j < len(entry_list):
                print(entry_list[j],type(entry_list[j]))
                if entry_list[j] != '':
                    new_list.append(entry_list[j])
                j = j + 1
                
            random.shuffle(new_list)
            print("random_list",new_list)
            
            
            i = 0
            while i < len(new_list):
                
                self.ids.list_of_steps.add_widget(Label(text= str(i+1) + ")" + str(new_list[i])  ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                i = i + 1
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
        
        
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            


sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(draft_order(name="draft_order"))
sm.current = "Homepage"   


class draft_order(App):
    def build(app):
        return sm

if __name__ == '__main__':
    draft_order().run()
