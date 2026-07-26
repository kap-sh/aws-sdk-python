"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteInSegments``."""

from typing import Literal, TypeAlias, cast

ScteInSegments: TypeAlias = Literal[
    "NONE",
    "ALL",
    "MATCHES_FILTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScteInSegments) -> str:
    return value


def deserialize_json(data: str) -> ScteInSegments:
    return cast(ScteInSegments, data)
