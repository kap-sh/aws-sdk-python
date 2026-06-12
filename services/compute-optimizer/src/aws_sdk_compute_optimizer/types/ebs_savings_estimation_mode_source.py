"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EBSSavingsEstimationModeSource: TypeAlias = Literal[
    "PublicPricing",
    "CostExplorerRightsizing",
    "CostOptimizationHub",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PublicPricing",
        "CostExplorerRightsizing",
        "CostOptimizationHub",
    )
)


def serialize_aws_json_1_0(value: EBSSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EBSSavingsEstimationModeSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EBSSavingsEstimationModeSource value: {data!r}"
        )
    return cast(EBSSavingsEstimationModeSource, data)
