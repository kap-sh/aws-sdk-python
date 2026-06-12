"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_configuration

EndpointConfigurations: TypeAlias = list[
    "aws_sdk_global_accelerator.types.endpoint_configuration.EndpointConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointConfigurations) -> list:
    import aws_sdk_global_accelerator.types.endpoint_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EndpointConfigurations:
    import aws_sdk_global_accelerator.types.endpoint_configuration

    out: EndpointConfigurations = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.endpoint_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
