"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#SharedAudienceMetrics``."""

from typing import Literal, TypeAlias, cast

SharedAudienceMetrics: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharedAudienceMetrics) -> str:
    return value


def deserialize_json(data: str) -> SharedAudienceMetrics:
    return cast(SharedAudienceMetrics, data)
