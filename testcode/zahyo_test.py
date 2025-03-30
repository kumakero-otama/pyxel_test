import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Moving Circle")
        self.x = 80  # 初期X座標
        self.y = 60  # 初期Y座標
        self.speed = 2  # 移動速度
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, 5, 7)  # 円を描画

App()
