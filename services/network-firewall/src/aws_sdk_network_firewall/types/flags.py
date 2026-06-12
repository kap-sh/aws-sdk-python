"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tcp_flag

Flags: TypeAlias = list["aws_sdk_network_firewall.types.tcp_flag.TCPFlag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flags) -> list:
    import aws_sdk_network_firewall.types.tcp_flag

    out: list = []
    for item in value:
        out.append(aws_sdk_network_firewall.types.tcp_flag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Flags:
    import aws_sdk_network_firewall.types.tcp_flag

    out: Flags = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.tcp_flag.deserialize_aws_json_1_0(item)
        )
    return out
