#!/usr/bin/env node
var fs = require('fs')
//var pythonjs = require('../PythonJS/pythonjs/python-js')
var pythonjs = require('python-js')
console.log(pythonjs)

var pycode = fs.readFileSync( './server.py', {'encoding':'utf8'} )

var jscode = pythonjs.translator.to_javascript( pycode )
//console.log(jscode)
eval( pythonjs.runtime.javascript + jscode )