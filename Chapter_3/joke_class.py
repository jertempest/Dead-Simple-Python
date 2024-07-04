class Joke:
    def __init__(self, joke_type):
        if joke_type == "funny":
            self.question = "How can you tell if an elephant is in your fridge?"
            self.answer = "There are footprints in the butter!"
        elif joke_type == "lethal":
            self.question = "Wenn ist das Nunstuck git und Slotermeyer?" 
            self.answer = "JA! Beiherhund das Oder die Flipperwaldt gersput!"
        else:
            self.question = "Why did chicken cross the road?"
            self.answer = "To get to the other side!"
    def tell(self):
        print(self.question)
        print(self.answer)
lethal_joke = Joke("lethal")
lethal_joke.tell()