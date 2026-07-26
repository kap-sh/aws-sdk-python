"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.tcp_flag

Flags: TypeAlias = list["capo_network_firewall.types.tcp_flag.TCPFlag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flags) -> list:
    import capo_network_firewall.types.tcp_flag

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.tcp_flag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Flags:
    import capo_network_firewall.types.tcp_flag

    out: Flags = []
    for item in data:
        out.append(capo_network_firewall.types.tcp_flag.deserialize_aws_json_1_0(item))
    return out
