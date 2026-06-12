"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceActiveInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The source at the input device that is currently active."""
InputDeviceActiveInput: TypeAlias = Literal[
    "HDMI",
    "SDI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HDMI",
        "SDI",
    )
)


def serialize_json(value: InputDeviceActiveInput) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceActiveInput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceActiveInput value: {data!r}")
    return cast(InputDeviceActiveInput, data)
