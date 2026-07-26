"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceState``."""

from typing import Literal, TypeAlias, cast

"""The state of the input device."""
InputDeviceState: TypeAlias = Literal[
    "IDLE",
    "STREAMING",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceState) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceState:
    return cast(InputDeviceState, data)
