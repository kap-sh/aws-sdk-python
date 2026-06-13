"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UriPathType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

UriPathType: TypeAlias = Literal[
    "LEAF",
    "ROOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEAF",
        "ROOT",
    )
)


def serialize_json(value: UriPathType) -> str:
    return value


def deserialize_json(data: str) -> UriPathType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UriPathType value: {data!r}")
    return cast(UriPathType, data)
