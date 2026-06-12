"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LambdaSavingsEstimationModeSource: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: LambdaSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaSavingsEstimationModeSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaSavingsEstimationModeSource value: {data!r}"
        )
    return cast(LambdaSavingsEstimationModeSource, data)
