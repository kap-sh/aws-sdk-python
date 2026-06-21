"""Generated from Smithy shape ``com.amazonaws.sagemaker#StageStatus``."""

from typing import Literal, TypeAlias, cast

StageStatus: TypeAlias = Literal[
    "CREATING",
    "READYTODEPLOY",
    "STARTING",
    "INPROGRESS",
    "DEPLOYED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageStatus:
    return cast(StageStatus, data)
