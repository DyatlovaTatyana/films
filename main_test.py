from main import MoviesLibrary


def test_add_movie():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    library.add_movie('Комедия', 'Весёлый питонист')
    library.add_movie('Комедия', 'Три разраба и тестировщик')
    library.add_movie('Ужасы', 'Спойлер домашки')
    library.add_movie('Романтика', 'Я и питон сидим вечером')

    actual = library.recommend('Комедия')
    expected = ['Весёлый питонист', 'Три разраба и тестировщик']
    assert actual==expected