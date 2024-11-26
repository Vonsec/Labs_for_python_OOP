class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Инициализирует библиотеку с заданным списком книг.
        Если список не передан, инициализирует пустую библиотеку.

        :param books: Список экземпляров класса Book (по умолчанию None)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор для добавления новой книги.
        Если библиотека пуста, возвращает 1.
        Иначе возвращает идентификатор последней книги + 1.

        :return: Следующий идентификатор книги (int)
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её идентификатору.
        Если книги с таким идентификатором нет, вызывает ValueError.

        :param book_id: Идентификатор книги (int)
        :return: Индекс книги в списке (int)
        :raises ValueError: Если книга с заданным id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]

if __name__ == "__main__":
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
