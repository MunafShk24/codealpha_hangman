import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def draw_screen(screen, word, guessed_letters, attempts):
    screen.fill(WHITE)
    text = FONT.render(display_word(word, guessed_letters), True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    attempts_text = FONT.render(f'Attempts left: {attempts}', True, BLACK)
    screen.blit(attempts_text, (WIDTH // 2 - attempts_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman Game")
    running = True
    
    while running and attempts > 0:
        screen.fill(WHITE)
        draw_screen(screen, word, guessed_letters, attempts)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    guess = event.unicode.lower()
                    if guess in guessed_letters:
                        continue
                    guessed_letters.add(guess)
                    if guess not in word:
                        attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")
    
    pygame.quit()

if __name__ == "__main__":
    hangman()