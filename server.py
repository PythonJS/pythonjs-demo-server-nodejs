import tornado, tornado.web, tornado.ioloop

class MainHandler( tornado.web.RequestHandler ):
	def get(self, path=None):
		print('path', path)
		self.write('hello world')

handlers = [
	('/', MainHandler)

]

app = tornado.web.Application( handlers )
app.listen( 8080 )
tornado.ioloop.IOLoop.instance().start()
