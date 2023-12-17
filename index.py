from flask import render_template, request
import dao
from app import app  # Đã import app từ __init__.py
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def index():
    products = dao.get_product()
    category = dao.get_category()

    return render_template("index.html", hello = category ,products = category)

if __name__ == '__main__':
    app.run(debug=True)