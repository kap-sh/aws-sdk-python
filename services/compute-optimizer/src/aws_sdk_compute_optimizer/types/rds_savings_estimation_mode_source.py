"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RDSSavingsEstimationModeSource: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: RDSSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSSavingsEstimationModeSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RDSSavingsEstimationModeSource value: {data!r}"
        )
    return cast(RDSSavingsEstimationModeSource, data)
