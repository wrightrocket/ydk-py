""" Cisco_IOS_XE_trustsec_oper 

This module contains a collection of YANG definitions
for monitoring of Cisco Trustsec operational information on
Role based permissions, IP\-SGT bindings and SXP connections.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CtsOdmBindingSource(Enum):
    """
    CtsOdmBindingSource

    Binding Source enumeration

    .. data:: default = 0

    	Default Security Group Tag binding value in this device

    	for the given IP-Address

    .. data:: from_vlan = 1

    	Security Group Tag binding value in this device for the given

    	IP-Address is learned from a VLAN

    .. data:: from_cli = 2

    	Security Group Tag binding value in this device

    	for the given

    	IP-Address is configure from CLI (Command Line Inteface)

    .. data:: from_l3if = 3

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned from a L3 (Layer 3) interface

    .. data:: from_cfp = 4

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned via SXP

    	binding exchange protocol

    .. data:: from_ip_arp = 5

    	Security Group Tag binding value in this

    	device for the given

    	IP-Address is learned via IP-ARP protocol

    .. data:: from_local = 6

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned locally

    .. data:: from_sgt_caching = 7

    	Security Group Tag binding value in this device

    	for the given IP-Address is learned via Security Group Tag

    	caching from datapath.

    .. data:: from_cli_hi = 8

    	Security Group Tag binding value in this device

    	for the given IP-Address is configured from CLI-high priority.

    """

    default = Enum.YLeaf(0, "default")

    from_vlan = Enum.YLeaf(1, "from-vlan")

    from_cli = Enum.YLeaf(2, "from-cli")

    from_l3if = Enum.YLeaf(3, "from-l3if")

    from_cfp = Enum.YLeaf(4, "from-cfp")

    from_ip_arp = Enum.YLeaf(5, "from-ip-arp")

    from_local = Enum.YLeaf(6, "from-local")

    from_sgt_caching = Enum.YLeaf(7, "from-sgt-caching")

    from_cli_hi = Enum.YLeaf(8, "from-cli-hi")


class SxpConMode(Enum):
    """
    SxpConMode

    SXP Connection mode

    .. data:: con_mode_invalid = 0

    	SXP Connection mode is Invalid

    .. data:: con_mode_speaker = 1

    	SXP Connection mode is Speaker

    .. data:: con_mode_listener = 2

    	SXP Connection mode is Listener

    .. data:: con_mode_both = 3

    	SXP Connection mode is Both (Speaker and Listener)

    """

    con_mode_invalid = Enum.YLeaf(0, "con-mode-invalid")

    con_mode_speaker = Enum.YLeaf(1, "con-mode-speaker")

    con_mode_listener = Enum.YLeaf(2, "con-mode-listener")

    con_mode_both = Enum.YLeaf(3, "con-mode-both")


class SxpConState(Enum):
    """
    SxpConState

    SXP Connection state

    .. data:: state_off = 0

    	SXP Connection state is OFF

    .. data:: state_pending_on = 1

    	SXP Connection state is Pending-On

    .. data:: state_on = 2

    	SXP Connection state is ON

    .. data:: state_delete_hold_down = 3

    	SXP Connection state is Delete-Hold-Down

    .. data:: state_not_applicable = 4

    	SXP Connection state is Not-Applicable

    """

    state_off = Enum.YLeaf(0, "state-off")

    state_pending_on = Enum.YLeaf(1, "state-pending-on")

    state_on = Enum.YLeaf(2, "state-on")

    state_delete_hold_down = Enum.YLeaf(3, "state-delete-hold-down")

    state_not_applicable = Enum.YLeaf(4, "state-not-applicable")



class TrustsecState(Entity):
    """
    This is top level container for Cisco Trusted Security
    solution operational data.
    It can have Security Group Tag binding information for
    the given IP\-Address, Role based permissions between a
    Source Security Group Tag and a Destination Security
    Group, SXP Connection information for a given peer
    IP\-Address in this device
    
    .. attribute:: cts_rolebased_sgtmaps
    
    	Security Group Tag value corresponding to an IP\-Address  in the given VRF instance in this device
    	**type**\:   :py:class:`CtsRolebasedSgtmaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps>`
    
    .. attribute:: cts_rolebased_policies
    
    	Role based permissions between a Source Security Group and a Destination Security Group are configured by the administrator in the Identity Services Engine or in the Device
    	**type**\:   :py:class:`CtsRolebasedPolicies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies>`
    
    .. attribute:: cts_sxp_connections
    
    	Trustsec SXP connection is used between Cisco devices to propagate Security Group Tags from one device to  another device. One of the device will be in Speaker  mode or Listener mode or both the devices can be in both the connection modes
    	**type**\:   :py:class:`CtsSxpConnections <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections>`
    
    

    """

    _prefix = 'trustsec-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(TrustsecState, self).__init__()
        self._top_entity = None

        self.yang_name = "trustsec-state"
        self.yang_parent_name = "Cisco-IOS-XE-trustsec-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cts-rolebased-sgtmaps" : ("cts_rolebased_sgtmaps", TrustsecState.CtsRolebasedSgtmaps), "cts-rolebased-policies" : ("cts_rolebased_policies", TrustsecState.CtsRolebasedPolicies), "cts-sxp-connections" : ("cts_sxp_connections", TrustsecState.CtsSxpConnections)}
        self._child_list_classes = {}

        self.cts_rolebased_sgtmaps = TrustsecState.CtsRolebasedSgtmaps()
        self.cts_rolebased_sgtmaps.parent = self
        self._children_name_map["cts_rolebased_sgtmaps"] = "cts-rolebased-sgtmaps"
        self._children_yang_names.add("cts-rolebased-sgtmaps")

        self.cts_rolebased_policies = TrustsecState.CtsRolebasedPolicies()
        self.cts_rolebased_policies.parent = self
        self._children_name_map["cts_rolebased_policies"] = "cts-rolebased-policies"
        self._children_yang_names.add("cts-rolebased-policies")

        self.cts_sxp_connections = TrustsecState.CtsSxpConnections()
        self.cts_sxp_connections.parent = self
        self._children_name_map["cts_sxp_connections"] = "cts-sxp-connections"
        self._children_yang_names.add("cts-sxp-connections")
        self._segment_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state"


    class CtsRolebasedSgtmaps(Entity):
        """
        Security Group Tag value corresponding to an IP\-Address 
        in the given VRF instance in this device
        
        .. attribute:: cts_rolebased_sgtmap
        
        	Security Group Tag is assigned for an IP\-Address based on the user permissions and authorization  level as configured by the network administrator in Identity Service Engine server or in the device locally
        	**type**\: list of    :py:class:`CtsRolebasedSgtmap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsRolebasedSgtmaps, self).__init__()

            self.yang_name = "cts-rolebased-sgtmaps"
            self.yang_parent_name = "trustsec-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cts-rolebased-sgtmap" : ("cts_rolebased_sgtmap", TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap)}

            self.cts_rolebased_sgtmap = YList(self)
            self._segment_path = lambda: "cts-rolebased-sgtmaps"
            self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrustsecState.CtsRolebasedSgtmaps, [], name, value)


        class CtsRolebasedSgtmap(Entity):
            """
            Security Group Tag is assigned for an IP\-Address
            based on the user permissions and authorization 
            level as configured by the network administrator
            in Identity Service Engine server or in the device locally
            
            .. attribute:: ip  <key>
            
            	IP\-Prefix information to find its corresponding Secure Group Tag. Only IPv4 prefix information is supported currently to get the Security Group Tag binding in this device
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	VRF\-Name to find the Security Group Tag for the corresponding IP\-Address in this VRF instance. Only default VRF is supported currently which is indicated by (empty string)
            	**type**\:  str
            
            .. attribute:: sgt
            
            	Security Group Tag value corresponding to the given IP\-Address
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: source
            
            	Source information via which the Security Group Tag binding was learned in this device
            	**type**\:   :py:class:`CtsOdmBindingSource <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.CtsOdmBindingSource>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap, self).__init__()

                self.yang_name = "cts-rolebased-sgtmap"
                self.yang_parent_name = "cts-rolebased-sgtmaps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ip = YLeaf(YType.str, "ip")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.sgt = YLeaf(YType.int32, "sgt")

                self.source = YLeaf(YType.enumeration, "source")
                self._segment_path = lambda: "cts-rolebased-sgtmap" + "[ip='" + self.ip.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-rolebased-sgtmaps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap, ['ip', 'vrf_name', 'sgt', 'source'], name, value)


    class CtsRolebasedPolicies(Entity):
        """
        Role based permissions between a Source Security Group
        and a Destination Security Group are configured by the
        administrator in the Identity Services Engine or in the Device
        
        .. attribute:: cts_rolebased_policy
        
        	Role based permissions between a Source Security Group and a Destination Security Group can be retrieved from the device using a Security Group Tag and Destination Group Tag value
        	**type**\: list of    :py:class:`CtsRolebasedPolicy <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsRolebasedPolicies, self).__init__()

            self.yang_name = "cts-rolebased-policies"
            self.yang_parent_name = "trustsec-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cts-rolebased-policy" : ("cts_rolebased_policy", TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy)}

            self.cts_rolebased_policy = YList(self)
            self._segment_path = lambda: "cts-rolebased-policies"
            self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrustsecState.CtsRolebasedPolicies, [], name, value)


        class CtsRolebasedPolicy(Entity):
            """
            Role based permissions between a Source Security Group
            and a Destination Security Group can be retrieved from
            the device using a Security Group Tag and Destination
            Group Tag value
            
            .. attribute:: src_sgt  <key>
            
            	Source Security Group Tag number. This value must be in the inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dst_sgt  <key>
            
            	Destination Security Tag number. This value must be in the inclusive range of \-1 to 65519
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sgacl_name
            
            	List of Security Group Access Control List names separated by semi\-colon(;)
            	**type**\:  str
            
            .. attribute:: num_of_sgacl
            
            	Number of Security Group Access Control Lists that are currently applied between the Source Security Group and the Destination Security Group. This should match the number of Security Group Access Control List names in sgacl\-name
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: monitor_mode
            
            	Indicates the monitor mode status between the Source Security Group and Destination Security Group is currently enabled or disabled. This will be TRUE if monitor mode is enabled and FALSE if it is disabled
            	**type**\:  bool
            
            .. attribute:: policy_life_time
            
            	Duration of the Role based permissions that are applied between a Source Security Group and a Destination Security Group. The duration is represented in seconds
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: last_updated_time
            
            	Indicates the time when the Role based permissions between a Source Security Group and a Destination Security Group was modified or updated last. The value will be represented as date and time  corresponding to the local time zone of the Identify Services Engine when the Role based  permissions was modified or updated last
            	**type**\:  str
            
            .. attribute:: total_deny_count
            
            	Total number of packets that have been denied by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets denied in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_permit_count
            
            	Total number of packets that have been permitted by the Role based permissions between a Source Security Group and a Destination Security Group. This corresponds to total packets allowed in both hardware and software forwarding paths of the device
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_deny_count
            
            	Number of packets that have been denied in the  software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_permit_count
            
            	Number of packets that have been permitted in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_deny_count
            
            	Number of packets that have been denied in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_permit_count
            
            	Number of packets that have been permitted in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: software_monitor_count
            
            	Number of packets that have been monitored in the software forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: hardware_monitor_count
            
            	Number of packets that have been monitored in the hardware forwarding path of the device by the Role based permissions between a Source Security Group and a Destination Security Group
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy, self).__init__()

                self.yang_name = "cts-rolebased-policy"
                self.yang_parent_name = "cts-rolebased-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.src_sgt = YLeaf(YType.int32, "src-sgt")

                self.dst_sgt = YLeaf(YType.int32, "dst-sgt")

                self.sgacl_name = YLeaf(YType.str, "sgacl-name")

                self.num_of_sgacl = YLeaf(YType.uint32, "num-of-sgacl")

                self.monitor_mode = YLeaf(YType.boolean, "monitor-mode")

                self.policy_life_time = YLeaf(YType.uint64, "policy-life-time")

                self.last_updated_time = YLeaf(YType.str, "last-updated-time")

                self.total_deny_count = YLeaf(YType.uint64, "total-deny-count")

                self.total_permit_count = YLeaf(YType.uint64, "total-permit-count")

                self.software_deny_count = YLeaf(YType.uint64, "software-deny-count")

                self.software_permit_count = YLeaf(YType.uint64, "software-permit-count")

                self.hardware_deny_count = YLeaf(YType.uint64, "hardware-deny-count")

                self.hardware_permit_count = YLeaf(YType.uint64, "hardware-permit-count")

                self.software_monitor_count = YLeaf(YType.uint64, "software-monitor-count")

                self.hardware_monitor_count = YLeaf(YType.uint64, "hardware-monitor-count")
                self._segment_path = lambda: "cts-rolebased-policy" + "[src-sgt='" + self.src_sgt.get() + "']" + "[dst-sgt='" + self.dst_sgt.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-rolebased-policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy, ['src_sgt', 'dst_sgt', 'sgacl_name', 'num_of_sgacl', 'monitor_mode', 'policy_life_time', 'last_updated_time', 'total_deny_count', 'total_permit_count', 'software_deny_count', 'software_permit_count', 'hardware_deny_count', 'hardware_permit_count', 'software_monitor_count', 'hardware_monitor_count'], name, value)


    class CtsSxpConnections(Entity):
        """
        Trustsec SXP connection is used between Cisco devices
        to propagate Security Group Tags from one device to 
        another device. One of the device will be in Speaker 
        mode or Listener mode or both the devices can be in
        both the connection modes
        
        .. attribute:: cts_sxp_connection
        
        	Trustsec SXP connection information from a device can be retrieved with the SXP connection peer IP address. Only IPv4 address as Peer IP and default VRF instance in device is supported currently
        	**type**\: list of    :py:class:`CtsSxpConnection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.TrustsecState.CtsSxpConnections.CtsSxpConnection>`
        
        

        """

        _prefix = 'trustsec-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(TrustsecState.CtsSxpConnections, self).__init__()

            self.yang_name = "cts-sxp-connections"
            self.yang_parent_name = "trustsec-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cts-sxp-connection" : ("cts_sxp_connection", TrustsecState.CtsSxpConnections.CtsSxpConnection)}

            self.cts_sxp_connection = YList(self)
            self._segment_path = lambda: "cts-sxp-connections"
            self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrustsecState.CtsSxpConnections, [], name, value)


        class CtsSxpConnection(Entity):
            """
            Trustsec SXP connection information from a device
            can be retrieved with the SXP connection peer IP
            address. Only IPv4 address as Peer IP and default
            VRF instance in device is supported currently
            
            .. attribute:: peer_ip  <key>
            
            	IP\-Address information of the peer of an SXP connection in this device. Only IPv4 address is currently supported
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: vrf_name  <key>
            
            	vrf\-name string of the VRF instance in this device, to which the peer of an SXP connection belongs to. Only default VRF is supported currently which is indicated by empty string
            	**type**\:  str
            
            .. attribute:: source_ip
            
            	Source IP\-Address of the SXP connection in this device for the given peer IP\-Address
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: speaker_state
            
            	SXP speaker state information of the SXP connection in this device. This information is valid only if the local mode of the SXP connection in this device is Speaker
            	**type**\:   :py:class:`SxpConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConState>`
            
            .. attribute:: speaker_duration
            
            	Duration of the SXP speaker of the SXP connection in this device. This information is valid only if the local mode of the SXP connection is Speaker
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: listener_state
            
            	SXP listener state information of the SXP  connection in this device. This information is valid only if the local mode of the SXP connection in the device is Listener
            	**type**\:   :py:class:`SxpConState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConState>`
            
            .. attribute:: listener_duration
            
            	Duration of the SXP listener of the SXP connection in this device. This information is valid Only if the local mode of the SXP connection is Listener
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: local_mode
            
            	SXP connection mode of this device for the SXP connection with the given peer
            	**type**\:   :py:class:`SxpConMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper.SxpConMode>`
            
            

            """

            _prefix = 'trustsec-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(TrustsecState.CtsSxpConnections.CtsSxpConnection, self).__init__()

                self.yang_name = "cts-sxp-connection"
                self.yang_parent_name = "cts-sxp-connections"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.peer_ip = YLeaf(YType.str, "peer-ip")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.source_ip = YLeaf(YType.str, "source-ip")

                self.speaker_state = YLeaf(YType.enumeration, "speaker-state")

                self.speaker_duration = YLeaf(YType.uint64, "speaker-duration")

                self.listener_state = YLeaf(YType.enumeration, "listener-state")

                self.listener_duration = YLeaf(YType.uint64, "listener-duration")

                self.local_mode = YLeaf(YType.enumeration, "local-mode")
                self._segment_path = lambda: "cts-sxp-connection" + "[peer-ip='" + self.peer_ip.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-trustsec-oper:trustsec-state/cts-sxp-connections/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrustsecState.CtsSxpConnections.CtsSxpConnection, ['peer_ip', 'vrf_name', 'source_ip', 'speaker_state', 'speaker_duration', 'listener_state', 'listener_duration', 'local_mode'], name, value)

    def clone_ptr(self):
        self._top_entity = TrustsecState()
        return self._top_entity

