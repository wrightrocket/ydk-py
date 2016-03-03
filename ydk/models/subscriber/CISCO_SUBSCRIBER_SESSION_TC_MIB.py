""" CISCO_SUBSCRIBER_SESSION_TC_MIB 

This MIB module defines textual conventions describing
subscriber sessions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SubSessionRedundancyMode_Enum(Enum):
    """
    SubSessionRedundancyMode_Enum

    An enumerated integer\-value describing the redundancy mode in
    which a subscriber session is operating\:
    
        'none'
            The subscriber session is not part of a redundant
            configuration.
    
        'other'
            The subscriber session is part of a redundant
            configuration and is in a state not recognized by this
            MIB module.
    
        'active'
            The subscriber session is part of a redundant
            configuration and is forwarding traffic from the
            subscriber.
    
        'standby'
            The subscriber session is part of a redundant
            configuration and ready to become active in the case of
            a fail\-over event (e.g., linecard failure).

    """

    NONE = 1

    OTHER = 2

    ACTIVE = 3

    STANDBY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubSessionRedundancyMode_Enum']


class SubSessionState_Enum(Enum):
    """
    SubSessionState_Enum

    An enumerated integer\-value describing the state of a
    subscriber session\:
    
        'other'
            The subscriber session is in a state not recognized by
            the implementation of a MIB module using this textual
            convention.
    
        'pending'
            The subscriber session is in the PENDING state;
            that is, the subscriber session has been initiated and
            the system is in the process of establishing the
            subscriber session.
    
        'up'
            The subscriber session is in the UP state; that is, the
            system has established the subscriber session.

    """

    OTHER = 1

    PENDING = 2

    UP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubSessionState_Enum']


class SubSessionType_Enum(Enum):
    """
    SubSessionType_Enum

    An enumerated integer\-value describing the type of subscriber
    session.  This value has the intent of refining the interface
    type assigned to a subscriber session.  The interface type
    assigned to a subscriber session groups those types of
    subscriber sessions with similar interface semantics.
    
    A PPP subscriber session consists of a PPP connection
    (RFC\-1661)
    and has an interface type of 'ppp'.  The following subscriber
    types refine PPP subscriber sessions\:
    
        'pppSubscriber'
            A PPP connection initiated over a circuit (e.g., an
    ISDN
            line or ATM VC) using the LCP (RFC\-1661).
    
        'pppoeSubscriber'
            A PPP connection over Ethernet (RFC\-2516), initiated
            by a PADI (PPPoE Active Discovery Initiation) packet.
    
        'l2tpSubscriber'
            A PPP connection over an L2TP tunnel (RFC\-2661),
            initiated by an Incoming\-Call\-Request control message.
    
        'l2fSubscriber'
            A PPP connection over an L2F tunnel (RFC\-2341),
            initiated by a L2F\_OPEN message with a non\-zero MID.
    
    An IP subscriber session consists of the routed traffic
    associated with a subscriber IP address having an interface
    type of 'ipSubscriber'.  Routed traffic describes IP traffic
    that transits at least one router.  If a subscriber's IP
    address
    is not unique to the system, further distinguishing
    characteristics, such as VRF or MAC address, form part of the
    subscriber's identity.  The following subscriber types refine
    IP
    subscriber sessions\:
    
        'ipInterfaceSubscriber'
            An IP subcriber session provisioned by the system's
            configuration which consists of all traffic received by
            the interface to which the provisioning applies.
    
        'ipPktSubscriber'
            An IP subscriber session initiated by the receipt of
    the
            first packet received with an unclassified source IP
            address.
    
        'ipDhcpv4Subscriber'
            An IP subscriber session initiated by the receipt of a
            DHCPv4 DISCOVER packet (RFC\-2131).
    
        'ipRadiusSubscriber'
            An IP subscriber session initiated by the receipt of a
            RADIUS Access\-Request packet (RFC\-2865).
    
    An L2 subscriber session consists of the non\-routed traffic
    associated with a subscriber IP address having an interface
    type of 'l2Subscriber'.  Non\-routed traffic describes IP
    traffic
    that doesn't transit a router, meaning that the subscriber must
    be directly connected to the system or have a connection
    through
    an L2 access network (e.g., bridges, switches, and tunnels).
    The
    following subscriber types refine L2 subscriber sessions\:
    
        'l2MacPacketSubscriber'
            An L2 subscriber session initiated by the receipt of
    the
            first layer 2 packet with an unclassified source MAC
            address.
    
        'l2Dhcpv4Subscriber'
            An L2 subscriber session initiated by the receipt of a
            DHCPv4 DISCOVER packet (RFC\-2131).
    
        'l2RadiusSucriber'
            An L2 subscriber session initiated by the receipt of a
            RADIUS Access\-Request packet (RFC\-2865).
    
    The system should assign the value 'other' to any subscriber
    session not recognized by the implementation of a MIB module
    using this textual convention.
    
    The value 'all' represents a special value used to indicate all
    subscriber session types.  For example, a scope of aggregation
    that includes all subscriber session types uses this value to
    indicate this fact.

    """

    ALL = 1

    OTHER = 2

    PPPSUBSCRIBER = 3

    PPPOESUBSCRIBER = 4

    L2TPSUBSCRIBER = 5

    L2FSUBSCRIBER = 6

    IPINTERFACESUBSCRIBER = 7

    IPPKTSUBSCRIBER = 8

    IPDHCPV4SUBSCRIBER = 9

    IPRADIUSSUBSCRIBER = 10

    L2MACSUBSCRIBER = 11

    L2DHCPV4SUBSCRIBER = 12

    L2RADIUSSUBSCRIBER = 13


    @staticmethod
    def _meta_info():
        from ydk.models.subscriber._meta import _CISCO_SUBSCRIBER_SESSION_TC_MIB as meta
        return meta._meta_table['SubSessionType_Enum']


class SubSessionTypes_Bits(FixedBitsDict):
    """
    SubSessionTypes_Bits

    A bit string describing a set of subscriber session types\:
    
    'pppSubscriber'
        A PPP connection initiated over a circuit (e.g., an ISDN
        line or ATM VC) using the LCP (RFC\-1661).
    
    'pppoeSubscriber'
        A PPP connection over Ethernet (RFC\-2516), initiated
        by a PADI (PPPoE Active Discovery Initiation) packet.
    
    'l2tpSubscriber'
        A PPP connection over an L2TP tunnel (RFC\-2661),
        initiated by an Incoming\-Call\-Request control message.
    
    'l2fSubscriber'
        A PPP connection over an L2F tunnel (RFC\-2341),
        initiated by a L2F\_OPEN message with a non\-zero MID.
    
    'ipInterfaceSubscriber'
        An IP subcriber session provisioned by the system's
        configuration which consists of all traffic received by
        the interface the provisioning applies.
    
    'ipPktSubscriber'
        An IP subscriber session initiated by the receipt of
        the first packet received with an unclassified source IP
        address.
    
    'ipDhcpv4Subscriber'
        An IP subscriber session initiated by the receipt of a
        DHCPv4 DISCOVER packet (RFC\-2131).
    
    'ipRadiusSubscriber'
        An IP subscriber session initiated by the receipt of a
        RADIUS Access\-Request packet (RFC\-2865).
    
    'l2MacSubscriber'
        An L2 subscriber session initiated by the receipt of the
        first layer 2 packet with an unclassified source MAC
        address.
    
    'l2Dhcpv4Subscriber'
        An L2 subscriber session initiated by the receipt of a
        DHCPv4 DISCOVER packet (RFC\-2131).
    
    'l2RadiusSubscriber'
        An L2 subscriber session initiated by the receipt of a
        RADIUS Access\-Request packet (RFC\-2865).
    
    For more details regarding subscriber session types, see the
    descriptive text associated with the SubSessionType textual
    convention.
    Keys are:- ipRadiusSubscriber , pppSubscriber , l2RadiusSubscriber , ipPktSubscriber , ipInterfaceSubscriber , pppoeSubscriber , l2fSubscriber , l2tpSubscriber , l2Dhcpv4Subscriber , ipDhcpv4Subscriber , l2MacSubscriber

    """

    def __init__(self):
        self._dictionary = { 
            'ipRadiusSubscriber':False,
            'pppSubscriber':False,
            'l2RadiusSubscriber':False,
            'ipPktSubscriber':False,
            'ipInterfaceSubscriber':False,
            'pppoeSubscriber':False,
            'l2fSubscriber':False,
            'l2tpSubscriber':False,
            'l2Dhcpv4Subscriber':False,
            'ipDhcpv4Subscriber':False,
            'l2MacSubscriber':False,
        }
        self._pos_map = { 
            'ipRadiusSubscriber':7,
            'pppSubscriber':0,
            'l2RadiusSubscriber':10,
            'ipPktSubscriber':5,
            'ipInterfaceSubscriber':4,
            'pppoeSubscriber':1,
            'l2fSubscriber':3,
            'l2tpSubscriber':2,
            'l2Dhcpv4Subscriber':9,
            'ipDhcpv4Subscriber':6,
            'l2MacSubscriber':8,
        }

