def response(flow):
    print("")
    print("="*50)
    print(flow.request.method + " " + flow.request.path + " " + flow.request.http_version)

    print("-"*50 + "request headers:")
    for k, v in flow.request.headers.items():
        print("%-20s: %s" % (k.upper(), v))

    print("-"*50 + "response headers:")
    for k, v in flow.response.headers.items():
        print("%-20s: %s" % (k.upper(), v))
        print("-"*50 + "request headers:")