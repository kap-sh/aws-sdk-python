"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceStatus``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceStatus: TypeAlias = Literal[
    "Pending",
    "InService",
    "Stopping",
    "Stopped",
    "Failed",
    "Deleting",
    "Updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceStatus:
    return cast(NotebookInstanceStatus, data)
