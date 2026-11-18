
class Candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def __del__(self):
        pass

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes

    def set_name(self, name):
        self.name = name

    def set_votes(self, votes):
        self.votes = votes

    def show(self, total):
        print("Прізвище:", self.name)
        print("Голоси:", self.votes)
        if total > 0:
            print("Відсоток:", self.votes * 100 / total, "%")
        else:
            print("Відсоток: 0 %")


class Elections:
    def __init__(self):
        self.candidates = []

    def __del__(self):
        pass

    def add(self, candidate):
        self.candidates.append(candidate)

    def show(self):
        total = 0
        for candidate in self.candidates:
            total = total + candidate.get_votes()

        print("Усього голосів:", total)
        for candidate in self.candidates:
            candidate.show(total)

        winner = self.candidates[0]
        for candidate in self.candidates:
            if candidate.get_votes() > winner.get_votes():
                winner = candidate

        if total > 0:
            print("Переможець:", winner.get_name())
        else:
            print("Переможця немає")


def main():
    elections = Elections()
    for i in range(5):
        print("Кандидат", i + 1)
        name = input("Прізвище: ")
        votes = int(input("Кількість голосів: "))
        candidate = Candidate(name, votes)
        elections.add(candidate)

    elections.show()


main()
