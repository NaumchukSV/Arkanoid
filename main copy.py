import pygame
pygame.init()

back = (200,255,255)#колір фону (background)
mw = pygame.display.set_mode((500,500))#Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

#змінні, що відповідають за координати платформи
racket_x =200
racket_y =330

#нове


#прапор закінчення гри
game_over = False
#клас із попереднього проекту
class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


#клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width =10, height =10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,(width,height))
 
    def draw(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))


#створення м'яча та платформи
ball = Picture('ball.png',160,200,50,50)
platform = Picture('platform.png', racket_x, racket_y,100,30)

#Створення ворогів
enemy_width = 40
enemy_height = 40
start_x =30 #координати створення першого монстра
start_y =10
count =9 #кількість монстрів у верхньому ряду
monsters = []#список для зберігання об'єктів-монстрів
for j in range(3):#цикл по стовпцях
    y = start_y + (45* j)#координата монстра у кожному слід. стовпці буде зміщена на 55 пікселів по y
    x = start_x  + (17.5* j)
    for i in range(count):#цикл по рядах(рядків) створює в рядку кількість монстрів,що дорівнює count
        d = Picture ('enemy.png', x, y,enemy_width,enemy_height)#створюємо монстра
        monsters.append(d)#додаємо до списку
        x = x + (enemy_width+10) #збільшуємо координату наступного монстра
    count = count -1 #для наступного ряду зменшуємо кількість монстрів

while not game_over:
    ball.fill()
    platform.fill()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over =True


    
       
    #малюємо всіх монстрів зі списку
    for m in monsters:
        m.draw()

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)


