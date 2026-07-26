"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingProtocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_protocol

CustomRoutingProtocols: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_protocol.CustomRoutingProtocol"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingProtocols) -> list:
    import capo_global_accelerator.types.custom_routing_protocol

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_protocol.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingProtocols:
    import capo_global_accelerator.types.custom_routing_protocol

    out: CustomRoutingProtocols = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_protocol.deserialize_aws_json_1_1(
                item
            )
        )
    return out
