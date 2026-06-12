"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The state of the connection between the input device and AWS."""
InputDeviceConnectionState: TypeAlias = Literal[
    "DISCONNECTED",
    "CONNECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCONNECTED",
        "CONNECTED",
    )
)


def serialize_json(value: InputDeviceConnectionState) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceConnectionState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InputDeviceConnectionState value: {data!r}"
        )
    return cast(InputDeviceConnectionState, data)
