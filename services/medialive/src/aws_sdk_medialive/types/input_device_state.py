"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The state of the input device."""
InputDeviceState: TypeAlias = Literal[
    "IDLE",
    "STREAMING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "STREAMING",
    )
)


def serialize_json(value: InputDeviceState) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceState value: {data!r}")
    return cast(InputDeviceState, data)
