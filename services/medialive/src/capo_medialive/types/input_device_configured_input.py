"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConfiguredInput``."""

from typing import Literal, TypeAlias, cast

"""The source to activate (use) from the input device."""
InputDeviceConfiguredInput: TypeAlias = Literal[
    "AUTO",
    "HDMI",
    "SDI",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceConfiguredInput) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceConfiguredInput:
    return cast(InputDeviceConfiguredInput, data)
