"""Generated from Smithy shape ``com.amazonaws.inspector2#IpV4AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ip_v4_address

IpV4AddressList: TypeAlias = list["aws_sdk_inspector2.types.ip_v4_address.IpV4Address"]


# --- restJson1 ser/de ---
def serialize_json(value: IpV4AddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV4AddressList:
    return list(data)
