"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The scan type of the video source."""
InputDeviceScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERLACED",
        "PROGRESSIVE",
    )
)


def serialize_json(value: InputDeviceScanType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceScanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceScanType value: {data!r}")
    return cast(InputDeviceScanType, data)
