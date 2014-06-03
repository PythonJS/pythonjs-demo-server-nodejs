#!/usr/bin/env node
var fs = require('fs')
//var pythonjs = require('../PythonJS/pythonjs/python-js')
var pythonjs = require('python-js')
var pycode = fs.readFileSync( './server.py', {'encoding':'utf8'} )
var jscode = pythonjs.translator.to_javascript( pycode )
eval( pythonjs.runtime.javascript + jscode )