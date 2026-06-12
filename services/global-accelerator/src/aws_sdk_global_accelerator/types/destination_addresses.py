"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DestinationAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.ip_address

DestinationAddresses: TypeAlias = list[
    "aws_sdk_global_accelerator.types.ip_address.IpAddress"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DestinationAddresses:
    return list(data)
