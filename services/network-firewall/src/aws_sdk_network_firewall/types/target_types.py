"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TargetTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.target_type

TargetTypes: TypeAlias = list["aws_sdk_network_firewall.types.target_type.TargetType"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TargetTypes) -> list:
    import aws_sdk_network_firewall.types.target_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.target_type.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TargetTypes:
    import aws_sdk_network_firewall.types.target_type

    out: TargetTypes = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.target_type.deserialize_aws_json_1_0(item)
        )
    return out
