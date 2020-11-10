import __init__
from ctypes import Structure, Union, c_uint8, sizeof, resize
from copy import deepcopy

class Message_Struct(Structure):
    """

    """
    _pack_ = 1
    _fields_ = []

    def __str__(self):
        """

        """
        field_name_idx = 0
        retStr = ""
        retStr += f"{type(self).__name__} \n".rjust(20)
        for field_tuple in super(type(self), self)._fields_:
            if "reserved" in field_tuple[field_name_idx]:
               continue
            else:
                retStr += f"{field_tuple[field_name_idx]}           {getattr(self,field_tuple[field_name_idx])}\n"

        for field_tuple in self._fields_:
            if "reserved" in field_tuple[field_name_idx]:
                continue    # skip all reserved fields from parsing
            else:
                retStr += f"{field_tuple[field_name_idx]}                {getattr(self, field_tuple[field_name_idx])} \n"

        return retStr

class Message_Union(Union):
    """

    """
    _pack_ = 1
    _fields_ = []

class Response_Message(Message_Struct):
    """

    """
    _fields_ = [
        ("status",          c_uint8),
        ("byte_0",          c_uint8, 1),
        ("byte_1",          c_uint8, 1),
        ("byte_2",          c_uint8, 1),
        ("byte_3",          c_uint8, 1),
        ("byte_4",          c_uint8, 1),
        ("byte_5",          c_uint8, 1),
        ("reserved",        c_uint8, 2),
        ("reservedBytes",   c_uint8 * 6)
    ]

class Response_Message_Union(Message_Union):
    """

    """
    _fields_ = [
        ("structure",       Response_Message),
        ("bytes",           sizeof(Response_Message) * c_uint8)
    ]


class Request_Message(Message_Struct):
    """

    """
    _fields_ = [
        ("command",         c_uint8),
    ]

class Request_Message_Union(Message_Union):
    """

    """
    _fields_ = [
        ("structure",       Request_Message),
        ("bytes",           sizeof(Request_Message) * c_uint8)
    ]


class Sanity_Bt_Message(Request_Message):
    """

    """
    _fields_ = [
        ("reservedBytes",   c_uint8 * 7)
    ]

class Sanity_Bt_Message_Union(Message_Union):
    """

    """
    pass


class Sanity_Servo_Message(Request_Message):
    """

    """
    _fields_ = [
        ("reservedBytes", c_uint8 * 7)
    ]

class Sanity_Servo_Message_Union(Message_Union):
    """

    """
    pass


class Sanity_Sensor_Message(Request_Message):
    """

    """
    _fields_ = [
        ("reservedBytes", c_uint8 * 7)
    ]

class Sanity_Sensor_Message_Union(Message_Union):
    """

    """
    pass


class Sanity_PID_Message(Request_Message):
    """

    """
    _fields_ = [
        ("reservedBytes", c_uint8 * 7)
    ]

class Sanity_PID_Message_Union(Message_Union):
    """

    """
    pass


class PID_Controller_Message(Request_Message):
    """

    """
    _fields_ = [
        ("angle",           c_uint8),
        ("algorithm",       c_uint8),
        ("kp",              c_uint8),
        ("ki",              c_uint8),
        ("kd",              c_uint8),
        ("reserved",        c_uint8 * 2)
    ]

class PID_Controller_Message_Union(Message_Union):
    """

    """
    _fields_ = [
        ("structure",       PID_Controller_Message),
        ("bytes",           sizeof(PID_Controller_Message) * c_uint8)
    ]
