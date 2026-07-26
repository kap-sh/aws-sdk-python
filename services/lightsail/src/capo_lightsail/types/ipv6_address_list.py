"""Generated from Smithy shape ``com.amazonaws.lightsail#Ipv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.ipv6_address

Ipv6AddressList: TypeAlias = list["capo_lightsail.types.ipv6_address.Ipv6Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ipv6AddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Ipv6AddressList:
    return list(data)
