"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceConfiguredInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The source to activate (use) from the input device."""
InputDeviceConfiguredInput: TypeAlias = Literal[
    "AUTO",
    "HDMI",
    "SDI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "HDMI",
        "SDI",
    )
)


def serialize_json(value: InputDeviceConfiguredInput) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceConfiguredInput:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InputDeviceConfiguredInput value: {data!r}"
        )
    return cast(InputDeviceConfiguredInput, data)
