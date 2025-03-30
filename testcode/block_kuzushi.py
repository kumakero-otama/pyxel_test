import pyxel

class BlockBreaker:
    def __init__(self):
        pyxel.init(160, 120, title="Block Breaker")
        self.score = 0
        self.page = 1
        self.paddle_x = 70
        self.ball_x = 80
        self.ball_y = 60
        self.ball_dx = 2
        self.ball_dy = 2
        self.blocks = [(x, y) for x in range(20, 140, 20) for y in range(10, 40, 10)]
        pyxel.run(self.update, self.draw)

    def update(self):
        # ページ1
        if self.page == 1:
            # パドルの移動
            if pyxel.btn(pyxel.KEY_LEFT) and self.paddle_x > 0:
                self.paddle_x -= 3
            if pyxel.btn(pyxel.KEY_RIGHT) and self.paddle_x < 120:
                self.paddle_x += 3
            
            # ボールの移動
            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy
            
            # 壁との衝突
            if self.ball_x <= 0 or self.ball_x >= 159:
                self.ball_dx *= -1
            if self.ball_y <= 0:
                self.ball_dy *= -1
            
            # パドルとの衝突
            if (self.paddle_x <= self.ball_x <= self.paddle_x + 40) and (self.ball_y >= 110):
                self.ball_dy *= -1
            
            # ブロックとの衝突
            new_blocks = []
            for bx, by in self.blocks:
                if bx <= self.ball_x <= bx + 18 and by <= self.ball_y <= by + 8:
                    self.ball_dy *= -1
                    self.score += 1
                else:
                    new_blocks.append((bx, by))
            self.blocks = new_blocks
            
            # ボールが下に落ちたらリセット
            if self.ball_y > 120:
                self.page = 2
                #self.ball_x, self.ball_y = 80, 60
                #self.ball_dx, self.ball_dy = 2, 2

            # クリアか判定
            if self.score == 18:
                self.page = 3

        # ページ2
        if self.page == 2:
            # リトライ
            if pyxel.btn(pyxel.KEY_R):
                self.page = 1
                self.ball_x, self.ball_y = 80, 60
                self.ball_dx, self.ball_dy = 2, 2

        # ページ3
        if self.page == 3:
            # リトライ
            if pyxel.btn(pyxel.KEY_R):
                self.page = 1
                self.ball_x, self.ball_y = 80, 60
                self.ball_dx, self.ball_dy = 2, 2


    def draw(self):
        pyxel.cls(0)

        # ページ1（ゲーム画面）の描画
        if self.page == 1:
            # ボール・ブロックの表示
            pyxel.rect(self.paddle_x, 115, 40, 5, 7)
            pyxel.circ(self.ball_x, self.ball_y, 3, 8)
            for bx, by in self.blocks:
                pyxel.rect(bx, by, 18, 8, 9)

            # スコアの表示
            pyxel.text(5, 5, f"Score: {self.score}", 7)

        # ページ2（ゲームオーバー画面）の描画    
        if self.page == 2:
            pyxel.text(63,50,f"GAMEOVER",pyxel.COLOR_RED)
            pyxel.text(63,60,f"RETRY:[R]",pyxel.COLOR_WHITE)
            pyxel.text(63,70,f"QUIT:[Q]",pyxel.COLOR_WHITE)

        # ページ3（ゲームクリア画面）の描画
        if self.page == 3:
            pyxel.text(63,55,f"GAMECLEAR!",pyxel.COLOR_YELLOW)
            pyxel.text(63,60,f"RETRY:[R]",pyxel.COLOR_WHITE)
            pyxel.text(63,70,f"QUIT:[Q]",pyxel.COLOR_WHITE)


BlockBreaker()
