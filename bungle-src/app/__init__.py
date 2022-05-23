import re
import bottle
from bottle import response, request, template
from . import project2

bottle.TEMPLATE_PATH = ['./app/views']
app = bottle.default_app()

class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)

        return _enable_cors

class EnforceBrowser(object):
    name = 'enforce_browser'
    api = 2

    def apply(self, fn, context):
        def _enforce_browser(*args, **kwargs):
            regex = '^Mozilla\/5.0 \(([^)]+)\) Gecko\/20100101 Firefox\/(.*)$'
            expected = '78.0'

            agent = request.headers['user-agent']
            match = re.match(regex, agent)
            actual = match and match.group(2)

            if actual != expected:
                return template('error_version', expected=expected, actual=actual)
            else:
                return fn(*args, **kwargs)

        return _enforce_browser

app.install(EnableCors())
app.install(EnforceBrowser())
