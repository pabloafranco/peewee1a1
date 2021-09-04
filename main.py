import peewee


database = peewee.MySQLDatabase('pythondb', 
                                 host='localhost', 
                                 port=3306, 
                                 user='root', 
                                 passwd='root')

class Author(peewee.Model):
    name = peewee.CharField(max_length=50)

    class Meta:
        database = database
        db_table = 'authors'

    def __str__(self):
        return self.name

class Book(peewee.Model):
    title = peewee.CharField(max_length=50)
    author = peewee.ForeignKeyField(Author)

    class Meta:
        database = database
        db_table = 'books'

    def __str__(self):
        return self.title


if __name__ == '__main__':
    database.drop_tables([Author, Book])
    database.create_tables([Author, Book])

    author1 = Author.create(name='Stephen Key')

    book1 = Book.create(title='It', author=author1)
    book1 = Book.create(title='El resplandor', author=author1)
    book1 = Book.create(title='Cujo', author=author1)
