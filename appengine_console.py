#!/usr/bin/python
import code
import getpass
import sys

sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine")
sys.path.append("/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/yaml/lib")
sys.path.append('', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Library/Python/2.7/site-packages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC', '/Library/Python/2.7/site-packages/pingpp-2.0.11-py2.7.egg', '/Library/Python/2.7/site-packages/pycrypto-2.6.1-py2.7-macosx-10.11-intel.egg', '/Library/Python/2.7/site-packages/qrcode-5.3-py2.7.egg', '/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg', '/Library/Python/2.7/site-packages/pyquery-1.2.17-py2.7.egg', '/Library/Python/2.7/site-packages/cssselect-1.0.1-py2.7.egg', '/Library/Python/2.7/site-packages/lxml-3.7.2-py2.7-macosx-10.12-intel.egg', '/Library/Python/2.7/site-packages/pandas-0.19.2-py2.7-macosx-10.12-intel.egg', '/Library/Python/2.7/site-packages/pycurl-7.43.0-py2.7-macosx-10.12-intel.egg', '/Library/Python/2.7/site-packages/web.py-0.40.dev0-py2.7.egg', '/Library/Python/2.7/site-packages/Sphinx-1.6b1-py2.7.egg', '/Library/Python/2.7/site-packages/typing-3.6.1-py2.7.egg', '/Library/Python/2.7/site-packages/sphinxcontrib_websupport-1.0.0-py2.7.egg', '/Library/Python/2.7/site-packages/imagesize-0.7.1-py2.7.egg', '/Library/Python/2.7/site-packages/alabaster-0.7.10-py2.7.egg', '/Library/Python/2.7/site-packages/Babel-2.4.0-py2.7.egg', '/Library/Python/2.7/site-packages/snowballstemmer-1.2.1-py2.7.egg', '/Library/Python/2.7/site-packages/docutils-0.13.1-py2.7.egg', '/Library/Python/2.7/site-packages/Whoosh-2.7.4-py2.7.egg', '/Library/Python/2.7/site-packages/SQLAlchemy-1.1.9-py2.7-macosx-10.12-intel.egg')
from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
    return raw_input('Username:'), getpass.getpass('Password:')

if len(sys.argv) < 2:
    print "Usage: %s app_id [host]" % (sys.argv[0],)
app_id = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]
else:
    host = '%s.appspot.com' % app_id

remote_api_stub.ConfigureRemoteDatastore(app_id, '/remote_api', auth_func, host)

code.interact('App Engine interactive console for %s' % (app_id,), None, locals())