#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2
from collections import defaultdict
from prettytable import PrettyTable

zap = ZAPv2()
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8787', 'https': 'http://127.0.0.1:8787'})
alerts = zap.core.alerts()
#pprint (zap.core.alerts())

# create a data structure to match our output
sort_by_url = defaultdict(list)
for alert in alerts:
    sort_by_url[alert['url']].append({
                                'risk':  alert['risk'],
                                'alert': alert['alert']
                                })

# print a useful set of tables of the alerts
for url in sort_by_url:
    print
    print url

    results = PrettyTable(["Risk", "Description"])
    results.padding_width = 1
    results.align = "l"
    results.sortby = "Risk"

    for details in sort_by_url[url]:
        results.add_row([details['risk'], details['alert']])
    print results
