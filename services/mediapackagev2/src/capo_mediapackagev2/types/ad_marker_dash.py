"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerDash``."""

from typing import Literal, TypeAlias, cast

AdMarkerDash: TypeAlias = Literal[
    "BINARY",
    "XML",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdMarkerDash) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerDash:
    return cast(AdMarkerDash, data)
