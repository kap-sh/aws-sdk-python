"""Generated from Smithy shape ``com.amazonaws.costexplorer#RecommendationTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

RecommendationTarget: TypeAlias = Literal[
    "SAME_INSTANCE_FAMILY",
    "CROSS_INSTANCE_FAMILY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAME_INSTANCE_FAMILY",
        "CROSS_INSTANCE_FAMILY",
    )
)


def serialize_aws_json_1_1(value: RecommendationTarget) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationTarget value: {data!r}")
    return cast(RecommendationTarget, data)
