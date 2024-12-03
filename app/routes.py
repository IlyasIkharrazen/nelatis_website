from flask import Blueprint, render_template

main = Blueprint('main', __name__)  # Création du Blueprint

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/blog-details')
def blog_details():
    return render_template('blog-details.html')

@main.route('/portofolio')
def portofolio_details():
    return render_template('portofolio-details.html')

@main.route('/services')
def services_details():
    return render_template('services-details.html')
