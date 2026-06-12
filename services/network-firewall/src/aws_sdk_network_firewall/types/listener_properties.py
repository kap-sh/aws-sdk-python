"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.listener_property

ListenerProperties: TypeAlias = list[
    "aws_sdk_network_firewall.types.listener_property.ListenerProperty"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerProperties) -> list:
    import aws_sdk_network_firewall.types.listener_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.listener_property.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListenerProperties:
    import aws_sdk_network_firewall.types.listener_property

    out: ListenerProperties = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.listener_property.deserialize_aws_json_1_0(
                item
            )
        )
    return out
