"""Generated from Smithy shape ``com.amazonaws.budgets#ApprovalModel``."""

from typing import Literal, TypeAlias, cast

ApprovalModel: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalModel:
    return cast(ApprovalModel, data)
