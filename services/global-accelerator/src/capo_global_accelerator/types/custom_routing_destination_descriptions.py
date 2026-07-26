"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_destination_description

CustomRoutingDestinationDescriptions: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_destination_description.CustomRoutingDestinationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationDescriptions) -> list:
    import capo_global_accelerator.types.custom_routing_destination_description

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_destination_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingDestinationDescriptions:
    import capo_global_accelerator.types.custom_routing_destination_description

    out: CustomRoutingDestinationDescriptions = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_destination_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
