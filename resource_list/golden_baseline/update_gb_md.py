import os
import re
import pprint
from jinja2 import Template 

resource_path = os.getcwd()+r"\global_variable"
list_dir = os.listdir(resource_path)
# pprint.pprint(list_dir)
# ['sFlow',
# 'show aaa server [Alcatel Lucent OmniSwitch]',
# 'show access-list [Cisco IOS]',
# 'show ap association [Aruba WLC]',
# 'show ap database summary [Aruba WLC]',
# 'show apm access-info all-properties [F5 Load Balancer]',
# 'show bgp all summary [Cisco IOS]',
# 'show bgp neighbor [JUNOS Common]']

# total_num = len(list_dir)
# print(total_num)

vendor_tree = {}
total_num = 0

re_match = r'(.+?)(\[.+\])'
for names in list_dir:
    res = re.match(re_match,names)
    if res and res.group(1):
        cli = res.group(1)
        vendor = res.group(2)
        if "DVT" not in vendor:
            total_num+=1

            if vendor not in vendor_tree:
                vendor_tree[vendor]=[]
            vendor_tree[vendor].append(cli)

print(total_num)
# pprint.pprint(vendor_tree)

vendor_readme_template ='''
# Baseline CLI Group by Vendor
{% for vendor in vendor_tree %}
## {{vendor}}
{% for cli in vendor_tree[vendor] %}
* {{cli}}
{% endfor %}
{% endfor %}
'''
vendor_res = Template(vendor_readme_template)
vendor_res_txt = vendor_res.render(vendor_tree=vendor_tree)
# print(vendor_res_txt)

with open('byVendor.md','w', newline='') as f_readme1:
    f_readme1.write(vendor_res_txt)
f_readme1.close()
