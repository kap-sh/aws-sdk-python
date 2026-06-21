"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SavingsEstimationMode``."""

from typing import Literal, TypeAlias, cast

SavingsEstimationMode: TypeAlias = Literal[
    "BeforeDiscounts",
    "AfterDiscounts",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsEstimationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SavingsEstimationMode:
    return cast(SavingsEstimationMode, data)
