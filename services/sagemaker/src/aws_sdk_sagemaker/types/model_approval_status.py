"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelApprovalStatus``."""

from typing import Literal, TypeAlias, cast

ModelApprovalStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
    "PendingManualApproval",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelApprovalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelApprovalStatus:
    return cast(ModelApprovalStatus, data)
