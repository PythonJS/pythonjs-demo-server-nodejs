pythonjs demo server
===========================

This project shows you how to install the NodeJS package, and how it can be used to write a dynamic transpiling server.  First, git clone this repo, and then run: `npm install python-js'.  Now you are ready to run the server, run: `./run-demo.js` and then open your browser to `localhost:8080`.

run-demo.js is a small wrapper script that reads in server.py, translates it to javascript and eval's the code.  server.py is written using a subset of the Tornado Web API that PythonJS is able to translate into the NodeJS `http` API.

run-demo.js
-----------

```
	#!/usr/bin/env node
	var fs = require('fs')
	var pythonjs = require('python-js')
	var pycode = fs.readFileSync( './server.py', {'encoding':'utf8'} )
	var jscode = pythonjs.translator.to_javascript( pycode )
	eval( pythonjs.runtime.javascript + jscode )

```