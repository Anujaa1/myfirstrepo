questions = [
    ["What is the powerhouse of the cell?", "Mitochondria", "Vacuole", "Nucleus", "Cytoplasm", None, 0],
    ["Which organelle is responsible for photosynthesis?", "Mitochondria", "Chloroplast", "Nucleus", "Cytoplasm", None, 1],
    ["What structure protects and supports the cell?", "Cell Membrane", "Nucleus", "Mitochondria", "Endoplasmic Reticulum", None, 0],
    ["Where is the genetic material of the cell stored?", "Nucleus", "Cytoplasm", "Mitochondria", "Vacuole", None, 0],
    ["What organelle is involved in protein synthesis?", "Ribosome", "Vacuole", "Nucleus", "Mitochondria", None, 0],
    ["Which organelle is involved in digestion within the cell?", "Lysosome", "Nucleus", "Mitochondria", "Vacuole", None, 0],
    ["What part of the cell controls what enters and exits?", "Cell Membrane", "Vacuole", "Cytoplasm", "Nucleus", None, 0],
    ["Where does cellular respiration take place?", "Mitochondria", "Nucleus", "Chloroplast", "Endoplasmic Reticulum", None, 0],
    ["What is the fluid-like substance inside the cell?", "Cytoplasm", "Nucleus", "Mitochondria", "Vacuole", None, 0],
    ["What is the function of the vacuole?", "Storage of water and nutrients", "Protein synthesis", "Genetic information storage", "Cell division", None, 0]
]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
money = 0  # Initialize money before the loop

for i in range(len(questions)):
    question = questions[i]  # Get the current question
    
    # Display the question and options
    print(f"\nQuestion for Rs {levels[i]}")
    print(f"{question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    reply = int(input("Enter your answer (1-4): "))

    if reply - 1 == question[-1]:  # Convert user input (1-based to 0-based)
        print(f"Correct answer! You have won Rs {levels[i]}")
        money = levels[i]  # Update winnings
    else:
        print("Wrong answer!")

        # Assign guaranteed money levels
        if i >= 4 and i < 8:
            money = 3000
        elif i >= 8:
            money = 5000
        elif i == 9:
            money = 6000

        print(f"Now you have Rs {money}")
        break  # Stop the game after a wrong answer

print(f"\nYour total amount is Rs {money}")  # Final amount
