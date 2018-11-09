from flask import render_template
from . import main

@main.app_error handler(404)
def four_Ow_four (error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404