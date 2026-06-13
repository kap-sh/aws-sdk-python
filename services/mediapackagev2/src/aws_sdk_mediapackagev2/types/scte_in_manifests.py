"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteInManifests``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

ScteInManifests: TypeAlias = Literal[
    "ALL",
    "MATCHES_FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "MATCHES_FILTER",
    )
)


def serialize_json(value: ScteInManifests) -> str:
    return value


def deserialize_json(data: str) -> ScteInManifests:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScteInManifests value: {data!r}")
    return cast(ScteInManifests, data)
