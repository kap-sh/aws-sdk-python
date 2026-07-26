"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_destination_configuration

CustomRoutingDestinationConfigurations: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_destination_configuration.CustomRoutingDestinationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationConfigurations) -> list:
    import capo_global_accelerator.types.custom_routing_destination_configuration

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_destination_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingDestinationConfigurations:
    import capo_global_accelerator.types.custom_routing_destination_configuration

    out: CustomRoutingDestinationConfigurations = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_destination_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
