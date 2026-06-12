"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_description

CustomRoutingEndpointDescriptions: TypeAlias = list[
    "aws_sdk_global_accelerator.types.custom_routing_endpoint_description.CustomRoutingEndpointDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointDescriptions) -> list:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingEndpointDescriptions:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_description

    out: CustomRoutingEndpointDescriptions = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
