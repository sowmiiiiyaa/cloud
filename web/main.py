
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("""
        <html>
        <head>
            <title>My First Web Application</title>
        </head>
        <body>
            <h1>Welcome to Google App Engine</h1>
            <p>This is my first web application using Python.</p>
        </body>
        </html>
        """)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
