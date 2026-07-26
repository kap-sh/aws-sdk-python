"""Generated from Smithy shape ``com.amazonaws.detective#IndicatorType``."""

from typing import Literal, TypeAlias, cast

IndicatorType: TypeAlias = Literal[
    "TTP_OBSERVED",
    "IMPOSSIBLE_TRAVEL",
    "FLAGGED_IP_ADDRESS",
    "NEW_GEOLOCATION",
    "NEW_ASO",
    "NEW_USER_AGENT",
    "RELATED_FINDING",
    "RELATED_FINDING_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: IndicatorType) -> str:
    return value


def deserialize_json(data: str) -> IndicatorType:
    return cast(IndicatorType, data)
