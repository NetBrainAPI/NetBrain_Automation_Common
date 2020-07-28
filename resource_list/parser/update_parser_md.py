import os
import re
import pprint
from jinja2 import Template 

resource_path = os.getcwd()+r"\Network Vendors"

total_num = 0
vendor_tree = {}

# ['sFlow',
# 'show aaa server [Alcatel Lucent OmniSwitch]',
# 'show access-list [Cisco IOS]',
# 'show ap association [Aruba WLC]',
# 'show ap database summary [Aruba WLC]',
# 'show apm access-info all-properties [F5 Load Balancer]',
# 'show bgp all summary [Cisco IOS]',
# 'show bgp neighbor [JUNOS Common]']

for (dirpath, dirnames, filenames) in os.walk(resource_path):
    p_path = dirpath.split("\\")
    re_match = r'(.+?)(\[.+\])'
    p_name = p_path[-1]
    if "[" in p_name:
        res = re.match(re_match, p_name)
        if res and res.group(1):
            total_num+=1
            cli = res.group(1)
            vendor = res.group(2)
            if vendor not in vendor_tree:
                vendor_tree[vendor]=[]
            vendor_tree[vendor].append(cli)

print(total_num)
# pprint.pprint(vendor_tree)

vendor_readme_template ='''
# Parser Category by Vendor
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
