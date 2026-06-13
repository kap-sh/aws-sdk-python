"""Generated from Smithy shape ``com.amazonaws.inspector2#IpV6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ip_v6_address

IpV6AddressList: TypeAlias = list["aws_sdk_inspector2.types.ip_v6_address.IpV6Address"]


# --- restJson1 ser/de ---
def serialize_json(value: IpV6AddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV6AddressList:
    return list(data)
