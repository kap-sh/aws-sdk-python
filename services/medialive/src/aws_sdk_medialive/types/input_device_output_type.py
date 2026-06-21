"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceOutputType``."""

from typing import Literal, TypeAlias, cast

"""The output attachment type of the input device."""
InputDeviceOutputType: TypeAlias = Literal[
    "NONE",
    "MEDIALIVE_INPUT",
    "MEDIACONNECT_FLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceOutputType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceOutputType:
    return cast(InputDeviceOutputType, data)
