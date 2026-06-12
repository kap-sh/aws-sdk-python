"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_get_device_position_error

BatchGetDevicePositionErrorList: TypeAlias = list["aws_sdk_location.types.batch_get_device_position_error.BatchGetDevicePositionError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionErrorList) -> list:
    import aws_sdk_location.types.batch_get_device_position_error
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.batch_get_device_position_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetDevicePositionErrorList:
    import aws_sdk_location.types.batch_get_device_position_error
    out: BatchGetDevicePositionErrorList = []
    for item in data:
        out.append(aws_sdk_location.types.batch_get_device_position_error.deserialize_json(item))
    return out