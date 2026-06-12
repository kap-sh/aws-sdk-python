"""Generated from Smithy shape ``com.amazonaws.storagegateway#VTLDevices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.vtl_device

VTLDevices: TypeAlias = list["aws_sdk_storage_gateway.types.vtl_device.VTLDevice"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VTLDevices) -> list:
    import aws_sdk_storage_gateway.types.vtl_device

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.vtl_device.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VTLDevices:
    import aws_sdk_storage_gateway.types.vtl_device

    out: VTLDevices = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.vtl_device.deserialize_aws_json_1_1(item)
        )
    return out
