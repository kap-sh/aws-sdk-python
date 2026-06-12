"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerPropertiesRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.listener_property_request

ListenerPropertiesRequest: TypeAlias = list[
    "aws_sdk_network_firewall.types.listener_property_request.ListenerPropertyRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerPropertiesRequest) -> list:
    import aws_sdk_network_firewall.types.listener_property_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.listener_property_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListenerPropertiesRequest:
    import aws_sdk_network_firewall.types.listener_property_request

    out: ListenerPropertiesRequest = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.listener_property_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out
