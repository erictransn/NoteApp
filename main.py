from website import create_app

app = create_app()

if __name__ == '__main__':  # if we run this file execute this code below
    app.run(debug=True)
