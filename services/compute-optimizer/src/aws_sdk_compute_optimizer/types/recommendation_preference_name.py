"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferenceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RecommendationPreferenceName: TypeAlias = Literal[
    "EnhancedInfrastructureMetrics",
    "InferredWorkloadTypes",
    "ExternalMetricsPreference",
    "LookBackPeriodPreference",
    "PreferredResources",
    "UtilizationPreferences",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EnhancedInfrastructureMetrics",
        "InferredWorkloadTypes",
        "ExternalMetricsPreference",
        "LookBackPeriodPreference",
        "PreferredResources",
        "UtilizationPreferences",
    )
)


def serialize_aws_json_1_0(value: RecommendationPreferenceName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendationPreferenceName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RecommendationPreferenceName value: {data!r}"
        )
    return cast(RecommendationPreferenceName, data)
