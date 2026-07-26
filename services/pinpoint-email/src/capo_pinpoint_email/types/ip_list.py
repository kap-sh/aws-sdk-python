"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IpList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.ip

IpList: TypeAlias = list["capo_pinpoint_email.types.ip.Ip"]


# --- restJson1 ser/de ---
def serialize_json(value: IpList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpList:
    return list(data)
