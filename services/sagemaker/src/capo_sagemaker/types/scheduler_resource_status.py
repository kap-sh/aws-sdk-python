"""Generated from Smithy shape ``com.amazonaws.sagemaker#SchedulerResourceStatus``."""

from typing import Literal, TypeAlias, cast

SchedulerResourceStatus: TypeAlias = Literal[
    "Creating",
    "CreateFailed",
    "CreateRollbackFailed",
    "Created",
    "Updating",
    "UpdateFailed",
    "UpdateRollbackFailed",
    "Updated",
    "Deleting",
    "DeleteFailed",
    "DeleteRollbackFailed",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchedulerResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulerResourceStatus:
    return cast(SchedulerResourceStatus, data)
