"""Generated from Smithy shape ``com.amazonaws.detective#IndicatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "TTP_OBSERVED",
        "IMPOSSIBLE_TRAVEL",
        "FLAGGED_IP_ADDRESS",
        "NEW_GEOLOCATION",
        "NEW_ASO",
        "NEW_USER_AGENT",
        "RELATED_FINDING",
        "RELATED_FINDING_GROUP",
    )
)


def serialize_json(value: IndicatorType) -> str:
    return value


def deserialize_json(data: str) -> IndicatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndicatorType value: {data!r}")
    return cast(IndicatorType, data)
