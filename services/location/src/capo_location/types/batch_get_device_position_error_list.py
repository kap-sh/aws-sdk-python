"""Generated from Smithy shape ``com.amazonaws.location#BatchGetDevicePositionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_get_device_position_error

BatchGetDevicePositionErrorList: TypeAlias = list[
    "capo_location.types.batch_get_device_position_error.BatchGetDevicePositionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDevicePositionErrorList) -> list:
    import capo_location.types.batch_get_device_position_error

    out: list = []
    for item in value:
        out.append(
            capo_location.types.batch_get_device_position_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetDevicePositionErrorList:
    import capo_location.types.batch_get_device_position_error

    out: BatchGetDevicePositionErrorList = []
    for item in data:
        out.append(
            capo_location.types.batch_get_device_position_error.deserialize_json(item)
        )
    return out
