"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_mapping

PortMappings: TypeAlias = list[
    "aws_sdk_global_accelerator.types.port_mapping.PortMapping"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortMappings) -> list:
    import aws_sdk_global_accelerator.types.port_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.port_mapping.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PortMappings:
    import aws_sdk_global_accelerator.types.port_mapping

    out: PortMappings = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.port_mapping.deserialize_aws_json_1_1(item)
        )
    return out
