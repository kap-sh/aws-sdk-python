"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdMarkupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

AdMarkupType: TypeAlias = Literal[
    "DATERANGE",
    "SCTE35_ENHANCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATERANGE",
        "SCTE35_ENHANCED",
    )
)


def serialize_json(value: AdMarkupType) -> str:
    return value


def deserialize_json(data: str) -> AdMarkupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkupType value: {data!r}")
    return cast(AdMarkupType, data)
