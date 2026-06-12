"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceRecommendationFinding: TypeAlias = Literal[
    "Optimized",
    "Underprovisioned",
    "Overprovisioned",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Optimized",
        "Underprovisioned",
        "Overprovisioned",
    )
)


def serialize_aws_json_1_0(value: ECSServiceRecommendationFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFinding:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ECSServiceRecommendationFinding value: {data!r}"
        )
    return cast(ECSServiceRecommendationFinding, data)
