#!/usr/bin/env python
# coding=utf-8

from webapp import app


def main():
    # app.run(debug=True, port=5000, host="0.0.0.0")
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()
