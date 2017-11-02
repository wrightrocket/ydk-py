""" Cisco_IOS_XR_man_xml_ttyagent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package operational data.

This module contains definitions
for the following management objects\:
  netconf\: NETCONF operational information
  xr\-xml\: xr xml

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class XrXmlSessionAlarmRegister(Enum):
    """
    XrXmlSessionAlarmRegister

    AlarmNotify

    .. data:: registered = 1

    	Registered

    .. data:: not_registered = 2

    	NotRegistered

    """

    registered = Enum.YLeaf(1, "registered")

    not_registered = Enum.YLeaf(2, "not-registered")


class XrXmlSessionState(Enum):
    """
    XrXmlSessionState

    SessionState

    .. data:: idle = 1

    	Idle

    .. data:: busy = 2

    	Busy

    """

    idle = Enum.YLeaf(1, "idle")

    busy = Enum.YLeaf(2, "busy")



class Netconf(Entity):
    """
    NETCONF operational information
    
    .. attribute:: agent
    
    	NETCONF agent operational information
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"agent" : ("agent", Netconf.Agent)}
        self._child_list_classes = {}

        self.agent = Netconf.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf"


    class Agent(Entity):
        """
        NETCONF agent operational information
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Netconf.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tty" : ("tty", Netconf.Agent.Tty)}
            self._child_list_classes = {}

            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._children_yang_names.add("tty")
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/%s" % self._segment_path()


        class Tty(Entity):
            """
            NETCONF agent over TTY
            
            .. attribute:: sessions
            
            	Session information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Netconf.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sessions" : ("sessions", Netconf.Agent.Tty.Sessions)}
                self._child_list_classes = {}

                self.sessions = Netconf.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/%s" % self._segment_path()


            class Sessions(Entity):
                """
                Session information
                
                .. attribute:: session
                
                	Session information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Netconf.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"session" : ("session", Netconf.Agent.Tty.Sessions.Session)}

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Netconf.Agent.Tty.Sessions, [], name, value)


                class Session(Entity):
                    """
                    Session information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Netconf.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.username = YLeaf(YType.str, "username")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")
                        self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Netconf.Agent.Tty.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

    def clone_ptr(self):
        self._top_entity = Netconf()
        return self._top_entity

class XrXml(Entity):
    """
    xr xml
    
    .. attribute:: agent
    
    	XML agents
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(XrXml, self).__init__()
        self._top_entity = None

        self.yang_name = "xr-xml"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"agent" : ("agent", XrXml.Agent)}
        self._child_list_classes = {}

        self.agent = XrXml.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml"


    class Agent(Entity):
        """
        XML agents
        
        .. attribute:: tty
        
        	TTY sessions information
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty>`
        
        .. attribute:: default
        
        	Default sessions information
        	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default>`
        
        .. attribute:: ssl
        
        	SSL sessions information
        	**type**\:   :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl>`
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(XrXml.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "xr-xml"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tty" : ("tty", XrXml.Agent.Tty), "default" : ("default", XrXml.Agent.Default), "ssl" : ("ssl", XrXml.Agent.Ssl)}
            self._child_list_classes = {}

            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._children_yang_names.add("tty")

            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self._children_name_map["default"] = "default"
            self._children_yang_names.add("default")

            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self._children_name_map["ssl"] = "ssl"
            self._children_yang_names.add("ssl")
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/%s" % self._segment_path()


        class Tty(Entity):
            """
            TTY sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sessions" : ("sessions", XrXml.Agent.Tty.Sessions)}
                self._child_list_classes = {}

                self.sessions = XrXml.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"session" : ("session", XrXml.Agent.Tty.Sessions.Session)}

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Tty.Sessions, [], name, value)


                class Session(Entity):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(XrXml.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.username = YLeaf(YType.str, "username")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")
                        self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Tty.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)


        class Default(Entity):
            """
            Default sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Default, self).__init__()

                self.yang_name = "default"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sessions" : ("sessions", XrXml.Agent.Default.Sessions)}
                self._child_list_classes = {}

                self.sessions = XrXml.Agent.Default.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "default"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Default.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "default"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"session" : ("session", XrXml.Agent.Default.Sessions.Session)}

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Default.Sessions, [], name, value)


                class Session(Entity):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(XrXml.Agent.Default.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.username = YLeaf(YType.str, "username")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")
                        self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Default.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)


        class Ssl(Entity):
            """
            SSL sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Ssl, self).__init__()

                self.yang_name = "ssl"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sessions" : ("sessions", XrXml.Agent.Ssl.Sessions)}
                self._child_list_classes = {}

                self.sessions = XrXml.Agent.Ssl.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")
                self._segment_path = lambda: "ssl"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "ssl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"session" : ("session", XrXml.Agent.Ssl.Sessions.Session)}

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Ssl.Sessions, [], name, value)


                class Session(Entity):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(XrXml.Agent.Ssl.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.username = YLeaf(YType.str, "username")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")
                        self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/sessions/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Ssl.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

    def clone_ptr(self):
        self._top_entity = XrXml()
        return self._top_entity

