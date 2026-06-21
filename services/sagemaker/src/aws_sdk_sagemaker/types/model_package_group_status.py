"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroupStatus``."""

from typing import Literal, TypeAlias, cast

ModelPackageGroupStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageGroupStatus:
    return cast(ModelPackageGroupStatus, data)
