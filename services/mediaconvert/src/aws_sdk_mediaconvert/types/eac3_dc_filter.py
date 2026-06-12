"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3DcFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Activates a DC highpass filter for all input channels."""
Eac3DcFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: Eac3DcFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3DcFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3DcFilter value: {data!r}")
    return cast(Eac3DcFilter, data)
