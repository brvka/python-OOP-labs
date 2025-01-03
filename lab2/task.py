class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализировать объект "Книга"

        :param id_: Идентификатор книги
        :param name: Имя книги
        :param pages: Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга '{self.name}'"

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализировать объект "Библиотека"

        :param books: Список книг в библиотеке
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Вернуть идентификатор для добавления новой книги в библиотеку

        :return: Идентификатор
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Вернуть индекс книги в списке books по id книги

        :raise ValueError: Если книги с таким id не существует, то вызываем ошибку

        :param book_id: Идентификатор книги
        :return: Индекс книги в библиотеке
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
