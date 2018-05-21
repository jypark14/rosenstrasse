class InputBox:
    #initalize variables
    def __init__(self, x, y, w, h, name, text='0'):
        self.sum = 0
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.name = name

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            #adds  new risk if clicked upon when facilitator presses enter
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.sum = self.sum + int(self.text)
                    print(self.sum)
                    self.text = str(self.sum)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        screen.blit(FONT.render(self.name, True, self.color),
(self.rect.x-70, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)



def main():
    clock = pygame.time.Clock()
    screen.blit
    #creates risk matrixes for each character
    input_box1 = InputBox(500, 100, 140, 32, "Kurt")
    input_box2 = InputBox(500, 200, 140, 32, "Josef")
    input_box3 = InputBox(500, 300, 140, 32, "Max")
    input_box4 = InputBox(500, 400, 140, 32, "Izak")
    input_boxes = [input_box1, input_box2, input_box3, input_box4]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()

