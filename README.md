# mx-bng-toolset





##### RADIUS Configuration
```set access profile aaa-profile authentication-order radius
set access profile aaa-profile radius authentication-server 192.168.100.2
set access profile aaa-profile radius accounting-server 192.168.100.2
set access profile aaa-profile radius options interface-description-format exclude-sub-interface
set access profile aaa-profile radius options nas-identifier MX5
set access profile aaa-profile radius options accounting-session-id-format decimal
set access profile aaa-profile radius options vlan-nas-port-stacked-format
set access profile aaa-profile radius-server 192.168.100.2 port 18120
set access profile aaa-profile radius-server 192.168.100.2 accounting-port 1813
set access profile aaa-profile radius-server 192.168.100.2 secret Jun1per
set access profile aaa-profile radius-server 192.168.100.2 timeout 10
set access profile aaa-profile radius-server 192.168.100.2 retry 10
set access profile aaa-profile radius-server 192.168.100.2 source-address 192.168.100.248
set access profile aaa-profile accounting order radius
set access profile aaa-profile accounting accounting-stop-on-failure
set access profile aaa-profile accounting accounting-stop-on-access-deny
set access profile aaa-profile accounting immediate-update
set access profile aaa-profile accounting coa-immediate-update
set access profile aaa-profile accounting update-interval 10
set access profile aaa-profile accounting statistics volume-time```
