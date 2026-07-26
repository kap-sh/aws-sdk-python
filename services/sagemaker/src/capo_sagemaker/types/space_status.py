"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceStatus``."""

from typing import Literal, TypeAlias, cast

SpaceStatus: TypeAlias = Literal[
    "Deleting",
    "Failed",
    "InService",
    "Pending",
    "Updating",
    "Update_Failed",
    "Delete_Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpaceStatus:
    return cast(SpaceStatus, data)
