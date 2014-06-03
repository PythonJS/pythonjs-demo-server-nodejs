import tornado, tornado.web, tornado.ioloop
import os

PATHS = { 'webroot': './html'}

def get_main_page(server):
	root = PATHS['webroot']
	r = ['<html><head><title>index</title></head><body>']
	r.append( '<ul>' )
	files = os.listdir( root )
	files.sort()
	for name in files:
		path = os.path.join( root, name )
		if os.path.isfile( path ):
			r.append( '<a href="%s"><li>%s</li></a>' %(name,name) )
	r.append('</ul>')
	r.append('</body></html>')
	return ''.join(r)


def convert_python_html_document( data ):
	'''
	rewrites html document, converts python scripts into javascript.
	example:
		<script type="text/python">
		print("hello world")
		</script>

	'''
	doc = list()
	script = None
	for line in data.splitlines():

		if line.strip().startswith('<script'):

			if 'type="text/python"' in line:
				doc.append( '<script type="text/javascript">')
				script = list()
			else:
				doc.append( line )

		elif line.strip() == '</script>':
			if script:
				#src = '\n'.join( script )  ## TODO fix '\n'
				src = chr(10).join(script)
				js = pythonjs.translator.to_javascript( src )
				doc.append( js )
			doc.append( line )
			script = None

		elif isinstance( script, list ):
			script.append( line )

		else:
			doc.append( line )

	return '\n'.join( doc )



class MainHandler( tornado.web.RequestHandler ):
	def get(self, path=None):
		print('path', path)

		if not path:
			self.write( get_main_page() )
		elif path == 'pythonjs.js':
			data = pythonjs.runtime.javascript
			self.set_header("Content-Type", "text/javascript; charset=utf-8")
			self.set_header("Content-Length", len(data))
			self.write(data)
		else:
			local_path = os.path.join( PATHS['webroot'], path )
			if os.path.isfile( local_path ):
				data = open(local_path, 'r').read()
				if path.endswith( '.html' ):
					data = convert_python_html_document( data )
					self.set_header("Content-Type", "text/html; charset=utf-8")

				else:  ## only html files are allowed in the webroot
					raise tornado.web.HTTPError(404)

				self.set_header("Content-Length", len(data))
				self.write( data )


handlers = [
	('/', MainHandler)

]

app = tornado.web.Application( handlers )
app.listen( 8080 )
tornado.ioloop.IOLoop.instance().start()
