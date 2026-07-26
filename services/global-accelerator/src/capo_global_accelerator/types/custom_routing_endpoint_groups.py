"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_endpoint_group

CustomRoutingEndpointGroups: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_endpoint_group.CustomRoutingEndpointGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointGroups) -> list:
    import capo_global_accelerator.types.custom_routing_endpoint_group

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_endpoint_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingEndpointGroups:
    import capo_global_accelerator.types.custom_routing_endpoint_group

    out: CustomRoutingEndpointGroups = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_endpoint_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
