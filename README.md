#### Initial FreeRadius Setup

#### FreeRadius - mySQL integration

#### Basic Jnuiper MX-Series BNG Configuration

##### Global settings 
In order to use some of the newer subscriber features the following configuration needs to be added to the system. Changing network-services mode will requrie the router to be rebooted. 
```
set chassis network-services enhanced-ip
set system services subscriber-management enable
```

##### RADIUS Configuration
Set up access to the RADIUS Server first for both Authentication and Accounting. The configuration example uses the standard ports but obviously both the server IP address and port numbers should be adjusted to suit your setup. 
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
set access-profile aaa-profile
```

##### Dynamic Profile (Single VLAN Tag)
A dynamic profile defines the parameters of an interface when a user authenticates. The example here is to be attached to a physical interface that has one vlan tag. This will not work on an untagged interface or stacked VLAN tagged interface. 
```set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" no-traps
set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" vlan-id "$junos-vlan-id"
set dynamic-profiles vlan-single-tag interfaces "$junos-interface-ifd-name" unit "$junos-interface-unit" family pppoe dynamic-profile pppoe-client-profile
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" ppp-options chap
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" ppp-options pap
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" pppoe-options underlying-interface "$junos-underlying-interface"
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" pppoe-options server
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" keepalives interval 30
set dynamic-profiles pppoe-client-profile interfaces pp0 unit "$junos-interface-unit" family inet unnumbered-address lo0.0
```

##### Dynamic Interface assignment
The Dynamic profiles are then assocated with one or more physical interfaces. In this example the interface will accept any VLAN tag between 1 and 2000 and then apply the PPPoE profile. Once successfully authenticated a new dynamic interface will be created in the system. 
```set interfaces <interface> flexible-vlan-tagging
set interfaces <interface> auto-configure vlan-ranges dynamic-profile vlan-single-tag accept pppoe
set interfaces <interface> auto-configure vlan-ranges dynamic-profile vlan-single-tag ranges 1-2000
set interfaces <interface> auto-configure vlan-ranges dynamic-profile vlan-single-tag access-profile aaa-profile
```

##### Routing Instance
Optionally, subscribers can be placed into a dedicated routing-instance. This can be defined in the dynamic profile or as part of the return RADIUS VSA when authentication occurs. 
```set routing-instances subscribers instance-type vrf
set routing-instances subscribers access address-assignment high-utilization 90
set routing-instances subscribers access address-assignment abated-utilization 70
set routing-instances subscribers access address-assignment pool subscriber_pool family inet network 10.100.0.0/16
set routing-instances subscribers access address-assignment pool subscriber_pool family inet range subscriber_range low 10.100.0.0
set routing-instances subscribers access address-assignment pool subscriber_pool family inet range subscriber_range high 10.100.255.255
set routing-instances subscribers interface lo0.100
set routing-instances subscribers route-distinguisher 100:101
set routing-instances subscribers vrf-target target:100:101
set routing-instances subscribers vrf-table-label
```

