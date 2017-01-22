from flask import Flask, render_template
import sqlite3
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return render_template('testmap.html')
    db = sqlite3.connect('conuhacks')
    db.cursor()
    data = db.execute ('select lat,lon,name,avg_sentiment_score from places')
    myobject = {}
    myobject['places'] = []
    for rows in data:
        myelement = {"lat":rows[0], "lng":rows[1], "name":rows[2],"rating":rows[3]}
        myobject['places'].append(myelement)
    return render_template('iconmap.html', objects=myobject)

from flask.views import View

class ShowUsers(View):

    def dispatch_request(self):
        db = sqlite3.connect('conuhacks')
        db.cursor()
        data = db.execute ('select lat,lon,name,avg_sentiment_score from places')
        myobject = {}
        myobject['places'] = []
        for rows in data:
            myelement = {"lat":rows[0], "lng":rows[1], "name":rows[2],"rating":rows[3]}
            myobject['places'].append(myelement)
        return render_template('iconmap.html', objects=myobject)

# app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

from flask.views import View

class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))