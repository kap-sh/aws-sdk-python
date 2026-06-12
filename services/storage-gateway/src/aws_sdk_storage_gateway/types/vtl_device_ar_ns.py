"""Generated from Smithy shape ``com.amazonaws.storagegateway#VTLDeviceARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.vtl_device_arn

VTLDeviceARNs: TypeAlias = list[
    "aws_sdk_storage_gateway.types.vtl_device_arn.VTLDeviceARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VTLDeviceARNs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VTLDeviceARNs:
    return list(data)
