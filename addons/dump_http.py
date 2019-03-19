import re
import json

delimeter = '#####'


def response(flow):
    with open("dump_http.txt", "a") as ofile:

        outputString = ''

        ## DOMAIN or HOST
        outputString = outputString + 'DOMAIN:' + flow.request.pretty_host + delimeter

        ## Filter specific domain
        if bool(re.search('google.com', flow.request.pretty_host)):

            ## URL
            outputString = outputString + 'URL:' + flow.request.pretty_url + delimeter

            ## METHOD
            outputString = outputString + 'METHOD:' + flow.request.method + delimeter

            # REQUEST HEADERS
            data = {}
            for k, v in flow.request.headers.items():
                data[k] = v

            request_headers_json = json.dumps(data)
            outputString = outputString + 'REQUEST_HEADERS:' + request_headers_json + delimeter

            # REQUEST BODY
            if flow.request.content:
                outputString = outputString + "REQUEST:" + flow.request.content.decode() + delimeter

            # RESPONSE BODY
            if flow.response.content:
                outputString = outputString + "RESPONSE:" + flow.response.content.decode()


        ofile.write(outputString)
        ofile.write("\n-----------------------------------separator----------------------------------------------------\n")
