Ranking Web Server
==================

A web server to set up and manage a ranking page. Normally, you would need to
install [CMS](http://cms-dev.github.io/) in order to have RWS. This "fork"
tries to ease installation of RWS by splitting it away from CMS into its own
python package.

Installation
------------

```bash
pip install rws
```

Usage
-----

```bash
$ rws --help
```

```
usage: rws [-h] [-d] [-p HTTP_PORT] [--https-port HTTPS_PORT]
           [--https-certfile HTTPS_CERTFILE] [--https-keyfile HTTPS_KEYFILE]
           [-t TIMEOUT] [-b BIND_ADDRESS] [--realm-name REALM_NAME] [-l LOGIN]
           [--buffer-size BUFFER_SIZE] [-c CONFIG] [--log-dir LOG_DIR]
           [--lib-dir LIB_DIR]

Ranking Web Server.

optional arguments:
  -h, --help            show this help message and exit
  -d, --drop            Drop the data already stored.
  -p HTTP_PORT, --http-port HTTP_PORT
                        Listening HTTP port for RankingWebServer.
  --https-port HTTPS_PORT
                        Listening HTTPS port for RankingWebServer.
  --https-certfile HTTPS_CERTFILE
                        HTTPS certificate file for RankingWebServer.
  --https-keyfile HTTPS_KEYFILE
                        HTTPS key file for RankingWebServer.
  -t TIMEOUT, --timeout TIMEOUT
                        Listening HTTPS port for RankingWebServer.
  -b BIND_ADDRESS, --bind-address BIND_ADDRESS
                        Listening address for RankingWebServer.
  --realm-name REALM_NAME
                        Realm name for authentication.
  -l LOGIN, --login LOGIN
                        Login information for adding and editing data.
  --buffer-size BUFFER_SIZE
                        Listening HTTPS port for RankingWebServer.
  -c CONFIG, --config CONFIG
                        Path to a JSON config file.
  --log-dir LOG_DIR     Directory where RWS will store log files.
  --lib-dir LIB_DIR     Directory where RWS will store runtime data.
```
