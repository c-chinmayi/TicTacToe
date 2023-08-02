number_list = [i + 1 for i in range(10)]


def update_board(number_list):
    board = f"""
        |     |     
     {number_list[0]}  |  {number_list[1]}  |  {number_list[2]}  
   _ _ _|_ _ _|_ _ _
        |     |
     {number_list[3]}  |  {number_list[4]}  |  {number_list[5]}
   _ _ _|_ _ _|_ _ _
        |     |
     {number_list[6]}  |  {number_list[7]}  |  {number_list[8]}
        |     |
    """
    return board


def win_conditions(number_list):
    conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for i in conditions:
        x = i[0]
        y = i[1]
        z = i[2]
        if number_list[x] == number_list[y] == number_list[z]:
            return True
    return False


def game():
    symbol = "X"
    count = 0
    while True:
        while not win_conditions(number_list):
            print(update_board(number_list))
            if count < 9:
                print(f"It is {symbol}'s turn")
                turn = int(input("Enter the position you want to play at : "))
            if type(number_list[turn - 1]) == int:
                number_list[turn - 1] = symbol
                count = count + 1
            elif count == 9:
                print("The game is a draw!")
                break
            else:
                print("Please enter a different position")

            if symbol == "X" and not win_conditions(number_list):
                symbol = "O"
            elif not win_conditions(number_list):
                symbol = "X"

        else:
            print(update_board(number_list))
            print(symbol, "has won the game!")

        break


if __name__ == "__main__":
    game()
