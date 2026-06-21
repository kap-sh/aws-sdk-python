"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActionStatus``."""

from typing import Literal, TypeAlias, cast

ActionStatus: TypeAlias = Literal[
    "Unknown",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    return cast(ActionStatus, data)
