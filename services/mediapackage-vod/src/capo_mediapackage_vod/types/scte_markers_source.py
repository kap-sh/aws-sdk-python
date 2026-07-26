"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ScteMarkersSource``."""

from typing import Literal, TypeAlias, cast

ScteMarkersSource: TypeAlias = Literal[
    "SEGMENTS",
    "MANIFEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScteMarkersSource) -> str:
    return value


def deserialize_json(data: str) -> ScteMarkersSource:
    return cast(ScteMarkersSource, data)
