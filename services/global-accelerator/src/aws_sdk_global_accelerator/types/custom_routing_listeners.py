"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_listener

CustomRoutingListeners: TypeAlias = list[
    "aws_sdk_global_accelerator.types.custom_routing_listener.CustomRoutingListener"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingListeners) -> list:
    import aws_sdk_global_accelerator.types.custom_routing_listener

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_listener.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingListeners:
    import aws_sdk_global_accelerator.types.custom_routing_listener

    out: CustomRoutingListeners = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_listener.deserialize_aws_json_1_1(
                item
            )
        )
    return out
