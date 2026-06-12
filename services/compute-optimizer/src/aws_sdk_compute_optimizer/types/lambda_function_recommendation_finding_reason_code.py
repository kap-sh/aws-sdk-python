"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendationFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaFunctionRecommendationFindingReasonCode: TypeAlias = Literal[
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "InsufficientData",
    "Inconclusive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MemoryOverprovisioned",
        "MemoryUnderprovisioned",
        "InsufficientData",
        "Inconclusive",
    )
)


def serialize_aws_json_1_0(value: LambdaFunctionRecommendationFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> LambdaFunctionRecommendationFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaFunctionRecommendationFindingReasonCode value: {data!r}"
        )
    return cast(LambdaFunctionRecommendationFindingReasonCode, data)
