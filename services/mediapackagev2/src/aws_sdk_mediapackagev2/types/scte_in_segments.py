"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteInSegments``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

ScteInSegments: TypeAlias = Literal[
    "NONE",
    "ALL",
    "MATCHES_FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ALL",
        "MATCHES_FILTER",
    )
)


def serialize_json(value: ScteInSegments) -> str:
    return value


def deserialize_json(data: str) -> ScteInSegments:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScteInSegments value: {data!r}")
    return cast(ScteInSegments, data)
