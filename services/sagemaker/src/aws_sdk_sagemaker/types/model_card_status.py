"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardStatus``."""

from typing import Literal, TypeAlias, cast

ModelCardStatus: TypeAlias = Literal[
    "Draft",
    "PendingReview",
    "Approved",
    "Archived",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardStatus:
    return cast(ModelCardStatus, data)
