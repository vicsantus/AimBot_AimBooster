import time
import keyboard
import pyautogui
import win32api
import win32con


# Função para clicar na tela com o mouse
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 255, 195
# Criado 2 while true para controlar o funcionamento do bot
while True:
    if keyboard.is_pressed("c"):  # Apertar "c" para entrar no bot
        while True:
            """Bot funciona da seguinte forma.
            Ao entrar nesse while, ele printa a tela na regiao do game,
            em seguida ele percorre de 9 pixels a 9 pixels no plano cartesiano XY,
            dai ao encontrar o pixel com a cor RED==255 e BLUE==195,
            ele clica ali e ocorre um timeout de 8 milesimos de segundos para
            não clicar mais de uma vez no mesmo lugar."""
            scr = pyautogui.screenshot(region=(573, 459, 770, 540))
            width, height = scr.size

            for x in range(0, width, 9):
                achou = 0
                for y in range(0, height, 9):
                    r, g, b = scr.getpixel((x, y))
                    print(r, g, b)

                    if r == 255 and b == 195:
                        achou = 1
                        # pyautogui.click(573+x, 459+y)
                        click(573 + x, 459 + y)
                        time.sleep(0.08)
                        break
                if achou == 1:
                    break
            if keyboard.is_pressed("x"):  # Apertar "x" para sair do bot
                break
