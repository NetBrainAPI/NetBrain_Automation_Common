import os
import re
import pprint
from jinja2 import Template 

resource_path = os.getcwd()+r"\Auto_Data_View_Template"
list_dir = os.listdir(resource_path)
# pprint.pprint(list_dir)
# ['aaa [(Alcatel OmniSwitch)(Alcatel OmniStack)]',
#  'aaa [Arista Switch]',
#  'acl [(Cisco IOS Switch)(Cisco Router)]',
#  'anyconnect [Cisco ASA Firewall]',
#  'apm [F5 Load Balancer]',
#  'bfd [Alcatel Lucent Service Router]',
#  'bgp [(Alcatel OmniSwitch)(Alcatel OmniStack)]',
#  'bgp [(Checkpoint Gaia)(Checkpoint Gaia R80)]',
#  'bgp [(Cisco IOS Switch)(Cisco Router)]',
#  'bgp [(Dell Networking Switch)(Dell Force10 Switch)]',
#  'bgp [(Juniper Router)(Juniper EX Switch)(Juniper SRX Firewall)]',
#  'bgp [3Com Switch]']

total_num = len(list_dir)
print(total_num)

vendor_tree = {}
feature_tree = {}

re_match = r'(.+?)(\[.+\])'
for names in list_dir:
    res = re.match(re_match,names)
    feature = res.group(1)
    vendor = res.group(2)
    if feature not in feature_tree:
        feature_tree[feature]=[]
    feature_tree[feature].append(vendor)

    if vendor not in vendor_tree:
        vendor_tree[vendor]=[]
    vendor_tree[vendor].append(feature)

# pprint.pprint(feature_tree)
# pprint.pprint(vendor_tree)

vendor_readme_template ='''
# Auto DVT Group by Vendor
{% for vendor in vendor_tree %}
## {{vendor}}
{% for feature in vendor_tree[vendor] %}
* {{feature}}
{% endfor %}
{% endfor %}
'''
vendor_res = Template(vendor_readme_template)
vendor_res_txt = vendor_res.render(vendor_tree=vendor_tree)
# print(vendor_res_txt)

feature_readme_template ='''
# Auto DVT Group by Feature
{% for feature in feature_tree %}
## {{feature}}
{% for vendor in feature_tree[feature] %}
* {{vendor}}
{% endfor %}
{% endfor %}
'''

feature_res = Template(feature_readme_template)
feature_res_txt = feature_res.render(feature_tree=feature_tree)
# print(feature_res_txt)

with open('byFeature.md','w', newline='') as f_readme1:
    f_readme1.write(feature_res_txt)
f_readme1.close()

with open('byVendor.md','w',newline='') as f_readme2:
    f_readme2.write(vendor_res_txt)
f_readme2.close()