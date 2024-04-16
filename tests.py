import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    @pytest.mark.parametrize('name_books', ['Жареные зеленые помидоры в кафе "Полустанок"'])
    def test_add_new_book_add_book_more_than_40_characters(self, collector, name_books):
        collector.add_new_book(name_books)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name_books', ['Гордость и предубеждение и зомби'])
    def test_add_new_book_add_two_identical_books(self, collector, name_books):
        collector.add_new_book(name_books)
        collector.add_new_book(name_books)
        assert len(collector.get_books_genre()) != 2

    def test_add_new_book_the_added_book_has_no_genre(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert {'Что делать, если ваш кот хочет вас убить':''} == collector.get_books_genre()

    def test_add_new_book_set_book_genre(self, collector):
        collector.add_new_book('Падение Гипериона')
        collector.set_book_genre('Падение Гипериона','Фантастика')
        assert {'Падение Гипериона':'Фантастика'} == collector.get_books_genre()

    def test_the_genre_of_the_book_by_name(self, collector):
        collector.add_new_book('Падение Гипериона')
        collector.set_book_genre('Падение Гипериона', 'Фантастика')
        assert 'Фантастика' in collector.get_book_genre('Падение Гипериона')

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Падение Гипериона')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Падение Гипериона', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_suitable_for_children(self, collector):
        collector.add_new_book('Падение Гипериона')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Падение Гипериона', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_books_for_children() == ['Падение Гипериона', 'Что делать, если ваш кот хочет вас убить']

    def test_adding_a_book_to_favorites(self, books, collector):
        collector.add_new_book(books)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()

    def test_deleting_a_book_from_favorites(self, books, collector):
        collector.add_new_book(books)
        collector.add_book_in_favorites(books)
        collector.delete_book_from_favorites(books)
        assert books not in collector.get_list_of_favorites_books()
