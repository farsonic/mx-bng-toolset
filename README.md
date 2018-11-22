# mx-bng-toolset





##### RADIUS Configuration
```set access profile aaa-profile authentication-order radius
set access profile aaa-profile radius authentication-server <Server IP>
set access profile aaa-profile radius accounting-server <Server IP>
set access profile aaa-profile radius options nas-identifier <Hostname>
set access profile aaa-profile radius options accounting-session-id-format decimal
set access profile aaa-profile radius options vlan-nas-port-stacked-format
set access profile aaa-profile radius-server <Server IP> port 1812
set access profile aaa-profile radius-server <Server IP> accounting-port 1813
set access profile aaa-profile radius-server <Server IP> secret <Secret>
set access profile aaa-profile radius-server <Server IP> timeout 10
set access profile aaa-profile radius-server <Server IP> retry 10
set access profile aaa-profile radius-server <Server IP> source-address <Router Source IP>
set access profile aaa-profile accounting order radius
set access profile aaa-profile accounting accounting-stop-on-failure
set access profile aaa-profile accounting accounting-stop-on-access-deny
set access profile aaa-profile accounting immediate-update
set access profile aaa-profile accounting coa-immediate-update
set access profile aaa-profile accounting update-interval 10
set access profile aaa-profile accounting statistics volume-time
set access-profile aaa-profile```

##### RADIUS Configuration
```set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" no-traps
set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" vlan-id "$junos-vlan-id"
set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" family pppoe dynamic-profile pppoe-client-profile

set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" ppp-options chap
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" ppp-options pap
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" pppoe-options underlying-interface "$junos-underlying-interface"
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" pppoe-options server
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" keepalives interval 30
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" family inet unnumbered-address lo0.0```
