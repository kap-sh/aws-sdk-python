"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

IdleRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "ResourceType",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Finding",
        "ResourceType",
    )
)


def serialize_aws_json_1_0(value: IdleRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleRecommendationFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdleRecommendationFilterName value: {data!r}"
        )
    return cast(IdleRecommendationFilterName, data)
