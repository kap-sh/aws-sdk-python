"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

CustomRoutingEndpointGroups: TypeAlias = list[
    "aws_sdk_global_accelerator.types.custom_routing_endpoint_group.CustomRoutingEndpointGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointGroups) -> list:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingEndpointGroups:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

    out: CustomRoutingEndpointGroups = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
