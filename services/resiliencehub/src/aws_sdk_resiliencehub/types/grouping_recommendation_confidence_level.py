"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

GroupingRecommendationConfidenceLevel: TypeAlias = Literal[
    "High",
    "Medium",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "High",
        "Medium",
    )
)


def serialize_json(value: GroupingRecommendationConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationConfidenceLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupingRecommendationConfidenceLevel value: {data!r}"
        )
    return cast(GroupingRecommendationConfidenceLevel, data)
