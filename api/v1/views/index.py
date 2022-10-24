 
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', method=['GET'], strict_slashes=false)

def status():
    """retrurn a status"""
    return jsonify[{"status": "OK"}]
