__author__ = 'salman wahed'

import webapp2
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        t = jinja_env.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))


class MainPage(Handler):
    def get(self):
        items = self.request.get_all('food')
        self.render('shoping_list.html', items=items)


class FizzBuzz(Handler):
    def get(self):
        n = self.request.get("n")
        if n:
            n = int(n)
        else:
            n = 0
        self.render('fizzbuzz.html', n=n)


application = webapp2.WSGIApplication([('/', MainPage), ('/fizzbuzz', FizzBuzz)], debug=True)