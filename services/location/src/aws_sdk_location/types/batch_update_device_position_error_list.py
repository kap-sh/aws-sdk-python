"""Generated from Smithy shape ``com.amazonaws.location#BatchUpdateDevicePositionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_update_device_position_error

BatchUpdateDevicePositionErrorList: TypeAlias = list[
    "aws_sdk_location.types.batch_update_device_position_error.BatchUpdateDevicePositionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDevicePositionErrorList) -> list:
    import aws_sdk_location.types.batch_update_device_position_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.batch_update_device_position_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDevicePositionErrorList:
    import aws_sdk_location.types.batch_update_device_position_error

    out: BatchUpdateDevicePositionErrorList = []
    for item in data:
        out.append(
            aws_sdk_location.types.batch_update_device_position_error.deserialize_json(
                item
            )
        )
    return out
