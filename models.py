import json


class Books:
    def __init__(self):
        try:
            with open("books.json", "r", encoding="UTF-8") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books

    def get(self, id):
        return self.books[id]

    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w", encoding="UTF-8") as f:
            json.dump(self.books, f, ensure_ascii=False)

    def update(self, id, data):
        data.pop('csrf_token')
        self.books[id] = data
        self.save_all()


books = Books()
