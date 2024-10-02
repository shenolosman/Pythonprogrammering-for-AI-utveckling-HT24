fileName = "week3-lab/results.txt"


def read_results():
    try:
        with open(fileName, "r") as fil:
            results = fil.readlines()
            return [row.strip() for row in results[-5:]]
    except FileNotFoundError:
        return []


def save_results(new_results):
    with open(fileName, "a") as fil:
        fil.write(f"{new_results}\n")


def show_results():
    results = read_results()
    if results:
        print("\nSenaste 5 resultsen:")
        for row in results:
            print(row)
    else:
        print("Inga results hittades.")
