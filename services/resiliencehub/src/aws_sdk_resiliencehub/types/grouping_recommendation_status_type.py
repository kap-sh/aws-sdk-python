"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

GroupingRecommendationStatusType: TypeAlias = Literal[
    "Accepted",
    "Rejected",
    "PendingDecision",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Accepted",
        "Rejected",
        "PendingDecision",
    )
)


def serialize_json(value: GroupingRecommendationStatusType) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupingRecommendationStatusType value: {data!r}"
        )
    return cast(GroupingRecommendationStatusType, data)
