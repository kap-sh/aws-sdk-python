"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageStatus``."""

from typing import Literal, TypeAlias, cast

ModelPackageStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageStatus:
    return cast(ModelPackageStatus, data)
