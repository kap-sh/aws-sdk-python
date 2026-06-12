"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration

CustomRoutingEndpointConfigurations: TypeAlias = list[
    "aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration.CustomRoutingEndpointConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointConfigurations) -> list:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingEndpointConfigurations:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration

    out: CustomRoutingEndpointConfigurations = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.custom_routing_endpoint_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
