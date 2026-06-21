"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceScanType``."""

from typing import Literal, TypeAlias, cast

"""The scan type of the video source."""
InputDeviceScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceScanType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceScanType:
    return cast(InputDeviceScanType, data)
