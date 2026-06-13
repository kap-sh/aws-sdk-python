"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerDash``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

AdMarkerDash: TypeAlias = Literal[
    "BINARY",
    "XML",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BINARY",
        "XML",
    )
)


def serialize_json(value: AdMarkerDash) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerDash:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkerDash value: {data!r}")
    return cast(AdMarkerDash, data)
