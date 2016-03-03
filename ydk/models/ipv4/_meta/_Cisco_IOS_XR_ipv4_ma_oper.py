


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RpfMode_Enum' : _MetaInfoEnum('RpfMode_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_oper',
        {
            'strict':'STRICT',
            'loose':'LOOSE',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper']),
    'Ipv4MaOperLineState_Enum' : _MetaInfoEnum('Ipv4MaOperLineState_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_ma_oper',
        {
            'unknown':'UNKNOWN',
            'shutdown':'SHUTDOWN',
            'down':'DOWN',
            'up':'UP',
        }, 'Cisco-IOS-XR-ipv4-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper']),
}