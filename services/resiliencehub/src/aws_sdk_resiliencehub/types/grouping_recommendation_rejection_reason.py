"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationRejectionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

GroupingRecommendationRejectionReason: TypeAlias = Literal[
    "DistinctBusinessPurpose",
    "SeparateDataConcern",
    "DistinctUserGroupHandling",
    "Other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DistinctBusinessPurpose",
        "SeparateDataConcern",
        "DistinctUserGroupHandling",
        "Other",
    )
)


def serialize_json(value: GroupingRecommendationRejectionReason) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationRejectionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GroupingRecommendationRejectionReason value: {data!r}"
        )
    return cast(GroupingRecommendationRejectionReason, data)
