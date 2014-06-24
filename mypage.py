__author__ = 'salman wahed'

import webapp2


class MainPage(webapp2.RedirectHandler):
    def get(self, *args, **kwargs):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, I am Salman Wahed')


application = webapp2.WSGIApplication([('/', MainPage),], debug=True)