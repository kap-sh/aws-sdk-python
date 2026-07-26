"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingListeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_listener

CustomRoutingListeners: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_listener.CustomRoutingListener"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingListeners) -> list:
    import capo_global_accelerator.types.custom_routing_listener

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_listener.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingListeners:
    import capo_global_accelerator.types.custom_routing_listener

    out: CustomRoutingListeners = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_listener.deserialize_aws_json_1_1(
                item
            )
        )
    return out
