"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

ProjectStatus: TypeAlias = Literal[
    "Pending",
    "CreateInProgress",
    "CreateCompleted",
    "CreateFailed",
    "DeleteInProgress",
    "DeleteFailed",
    "DeleteCompleted",
    "UpdateInProgress",
    "UpdateCompleted",
    "UpdateFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectStatus:
    return cast(ProjectStatus, data)
