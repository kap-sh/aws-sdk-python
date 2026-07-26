"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupStatus``."""

from typing import Literal, TypeAlias, cast

InstanceGroupStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Failed",
    "Degraded",
    "SystemUpdating",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGroupStatus:
    return cast(InstanceGroupStatus, data)
