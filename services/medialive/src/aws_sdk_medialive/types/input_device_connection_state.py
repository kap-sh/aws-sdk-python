"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConnectionState``."""

from typing import Literal, TypeAlias, cast

"""The state of the connection between the input device and AWS."""
InputDeviceConnectionState: TypeAlias = Literal[
    "DISCONNECTED",
    "CONNECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceConnectionState) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceConnectionState:
    return cast(InputDeviceConnectionState, data)
