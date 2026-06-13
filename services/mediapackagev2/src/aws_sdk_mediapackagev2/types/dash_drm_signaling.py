"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDrmSignaling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashDrmSignaling: TypeAlias = Literal[
    "INDIVIDUAL",
    "REFERENCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDIVIDUAL",
        "REFERENCED",
    )
)


def serialize_json(value: DashDrmSignaling) -> str:
    return value


def deserialize_json(data: str) -> DashDrmSignaling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashDrmSignaling value: {data!r}")
    return cast(DashDrmSignaling, data)
