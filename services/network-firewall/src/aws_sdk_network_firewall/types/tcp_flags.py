"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TCPFlags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tcp_flag_field

TCPFlags: TypeAlias = list["aws_sdk_network_firewall.types.tcp_flag_field.TCPFlagField"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TCPFlags) -> list:
    import aws_sdk_network_firewall.types.tcp_flag_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.tcp_flag_field.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TCPFlags:
    import aws_sdk_network_firewall.types.tcp_flag_field

    out: TCPFlags = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.tcp_flag_field.deserialize_aws_json_1_0(item)
        )
    return out
