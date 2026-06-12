"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCode",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Finding",
        "FindingReasonCode",
    )
)


def serialize_aws_json_1_0(value: ECSServiceRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ECSServiceRecommendationFilterName value: {data!r}"
        )
    return cast(ECSServiceRecommendationFilterName, data)
