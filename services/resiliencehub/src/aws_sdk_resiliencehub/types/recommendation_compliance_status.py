"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

RecommendationComplianceStatus: TypeAlias = Literal[
    "BreachedUnattainable",
    "BreachedCanMeet",
    "MetCanImprove",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BreachedUnattainable",
        "BreachedCanMeet",
        "MetCanImprove",
        "MissingPolicy",
    )
)


def serialize_json(value: RecommendationComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RecommendationComplianceStatus value: {data!r}"
        )
    return cast(RecommendationComplianceStatus, data)
