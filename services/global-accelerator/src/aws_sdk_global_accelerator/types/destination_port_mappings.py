"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DestinationPortMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.destination_port_mapping

DestinationPortMappings: TypeAlias = list[
    "aws_sdk_global_accelerator.types.destination_port_mapping.DestinationPortMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationPortMappings) -> list:
    import aws_sdk_global_accelerator.types.destination_port_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.destination_port_mapping.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DestinationPortMappings:
    import aws_sdk_global_accelerator.types.destination_port_mapping

    out: DestinationPortMappings = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.destination_port_mapping.deserialize_aws_json_1_1(
                item
            )
        )
    return out
