"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashDrmSignaling``."""

from typing import Literal, TypeAlias, cast

DashDrmSignaling: TypeAlias = Literal[
    "INDIVIDUAL",
    "REFERENCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashDrmSignaling) -> str:
    return value


def deserialize_json(data: str) -> DashDrmSignaling:
    return cast(DashDrmSignaling, data)
