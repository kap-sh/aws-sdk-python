"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DestinationPorts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_number

DestinationPorts: TypeAlias = list[
    "aws_sdk_global_accelerator.types.port_number.PortNumber"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationPorts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DestinationPorts:
    return list(data)
