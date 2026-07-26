"""Generated from Smithy shape ``com.amazonaws.securityir#EngagementType``."""

from typing import Literal, TypeAlias, cast

EngagementType: TypeAlias = Literal[
    "Security Incident",
    "Investigation",
]


# --- restJson1 ser/de ---
def serialize_json(value: EngagementType) -> str:
    return value


def deserialize_json(data: str) -> EngagementType:
    return cast(EngagementType, data)
