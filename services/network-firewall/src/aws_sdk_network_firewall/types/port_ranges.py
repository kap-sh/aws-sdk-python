"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PortRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.port_range

PortRanges: TypeAlias = list["aws_sdk_network_firewall.types.port_range.PortRange"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PortRanges) -> list:
    import aws_sdk_network_firewall.types.port_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.port_range.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PortRanges:
    import aws_sdk_network_firewall.types.port_range

    out: PortRanges = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.port_range.deserialize_aws_json_1_0(item)
        )
    return out
