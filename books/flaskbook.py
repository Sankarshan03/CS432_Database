from flask import Flask, render_template, url_for

app = Flask(__name__)

details = [{
        'book_id': '1',
        'title': 'The Great Gatsby',
        'edition':'1',
        'copies':'10',
        'availability_status':'true',
        'publisher_id':'11',
        'author_id':'1'
        },{
        'book_id': '2',
        'title': 'To Kill a Mockingbird',
        'edition':'2',
        'copies':'15',
        'availability_status':'true',
        'publisher_id':'12',
        'author_id':'2'
        },{
        'book_id': '3',
        'title': '1984',
        'edition':'1',
        'copies':'5',
        'availability_status':'false',
        'publisher_id':'13',
        'author_id':'3'
        },{
        'book_id': '4',
        'title': 'Pride and Prejudice',
        'edition':'3',
        'copies':'20',
        'availability_status':'true',
        'publisher_id':'14',
        'author_id':'4'
        },{
        'book_id': '5',
        'title': 'The Catcher in the Rye',
        'edition':'2',
        'copies':'8',
        'availability_status':'false',
        'publisher_id':'15',
        'author_id':'5'
        },{ 
        'book_id': '6',
        'title': 'The Hobbit',
        'edition':'1',
        'copies':'12',
        'availability_status':'true',
        'publisher_id':'16',
        'author_id':'6'
        },{
        'book_id': '7',
        'title': 'Lord of the Flies',
        'edition':'1',
        'copies':'6',
        'availability_status':'true',
        'publisher_id':'17',
        'author_id':'7'
        },{
        'book_id': '8',
        'title': 'Animal Farm',
        'edition':'2',
        'copies':'10',
        'availability_status':'false',
        'publisher_id':'18',
        'author_id':'8'
        },{
        'book_id': '9',
        'title': 'The Odyssey',
        'edition':'1',
        'copies':'7',
        'availability_status':'true',
        'publisher_id':'19',
        'author_id':'9'
        },{ 
        'book_id': '10',
        'title': 'The Sun Also Rises',
        'edition':'3',
        'copies':'3',
        'availability_status':'true',
        'publisher_id':'20',
        'author_id':'10'
        }]

@app.route("/")
@app.route("/book")


def book():
    return render_template('booktem.html',details=details)

@app.route("/contact us")
def contact():
    return "<h1>contact us</h1>"

@app.route("/author")
def author():
    return "<h1>Author</h1>"
@app.route("/login")
def login():
    return "<h1>log in</h1>"
if __name__ =='__main__':
    app.run(debug=True)