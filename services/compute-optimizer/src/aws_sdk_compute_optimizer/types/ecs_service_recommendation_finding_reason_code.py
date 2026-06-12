"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceRecommendationFindingReasonCode: TypeAlias = Literal[
    "MemoryOverprovisioned",
    "MemoryUnderprovisioned",
    "CPUOverprovisioned",
    "CPUUnderprovisioned",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MemoryOverprovisioned",
        "MemoryUnderprovisioned",
        "CPUOverprovisioned",
        "CPUUnderprovisioned",
    )
)


def serialize_aws_json_1_0(value: ECSServiceRecommendationFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceRecommendationFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ECSServiceRecommendationFindingReasonCode value: {data!r}"
        )
    return cast(ECSServiceRecommendationFindingReasonCode, data)
