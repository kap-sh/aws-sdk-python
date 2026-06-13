"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashCompactness``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashCompactness: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "NONE",
    )
)


def serialize_json(value: DashCompactness) -> str:
    return value


def deserialize_json(data: str) -> DashCompactness:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashCompactness value: {data!r}")
    return cast(DashCompactness, data)
