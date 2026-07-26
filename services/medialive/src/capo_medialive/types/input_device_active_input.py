"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceActiveInput``."""

from typing import Literal, TypeAlias, cast

"""The source at the input device that is currently active."""
InputDeviceActiveInput: TypeAlias = Literal[
    "HDMI",
    "SDI",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceActiveInput) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceActiveInput:
    return cast(InputDeviceActiveInput, data)
