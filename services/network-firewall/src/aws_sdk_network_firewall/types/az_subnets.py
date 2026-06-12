"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AzSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.az_subnet

AzSubnets: TypeAlias = list["aws_sdk_network_firewall.types.az_subnet.AzSubnet"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AzSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AzSubnets:
    return list(data)
