"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionRecommendationFilterName: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionRecommendationFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionRecommendationFilterName value: {data!r}"
        )
    return cast(LambdaFunctionRecommendationFilterName, data)
