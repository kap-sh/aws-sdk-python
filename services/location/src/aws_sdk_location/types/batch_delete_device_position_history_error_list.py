"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteDevicePositionHistoryErrorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_delete_device_position_history_error

BatchDeleteDevicePositionHistoryErrorList: TypeAlias = list["aws_sdk_location.types.batch_delete_device_position_history_error.BatchDeleteDevicePositionHistoryError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDevicePositionHistoryErrorList) -> list:
    import aws_sdk_location.types.batch_delete_device_position_history_error
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.batch_delete_device_position_history_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDeleteDevicePositionHistoryErrorList:
    import aws_sdk_location.types.batch_delete_device_position_history_error
    out: BatchDeleteDevicePositionHistoryErrorList = []
    for item in data:
        out.append(aws_sdk_location.types.batch_delete_device_position_history_error.deserialize_json(item))
    return out