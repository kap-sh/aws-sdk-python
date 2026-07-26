"""Generated from Smithy shape ``com.amazonaws.groundstation#IpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.ip_v4_address

IpAddressList: TypeAlias = list["capo_groundstation.types.ip_v4_address.IpV4Address"]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpAddressList:
    return list(data)
