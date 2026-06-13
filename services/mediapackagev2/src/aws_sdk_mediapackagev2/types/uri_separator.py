"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UriSeparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

UriSeparator: TypeAlias = Literal[
    "UNDERSCORE",
    "HYPHEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNDERSCORE",
        "HYPHEN",
    )
)


def serialize_json(value: UriSeparator) -> str:
    return value


def deserialize_json(data: str) -> UriSeparator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UriSeparator value: {data!r}")
    return cast(UriSeparator, data)
