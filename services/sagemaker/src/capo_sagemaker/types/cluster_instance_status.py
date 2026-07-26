"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStatus``."""

from typing import Literal, TypeAlias, cast

ClusterInstanceStatus: TypeAlias = Literal[
    "Running",
    "Failure",
    "Pending",
    "ShuttingDown",
    "SystemUpdating",
    "DeepHealthCheckInProgress",
    "NotFound",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterInstanceStatus:
    return cast(ClusterInstanceStatus, data)
