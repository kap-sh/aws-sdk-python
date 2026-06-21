"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AchievabilityStatus``."""

from typing import Literal, TypeAlias, cast

AchievabilityStatus: TypeAlias = Literal[
    "ACHIEVABLE",
    "NOT_ACHIEVABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AchievabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> AchievabilityStatus:
    return cast(AchievabilityStatus, data)
