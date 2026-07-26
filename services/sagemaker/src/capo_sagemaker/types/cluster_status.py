"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

ClusterStatus: TypeAlias = Literal[
    "Creating",
    "Deleting",
    "Failed",
    "InService",
    "RollingBack",
    "SystemUpdating",
    "Updating",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
