"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_endpoint_configuration

CustomRoutingEndpointConfigurations: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_endpoint_configuration.CustomRoutingEndpointConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointConfigurations) -> list:
    import capo_global_accelerator.types.custom_routing_endpoint_configuration

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_endpoint_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingEndpointConfigurations:
    import capo_global_accelerator.types.custom_routing_endpoint_configuration

    out: CustomRoutingEndpointConfigurations = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_endpoint_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
