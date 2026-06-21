"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaSavingsEstimationModeSource``."""

from typing import Literal, TypeAlias, cast

LambdaSavingsEstimationModeSource: TypeAlias = Literal[
    "PublicPricing",
    "CostExplorerRightsizing",
    "CostOptimizationHub",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaSavingsEstimationModeSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaSavingsEstimationModeSource:
    return cast(LambdaSavingsEstimationModeSource, data)
