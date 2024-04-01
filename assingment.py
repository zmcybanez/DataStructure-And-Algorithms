import numpy as np
import matplotlib.pyplot as plt

#READS THE EQUATIONS FROM TXT FILE
def read_equations_from_file(filename):
    equations = []
    with open('equations.txt', 'r') as file:
        for line in file:
            equation_str = line.strip()
            equation = lambda x, eq=equation_str: eval(eq)
            equations.append(equation)
    return equations

def solve_expression(x_values, expression):
    y_values = [max(0, expression(x)) for x in x_values]
    return y_values

def write_to_file(x_values, y_values_dict):
    with open("output.txt", "w") as file:
        for expression_name, values in y_values_dict.items():
            file.write(f"{expression_name}:\n")
            for value in values:
                file.write(f"{int(round(value))}\n")  # Write rounded integer value
            file.write("\n")

# Now, you can use these functions as described previously
x_values = list(range(1, 51))
equations = read_equations_from_file("equations.txt")
y_values_dict = {}
for i, equation in enumerate(equations):
    expression_name = f"Expression {i+1}"
    y_values = solve_expression(x_values, equation)
    y_values_dict[expression_name] = y_values

write_to_file(x_values, y_values_dict)

def main():
    # Read equations from file
    filename = 'equations.txt'  # Replace with the name of your file
    equations = read_equations_from_file(filename)

    # Prompt the user to choose an option
    print("Choose an option:")
    print("1. Graph a single equation")
    print("2. Graph all equations")

    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()

    # Define the range of x values
    x_values = np.linspace(0, 50)  # Adjust the range as needed

    # Plot the selected option
    if option == 1:
        print("Choose an equation to graph (1-10):")
        for i in range(len(equations)):
            print(f"{i+1}. Equation {i+1}")

        try:
            choice = int(input("Enter your choice: ")) - 1
            if choice < 0 or choice >= len(equations):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid equation number.")
            exit()

        # Plot the chosen equation
        plt.figure()
        y_values = equations[choice](x_values)
        plt.plot(x_values, y_values, label=f'Equation {choice+1}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of Equation {choice+1}')
        plt.legend()
        plt.grid(True)
        plt.show()

    elif option == 2:
        # Plot all equations
        plt.figure()
        for i, equation in enumerate(equations):
            y_values = equation(x_values)
            plt.plot(x_values, y_values, label=f'Equation {i+1}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graphs of all Equations')
        plt.xlim(left=0)
        plt.ylim(bottom=0)
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
