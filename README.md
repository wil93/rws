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
  -d, --drop            Drop the data already stored. (default: False)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Listening HTTP port for RankingWebServer. (default:
                        8890)
  --https-port HTTPS_PORT
                        Listening HTTPS port for RankingWebServer. (default:
                        None)
  --https-certfile HTTPS_CERTFILE
                        HTTPS certificate file for RankingWebServer. (default:
                        None)
  --https-keyfile HTTPS_KEYFILE
                        HTTPS key file for RankingWebServer. (default: None)
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout. (default: 600)
  -b BIND_ADDRESS, --bind-address BIND_ADDRESS
                        Listening address for RankingWebServer. (default: )
  --realm-name REALM_NAME
                        Realm name for authentication. (default: Scoreboard)
  -l LOGIN, --login LOGIN
                        Login information for adding and editing data.
                        (default: usern4me:passw0rd)
  --buffer-size BUFFER_SIZE
                        Buffer size. (default: 100)
  -c CONFIG, --config CONFIG
                        Path to a JSON config file. (default: None)
  --log-dir LOG_DIR     Directory where RWS will store log files. (default:
                        /var/local/log/cms/ranking)
  --lib-dir LIB_DIR     Directory where RWS will store runtime data. (default:
                        /var/local/lib/cms/ranking)
```
