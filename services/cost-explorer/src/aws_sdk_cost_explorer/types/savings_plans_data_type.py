"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansDataType``."""

from typing import Literal, TypeAlias, cast

SavingsPlansDataType: TypeAlias = Literal[
    "ATTRIBUTES",
    "UTILIZATION",
    "AMORTIZED_COMMITMENT",
    "SAVINGS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SavingsPlansDataType:
    return cast(SavingsPlansDataType, data)
