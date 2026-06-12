"""Generated from Smithy shape ``com.amazonaws.mediapackage#UtcTiming``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

UtcTiming: TypeAlias = Literal[
    "NONE",
    "HTTP-HEAD",
    "HTTP-ISO",
    "HTTP-XSDATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "HTTP-HEAD",
        "HTTP-ISO",
        "HTTP-XSDATE",
    )
)


def serialize_json(value: UtcTiming) -> str:
    return value


def deserialize_json(data: str) -> UtcTiming:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UtcTiming value: {data!r}")
    return cast(UtcTiming, data)
