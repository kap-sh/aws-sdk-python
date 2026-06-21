"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteInManifests``."""

from typing import Literal, TypeAlias, cast

ScteInManifests: TypeAlias = Literal[
    "ALL",
    "MATCHES_FILTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScteInManifests) -> str:
    return value


def deserialize_json(data: str) -> ScteInManifests:
    return cast(ScteInManifests, data)
