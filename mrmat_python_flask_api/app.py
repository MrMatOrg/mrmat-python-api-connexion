#  MIT License
#
#  Copyright (c) 2021 MrMatOrg
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import sys
import argparse
import connexion

from mrmat_python_flask_api import __version__, __swagger__

cnx = connexion.App(__name__, specification_dir=__swagger__)
cnx.add_api('hello-api-0_1.yaml', base_path='/api/greeting/0.1', strict_validation=True)

@cnx.app.route('/healthz')
def healthz():
    """
    Check application health
    :return: 'OK' and a 200 upon success, a descriptive message and non-200 status code otherwise
    """
    return 'OK', 200


def main() -> int:
    """
    Main entry point
    :return: Exit code
    """
    parser = argparse.ArgumentParser(description=f'mrmat-python-flask-api - {__version__}')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')
    parser.add_argument('--host',
                        dest='host',
                        required=False,
                        default='localhost',
                        help='Host interface to bind to')
    parser.add_argument('--port',
                        dest='port',
                        required=False,
                        default=8080,
                        help='Port to bind to')

    args = parser.parse_args()

    cnx.run(host=args.host, port=args.port, debug=args.debug)
    return 0


if __name__ == '__main__':
    sys.exit(main())
