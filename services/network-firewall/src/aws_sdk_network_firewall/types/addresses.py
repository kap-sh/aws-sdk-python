"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.address

Addresses: TypeAlias = list["aws_sdk_network_firewall.types.address.Address"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Addresses) -> list:
    import aws_sdk_network_firewall.types.address

    out: list = []
    for item in value:
        out.append(aws_sdk_network_firewall.types.address.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Addresses:
    import aws_sdk_network_firewall.types.address

    out: Addresses = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.address.deserialize_aws_json_1_0(item)
        )
    return out
