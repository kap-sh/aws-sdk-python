"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#InputType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

InputType: TypeAlias = Literal[
    "HLS",
    "CMAF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HLS",
        "CMAF",
    )
)


def serialize_json(value: InputType) -> str:
    return value


def deserialize_json(data: str) -> InputType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputType value: {data!r}")
    return cast(InputType, data)
