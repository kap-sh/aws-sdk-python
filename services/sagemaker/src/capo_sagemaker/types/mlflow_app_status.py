"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowAppStatus``."""

from typing import Literal, TypeAlias, cast

MlflowAppStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "CreateFailed",
    "Updating",
    "Updated",
    "UpdateFailed",
    "Deleting",
    "DeleteFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlflowAppStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MlflowAppStatus:
    return cast(MlflowAppStatus, data)
