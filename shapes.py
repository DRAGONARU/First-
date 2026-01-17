class Shape():
    def __init__(self, cord_x, cord_y, colour):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.colour = colour
    
    def draw(self):
        return f"Рисую {self.colour} фигуру по координатам {self.cord_x}, {self.cord_y}"

class Circle(Shape):
    def __init__(self, cord_x, cord_y, colour, radius):
        super().__init__(self, cord_x, cord_y, colour)
        self.radius = radius
    
    def draw(self):
        return f"Рисую {self.colour} круг по координатам {self.cord_x}, {self.cord_y} с радиусом {self.radius}"

class Rectangle(Shape):
    def __init__(self, cord_x, cord_y, colour, x_length, y_length):
        super().__init__(self, cord_x, cord_y, colour)
        self.x_length = x_length
        self.y_length = y_length

    def draw(self):
        return f"Рисую {self.colour} прямоугольник по координатам {self.cord_x}, {self.cord_y} с длинной {self.x_length} и высотой {self.y_length}"

class Line(Shape):
    def __init__(self, cord_x, cord_y, colour, length, rotation_degree):
        super().__init__(self, cord_x, cord_y, colour)
        self.rotation_degree = rotation_degree
        self.length = length

    def draw(self):
        return f"Рисую {self.colour} линию по координатам {self.cord_x}, {self.cord_y} с длинной {self.length} повёрнутой на {self.rotation_degree} градусов"

class EditorHistory():
    undo_stack = []
    rendo_stack = []

class EditorCommand():
    pass

class Canvas():
    def __init__(self, objects_list, render_type, editor_history):
        self._objects_list = objects_list
        self.render_type = render_type
        self.editor_history = editor_history
    
    def render_shapes(self):
        print(f"Применяю метод рендера {self.render_type}")
        for item in self._objects_list:
            print(item.draw())
    
    def AddShape(self, shape):
        self.editor_history.undo_stack.append(['add'])
        self._objects_list.append(shape)

    def RemoveShape(self, number):
        _ = self._objects_list[number]
        self.editor_history.undo_stack.append(['remove', x])
        self._objects_list.pop(number)

    def MoveShape(self, number, plus_x, plus_y):
        self.editor_history.undo_stack.append(['move', number, plus_x, plus_y])
        self._objects_list[number].cord_x += plus_x
        self._objects_list[number].cord_y += plus_y
    
    def ChangeColor(self, number, colour):
        self.editor_history.undo_stack.append(['colour', number, colour])
        self._objects_list[number].colour = colour
    
    def undo(self):
        if len(self.editor_history.undo_stack) == 0:
            print("Can't undo")
        else:
            if self.editor_history.undo_stack[-1][0] == 'add':
                self._objects_list.pop(-1)
                self.editor_history.undo_stack.pop()
            elif self.editor_history.undo_stack[-1][0] == 'remove':
                self._objects_list.append(self.editor_history.undo_stack[-1][1])
                self.editor_history.undo_stack.pop()
            elif self.editor_history.undo_stack[-1][0] == 'move':
                tmp_num = self.editor_history.undo_stack[-1][1]
                tmp_x = self.editor_history.undo_stack[-1][2]
                tmp_y = self.editor_history.undo_stack[-1][3]
                self._objects_list[tmp_num].cord_x -= tmp_x
                self._objects_list[tmp_num].cord_y -= tmp_y
                self.editor_history.undo_stack.pop()
            else:
                tmp_num = self.editor_history.undo_stack[-1][1]
                tmp_c = self.editor_history.undo_stack[-1][2]
                self._objects_list[tmp_num].colour = tmp_c
                self.editor_history.undo_stack.pop()

if __name__ == '__main__':
    print('Вас приветствует графический редактор: "Как поняли, так и сделали"TM')
    print('''Наши возможные комманды:
             AddShape
             RemoveShape
             MoveShape
             ChangeColor
          ''')
    our_h = EditorHistory()
    our_c = Canvas([], "Растр", our_h)
    
    while True:
        print("Напишите комманду")
        command = input()
        if command == "AddShape":
            print("Напиши что за фигура (Круг, Прямоугольник, Линия)")
            command = input()
            if command == "Круг":
                print("Напиши x y цвет радиус")
                command = input()
                our_c.AddShape(a = Circle()) #Ну вы поняли, я надеюсь