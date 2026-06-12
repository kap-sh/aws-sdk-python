"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InstanceSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

InstanceSavingsEstimationModeSource: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: InstanceSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceSavingsEstimationModeSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceSavingsEstimationModeSource value: {data!r}"
        )
    return cast(InstanceSavingsEstimationModeSource, data)
