"""Generated from Smithy shape ``com.amazonaws.inspector#Ipv4AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.ipv4_address

Ipv4AddressList: TypeAlias = list["capo_inspector.types.ipv4_address.Ipv4Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ipv4AddressList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Ipv4AddressList:
    return list(data)
