import turtle

def art():
    def draw_circle_pattern(radius, num_circles):
        """Draw a pattern of circles."""
        for _ in range(num_circles):
            turtle.circle(radius)
            turtle.right(360 / num_circles)

    def draw_square_spiral(size):
        """Draw a square spiral."""
        for i in range(size):
            turtle.forward(i * 10)
            turtle.right(90)

    def draw_star(size, color):
        """Draw a filled star."""
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            turtle.right(144)
        turtle.end_fill()

    def draw_polygon(sides, size, color):
        """Draw a filled polygon based on the number of sides."""
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(sides):
            turtle.forward(size)
            turtle.right(360 / sides)
        turtle.end_fill()

    def draw_fractal(x, y, size):
        """Draw a simple fractal."""
        if size < 10:
            return
        else:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            for _ in range(3):
                turtle.forward(size)
                draw_fractal(turtle.xcor(), turtle.ycor(), size / 2)
                turtle.right(120)

    def main():
        turtle.title("Complex Art Creation Tool")
        turtle.bgcolor("black")  
        turtle.speed(0)  
        turtle.color("white")

        while True:
            shape = input("Enter a shape to draw (circle_pattern, square_spiral, star, polygon, fractal) or 'erase' to clear, or 'quit' to exit: ").lower()

            if shape == "quit":
                break

            elif shape == "erase":
                turtle.clear() 
                turtle.penup() 
                turtle.goto(0, 0)  
                turtle.pendown()  
                continue  

            if shape == "circle_pattern":
                radius = int(input("Enter the radius of the circles: "))
                num_circles = int(input("Enter the number of circles: "))
                draw_circle_pattern(radius, num_circles)

            elif shape == "square_spiral":
                size = int(input("Enter the size of the square spiral: "))
                draw_square_spiral(size)

            elif shape == "star":
                size = int(input("Enter the size of the star: "))
                color = input("Enter the color of the star: ")
                draw_star(size, color)

            elif shape == "polygon":
                sides = int(input("Enter the number of sides of the polygon: "))
                size = int(input("Enter the size of the polygon: "))
                color = input("Enter the color of the polygon: ")
                draw_polygon(sides, size, color)

            elif shape == "fractal":
                size = int(input("Enter the size of the fractal: "))
                draw_fractal(0, 0, size)  

            else:
                print("Invalid shape. Please try again.")

        turtle.hideturtle() 
        turtle.done()  

    main()

if __name__ == "__main__":
    art()
