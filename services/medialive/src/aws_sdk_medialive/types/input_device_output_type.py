"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceOutputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The output attachment type of the input device."""
InputDeviceOutputType: TypeAlias = Literal[
    "NONE",
    "MEDIALIVE_INPUT",
    "MEDIACONNECT_FLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "MEDIALIVE_INPUT",
        "MEDIACONNECT_FLOW",
    )
)


def serialize_json(value: InputDeviceOutputType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceOutputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceOutputType value: {data!r}")
    return cast(InputDeviceOutputType, data)
