"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionRecommendationFinding: TypeAlias = Literal[
    "Optimized",
    "NotOptimized",
    "Unavailable",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Optimized",
        "NotOptimized",
        "Unavailable",
    )
)


def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaFunctionRecommendationFinding:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionRecommendationFinding value: {data!r}"
        )
    return cast(LambdaFunctionRecommendationFinding, data)
