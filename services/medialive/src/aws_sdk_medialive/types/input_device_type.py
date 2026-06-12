"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The type of the input device. For an AWS Elemental Link device that outputs resolutions up to 1080, choose \"HD\"."""
InputDeviceType: TypeAlias = Literal[
    "HD",
    "UHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HD",
        "UHD",
    )
)


def serialize_json(value: InputDeviceType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceType value: {data!r}")
    return cast(InputDeviceType, data)
