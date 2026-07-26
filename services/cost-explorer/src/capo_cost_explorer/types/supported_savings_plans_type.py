"""Generated from Smithy shape ``com.amazonaws.costexplorer#SupportedSavingsPlansType``."""

from typing import Literal, TypeAlias, cast

SupportedSavingsPlansType: TypeAlias = Literal[
    "COMPUTE_SP",
    "EC2_INSTANCE_SP",
    "SAGEMAKER_SP",
    "DATABASE_SP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedSavingsPlansType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SupportedSavingsPlansType:
    return cast(SupportedSavingsPlansType, data)
