## Using mitm proxy and custom addons
### Download mitm:
```sh
    wget https://github.com/mitmproxy/mitmproxy/releases/download/v4.0.1/mitmproxy-4.0.1-linux.tar.gz
```

### Setup mitm
```sh
    tar xvf mitmproxy-4.0.1-linux.tar.gz
    cp mitm* /usr/local/bin
```

### Test mitm, dump traffic to outfile
```sh
    mitmdump -w outfile
```
### Start mitm with your addon (parser)
```sh
    mitmdump --set block_global=false --anticomp -s addons/dump_http.py
```
dump_http addon is performing below tasks

- Intercept all incoming traffic
- Optionally, you can parse requests only for specific domain. In this example, it is ```google.com```
- Creates a dump file called ```dump_http.txt```, and for each request/response, write following info
    ```sh
       - request domain
       - request url
       - request method
       - request headers
       - request body
       - response headers
       - response body     
    ```